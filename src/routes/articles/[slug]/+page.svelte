<!-- src/routes/article/[slug]/+page.svelte -->

<script lang="ts">
    export let article: {
      slug: string;
      title: string;
      content: string;
    };
  </script>
  
  <main>
    <div class="dashboard">
      <!-- Left Column -->
      <div class="card left-card">
        <div class="recent">
          <h2>Recent</h2>
          <ul>
            <li>User Pages</li>
            <li>User Groups</li>
            <li>Suggested Groups</li>
            <li>Events</li>
          </ul>
        </div>
  
        <!-- Discover Articles Section -->
        <div class="discover-articles">
          <h2>Discover Articles</h2>
          <ul>
            <li><a href="/article/article-1">Article 1 Title - First line of the article</a></li>
            <li><a href="/article/article-2">Article 2 Title - First line of the article</a></li>
            <!-- Add more articles as needed -->
          </ul>
        </div>
      </div>
  
      <!-- Center Column -->
      <div class="card center-card">
        {#if article}
          <article>
            <h1>{article.title}</h1>
            <div>{@html article.content}</div>
          </article>
        {:else}
          <p>Article not found.</p>
        {/if}
      </div>
  
      <!-- Right Column -->
      <div class="card right-card">
        <h2>Recent Activity</h2>
        <ul>
          <li>New Collaborations</li>
          <li>Recent Events</li>
          <li>Recent Publications</li>
        </ul>
  
        <!-- Discover Profiles Section (Instagram-style) -->
        <div class="discover-profiles">
          <h2>Discover Profiles</h2>
          <div class="profile-suggestions">
            <!-- Profile 1 -->
            <div class="profile">
              <img src="/path-to-avatar1.jpg" alt="Alice Johnson" class="profile-avatar">
              <div class="profile-info">
                <h4>Alice Johnson</h4>
                <p>AI Researcher</p>
              </div>
              <button class="follow-button">Follow</button>
            </div>
  
            <!-- Profile 2 -->
            <div class="profile">
              <img src="/path-to-avatar2.jpg" alt="Michael Lee" class="profile-avatar">
              <div class="profile-info">
                <h4>Michael Lee</h4>
                <p>Data Scientist</p>
              </div>
              <button class="follow-button">Follow</button>
            </div>
  
            <!-- Profile 3 -->
            <div class="profile">
              <img src="/path-to-avatar3.jpg" alt="Sarah Parker" class="profile-avatar">
              <div class="profile-info">
                <h4>Sarah Parker</h4>
                <p>Machine Learning Specialist</p>
              </div>
              <button class="follow-button">Follow</button>
            </div>
  
            <!-- Profile 4 -->
            <div class="profile">
              <img src="/path-to-avatar4.jpg" alt="David Brown" class="profile-avatar">
              <div class="profile-info">
                <h4>David Brown</h4>
                <p>Deep Learning Engineer</p>
              </div>
              <button class="follow-button">Follow</button>
            </div>
          </div>
          <button class="discover-more-button">Find More Profiles</button>
        </div>
  
        <!-- Nitro Subscription Section -->
        <div class="nitro-subscription">
          <h2>Get Nitro Subscription</h2>
          <p>Enhance your experience with Nitro:</p>
          <ul>
            <li>Better reach for auto posts/longer content</li>
            <li>Organize more events/pages</li>
            <li>Auto connect and connections recommendation engine feature</li>
            <li>Others</li>
          </ul>
          <button class="subscribe-button">Subscribe Now</button>
        </div>
      </div>
    </div>
  </main>
  
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Gemini:wght@400;700&display=swap');
  
    .dashboard {
      display: grid;
      grid-template-columns: 1fr 2fr 1fr;
      gap: 2%;
    }
  
    .card {
      background-color: #fff;
      padding: 2%;
      border-radius: 5px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      overflow: hidden;
    }
  
    .left-card, .right-card {
      padding: 2%;
    }
  
    .center-card {
      grid-column: 2;
      padding: 2%;
      background-color: #f5f5f5;
    }
  
    .post-creation {
      display: flex;
      flex-direction: column;
      border-bottom: 1px solid #ddd;
      padding-bottom: 1rem;
      margin-bottom: 1rem;
    }
  
    .post-creation textarea {
      width: 100%;
      padding: 0.5rem;
      border: 1px solid #ddd;
      border-radius: 5px;
      font-size: 1rem;
      resize: none;
    }
  
    .post-button {
      background-color: #00358b; /* Blue */
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 5px;
      cursor: pointer;
      margin-top: 0.5rem;
    }
  
    .post-button:hover {
      background-color: #ffeb3b;
      color: black;
    }
  
    .top-picks {
      margin-top: 1rem;
    }
  
    .top-picks h3 {
      margin: 0;
      font-size: 1.5rem;
      color: #333;
    }
  
    .feed-post {
      background-color: #fff;
      padding: 1rem;
      border-radius: 5px;
      margin-bottom: 1rem;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .post-header {
      display: flex;
      align-items: center;
      margin-bottom: 1rem;
    }
  
    .avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      margin-right: 0.75rem;
    }
  
    .user-info {
      display: flex;
      flex-direction: column;
    }
  
    .user-info h4 {
      margin: 0;
      font-size: 1rem;
    }
  
    .user-info p {
      margin: 0;
      color: #666;
      font-size: 0.875rem;
    }
  
    .post-content {
      margin-bottom: 1rem;
    }
  
    .post-actions {
      display: flex;
      gap: 1rem;
    }
  
    .post-actions button {
      background: none;
      border: none;
      color: #1e90ff;
      cursor: pointer;
    }
  
    .post-actions button:hover {
      text-decoration: underline;
    }
  
    .discover-articles {
      margin-top: 2rem;
    }
  
    .discover-articles ul {
      list-style: none;
      padding: 0;
    }
  
    .discover-articles li {
      margin-bottom: 0.5rem;
    }
  
    .discover-articles a {
      text-decoration: none;
      color: #00358b;
    }
  
    .discover-articles a:hover {
      text-decoration: underline;
    }
  
    .profile-suggestions {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
  
    .profile {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background-color: #fff;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    .profile-avatar {
      width: 50px;
      height: 50px;
      border-radius: 50%;
    }
  
    .profile-info {
      margin-left: 1rem;
    }
  
    .profile-info h4 {
      margin: 0;
      font-size: 1rem;
      color: #333;
    }
  
    .profile-info p {
      margin: 0;
      color: #666;
      font-size: 0.875rem;
    }
  
    .follow-button {
      background-color: #00358b; /* Blue */
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 5px;
      cursor: pointer;
    }
  
    .follow-button:hover {
      background-color: #ffeb3b;
      color: black;
    }
  
    .discover-more-button {
      background-color: #00358b; /* Blue */
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 5px;
      cursor: pointer;
      margin-top: 1rem;
    }
  
    .discover-more-button:hover {
      background-color: #ffeb3b;
      color: black;
    }
  
    .nitro-subscription {
      margin-top: 2rem;
    }
  
    .nitro-subscription ul {
      list-style: disc;
      margin-left: 1rem;
    }
  
    .nitro-subscription button {
      background-color: #00358b; /* Blue */
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 5px;
      cursor: pointer;
      margin-top: 1rem;
    }
  
    .nitro-subscription button:hover {
      background-color: #ffeb3b;
      color: black;
    }
  </style>
  