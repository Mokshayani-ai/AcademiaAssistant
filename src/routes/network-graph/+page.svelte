<script lang="ts">
  import { onMount } from 'svelte';

  let container: HTMLDivElement | undefined;
  let network: any;

  // Define the type of nodes and edges
  type Node = {
    id: number;
    label: string;
  };

  type Edge = {
    from: number;
    to: number;
  };

  let nodes: Node[] = [];
  let edges: Edge[] = [];

  // Sample JSON data representing publications and authors
  let publications = [
      {
      "title": "Performance comparison of time series data using predictive data mining techniques",
      "source": "Google Scholar",
      "url": "https://www.researchgate.net/publication/274315018_PERFORMANCE_COMPARISON_OF_TIME_SERIES_DATA_USING_PREDICTIVE_DATA_MINING_TECHNIQUES_Advances_in_Information_Mining",
      "authors": ["Saigal S.", "Deepti Mehrotra"]
      },
      {
          "title": "Another Research Paper",
          "source": "Google Scholar",
          "url": "https://example.com",
          "authors": ["Saigal S.", "John Doe"]
      },
      {
          "title": "Further Advances in Predictive Data Mining",
          "source": "Google Scholar",
          "url": "https://example.com",
          "authors": ["Deepti Mehrotra", "Jane Smith"]
      },
      {
          "title": "Comparative Review of Selection Techniques in Genetic Algorithm",
          "source": "Google Scholar",
          "url": "https://ieeexplore.ieee.org/document/7154916",
          "authors": [
              "Anupriya Shukla",
              "Hari Mohan Pandey",
              "Deepti Mehrotra"
          ],
          
     },
     
      {
          "title": "A comparative review of approaches to prevent premature convergence in GA",
          "source": "Google Scholar",
          "url": "https://www.sciencedirect.com/science/article/pii/S1568494614003901",
          "authors": [
              "Hari Mohan Pandey",
              "Ankit Chaudhary",
              "Deepti Mehrotra"
          ],
         
      },
      {
          "title": "Performance comparison of time series data using predictive data mining techniques",
          "source": "Google Scholar",
          "url": "https://www.researchgate.net/publication/274315018_PERFORMANCE_COMPARISON_OF_TIME_SERIES_DATA_USING_PREDICTIVE_DATA_MINING_TECHNIQUES_Advances_in_Information_Mining",
          "authors": [
              "Saigal S.",
              "Deepti Mehrotra"
          ],
      },
  ];

  onMount(() => {
    if (window.vis && container) {
      const { Network, DataSet } = window.vis;

      // Extract unique authors and co-authorship relationships
      let authorsMap = new Map<string, number>();
      let nodeId = 1;

      publications.forEach(pub => {
        let authors = pub.authors;

        // Create nodes for each author if not already created
        authors.forEach(author => {
          if (!authorsMap.has(author)) {
            authorsMap.set(author, nodeId);
            nodes.push({ id: nodeId, label: author });
            nodeId++;
          }
        });

        // Create edges for co-authors
        for (let i = 0; i < authors.length; i++) {
          for (let j = i + 1; j < authors.length; j++) {
            let author1Id = authorsMap.get(authors[i]);
            let author2Id = authorsMap.get(authors[j]);

            if (author1Id && author2Id) {
              edges.push({ from: author1Id, to: author2Id });
            }
          }
        }
      });

      // Create a vis-network graph
      const data = {
        nodes: new DataSet(nodes),
        edges: new DataSet(edges)
      };

      const options = {
        layout: {
          improvedLayout: true
        },
        nodes: {
          shape: 'dot',
          size: 15,
          font: {
            size: 14,
            color: '#333'
          },
          color: {
            border: '#000',
            background: '#f0f0f0'
          }
        },
        edges: {
          width: 2,
          color: '#000'
        },
        physics: {
          enabled: true,
          stabilization: { iterations: 100 }
        }
      };

      network = new Network(container, data, options);
    } else {
      console.error('vis-network is not loaded or container is not available');
    }
  });
</script>

<style>
.network-container {
  width: 100%;
  height: 600px;
  border: 1px solid #000;
}

h2 {
  font-family: 'Poppins', sans-serif;
  text-align: center;
  margin-bottom: 20px;
  font-size: 40px;
}
</style>

<h2>Co-Author Network Graph</h2>
<div class="network-container" bind:this={container}></div>
