import os
import json
from flask import Flask, request, jsonify
from Scraper import ScholarlyScraper, DBLPScraper, merge_publications_with_urls
from LLMInference import ResearchIdentifier, Topfields
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CACHE_DIR = 'cache'

# Create cache directory if it doesn't exist
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def save_to_cache(file_name, data):
    file_path = os.path.join(CACHE_DIR, file_name)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_cache(file_name):
    file_path = os.path.join(CACHE_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None

def orchestrate_scrape(author_name, limit=None, h_index=None, i10_index=None, year=None):
    # Step 1: Scrape and merge publications
    google_scraper = ScholarlyScraper(author_name)
    google_data = google_scraper.fetch_publications()
    dblp_scraper = DBLPScraper(author_name)
    dblp_data = dblp_scraper.fetch_publications()
    merged_publications = merge_publications_with_urls(google_data['publications'], dblp_data, author_name, limit)
    
    filtered_publications = []
    for pub in merged_publications:
        if isinstance(pub, dict) and 'publication year' in pub:
            pub_year = pub['publication year'].get('year', 0)
            if year and pub_year < year:
                continue
            filtered_publications.append(pub)
        else:
            print(f"Skipping invalid publication: {pub}")
    
    final_data_with_metadata = {
        'author': google_data['author'],
        'h_index': google_data['h_index'],
        'i10_index': google_data['i10_index'],
        'publications': filtered_publications
    }
    
    # Save scraped data to cache
    save_to_cache(f"{author_name}_all.json", final_data_with_metadata)
    return final_data_with_metadata

def orchestrate_publication_mapping(author_name):
    # Load previously saved scraped data
    cached_data = load_from_cache(f"{author_name}_all.json")
    if not cached_data:
        return None
    
    # Step 2: Run LLM to map publications to research areas and subjects
    research_identifier = ResearchIdentifier()
    for pub in cached_data['publications']:
        summary = pub.get('summary', '')
        title = pub.get('title', '')
        if summary and title:
            subject_area_json = research_identifier.identify_research(title, summary)
            try:
                subject_area = json.loads(subject_area_json)
                pub['research_subject'] = subject_area.get('research_subject', 'N/A')
                pub['research_area'] = subject_area.get('research_area', 'N/A')
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON for publication '{pub['title']}': {e}")
                pub['research_subject'] = 'N/A'
                pub['research_area'] = 'N/A'
    
    final_data = {
        'author': cached_data['author'],
        'publication_mappings': [
            {
                'id': idx + 1,
                'title': pub['title'],
                'research_subject': pub.get('research_subject', 'N/A'),
                'research_area': pub.get('research_area', 'N/A')
            }
            for idx, pub in enumerate(cached_data['publications'])
        ]
    }
    
    # Save publication mapping to cache
    save_to_cache(f"{author_name}_publications.json", final_data)
    return final_data

def orchestrate_interests(author_name, limit=None):
    # Load previously saved publication mapping
    cached_data = load_from_cache(f"{author_name}_publications.json")
    if not cached_data:
        return None

    # Step 3: Generate author's research interests using Topfields
    tops = Topfields()
    result = tops.identify_research_fields(cached_data["publication_mappings"], limit)
    
    # Save research interests to cache
    save_to_cache(f"{author_name}_interests.json", result)
    return result

# Route 1: Scrape author details
@app.route('/scrape', methods=['GET'])
def scrape():
    author_name = request.args.get('author')
    limit = request.args.get('limit', type=int)
    h_index = request.args.get('h_index', type=int)
    i10_index = request.args.get('i10_index', type=int)
    year = request.args.get('year', type=int)
    
    if not author_name:
        return jsonify({"error": "Author name is required"}), 400
    
    result = orchestrate_scrape(author_name, limit, h_index, i10_index, year)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Unable to scrape data"}), 500

# Route 2: Generate publication mappings
@app.route('/publications', methods=['GET'])
def publications():
    author_name = request.args.get('author')
    
    if not author_name:
        return jsonify({"error": "Author name is required"}), 400
    
    result = orchestrate_publication_mapping(author_name)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "No cached data available, run /scrape first"}), 500

# Route 3: Generate research interests
@app.route('/interests', methods=['GET'])
def interests():
    author_name = request.args.get('author')
    limit = request.args.get('limit', type=int)
    
    if not author_name:
        return jsonify({"error": "Author name is required"}), 400
    
    result = orchestrate_interests(author_name, limit)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "No cached data available, run /publications first"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5173)
