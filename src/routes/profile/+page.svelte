<script>
    import { onMount } from 'svelte';
  
    let summaryData = {
      general_summary: '',
      research_summaries: {}
    };
    let activeTab = 'general';
  
    async function fetchSummary() {
      try {
        const response = await fetch('http://127.0.0.1:5000/generate-summary');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        summaryData = data;
      } catch (error) {
        console.error('Error fetching summary data:', error);
      }
    }
  
    function switchTab(tab) {
      activeTab = tab;
      document.querySelectorAll('.tab-pane').forEach(pane => {
          pane.classList.remove('show', 'active');
      });
  
      document.querySelectorAll('.list-group-item').forEach(item => {
          item.classList.remove('active');
      });
  
      const tabElement = document.getElementById(tab);
      if (tabElement) {
          tabElement.classList.add('show', 'active');
      }
      const listItem = document.querySelector(`.list-group-item[onclick="switchTab('${tab}')"]`);
    if (listItem) {
      listItem.classList.add('active');
    }
  }

  onMount(() => {
      // Initialize the active tab
      switchTab('general');
  });
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif !important;
}
  /* Profile Page Styles */
  .profile-page {
      background-color: #f8f9fa;
      padding: 1% 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .profile-header {
      background-color: white;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      margin-bottom: 20px;
  }
  .background-image {
      width: 100%;
      height: 240px;
      object-fit: cover;
      opacity: 0.9;
  }
  .profile-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 20px;
     /* Adjust this value to control the overlap amount */
    z-index: 1;
}
  .profile-avatar {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      overflow: hidden;
      margin-right: 20px;
      top: -80px;
  }
  .profile-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }
  .profile-info h1 {
      font-size: 28px;
      font-weight: bold;
      margin-bottom: 10px;
  }
  .profile-info p {
      font-size: 16px;
      margin: 5px 0;
  }
  .button-group .btn {
      border-radius: 30px;
      padding: 5px 15px;
      font-weight: 500;
      font-size: 14px;
      margin-right: 5px;
      background-color: #000000f7;
      border: none;
      color: white;
      transition: transform 0.3s ease;
  }
  .button-group .btn:hover {
      background-color: #ef8534;
      transform: scale(1.05);
  }
  .associated-orgs h2 {
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 10px;
  }
  .tab-container, .card {
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      padding: 15px;
      margin-bottom: 20px;
      transition: transform 0.3s ease;
  }
  .tab-container:hover, .card:hover {
      transform: scale(1.05);
  }
  .list-group-item {
      cursor: pointer;
  }
  .dashboard {
      margin-top: 40px;
  }
  .metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin-bottom: 20px;
  }
  .metric-card {
      border: 1px solid #ccc;
      border-radius: 8px;
      padding: 15px;
      background-color: #fff;
  }
  .metric-value {
      font-size: 24px;
      font-weight: bold;
      margin: 10px 0;
  }
  .content-flex {
      display: flex;
      gap: 20px;
  }
  .chart-container {
      flex: 2;
      margin-bottom: 20px;
  }
  .recent-publications {
      flex: 1;
      background-color: #f9f9f9;
      padding: 20px;
      border-radius: 8px;
  }
  .publication {
      margin-bottom: 15px;
  }
  .publication h3 {
      margin-bottom: 5px;
  }
  .award-item {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 10px;
  width: 250px;
  margin-right: 20px;
}

.testimonials-section {
  padding: 10px;
}

.testimonial-item {
  background-color: #f1f1f1;
  padding: 15px;
  border-radius: 10px;
  display: flex;
  align-items: center;
}

.avatar-icon {
  font-size: 30px;
  margin-right: 15px;
}
</style>

<main class="profile-page">
  <!-- Profile Header -->
  <div class="profile-header">
      <img src="../src/lib/images/banner.png" alt="Background" class="background-image img-fluid rounded"/>
      <div class="profile-content">
          <div class="profile-avatar">
              <img src="../src/lib/images/avatar.png" alt="Profile Avatar" class="img-fluid"/>
          </div>
          <div class="profile-info">
              <h1>Dr. XYZ</h1>
              <p class="text-muted">Researcher in AI & Robotics</p>
              <p class="text-muted">Location: City, Country</p>
              <div class="button-group d-flex">
                  <button class="btn btn-primary">Follow</button>
                  <button class="btn btn-primary">Connect</button>
                  <button class="btn btn-primary">Send Co-auth Request</button>
                  
                  <!-- More Button with Dropdown -->
                  <div class="btn-group">
                      <button class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">More</button>
                      <ul class="dropdown-menu">
                          <li><a class="dropdown-item" href="#">Export to PDF</a></li>
                          <li><a class="dropdown-item" href="#">About this Profile</a></li>
                      </ul>
                  </div>
              </div>
          </div>
          <div class="associated-orgs">
              <h2>Associated Organizations</h2>
              <ul class="list-unstyled">
                  <li>Org 1</li>
                  <li>Org 2</li>
              </ul>
          </div>
      </div>
  </div>

  <!-- Summary and Statistics Section -->
  <div class="row mb-4">
      <div class="col-md-12">
          <div class="tab-container">
              <div class="summaries-heading">Field wise summaries</div>
              <div class="row">
                  <div class="col-md-3">
                      <div class="list-group">
                          <button class="list-group-item list-group-item-action active" on:click={() => switchTab('general')}>General</button>
                          <button class="list-group-item list-group-item-action" on:click={() => switchTab('nlp')}>NLP</button>
                          <button class="list-group-item list-group-item-action" on:click={() => switchTab('cv')}>CV</button>
                          <button class="list-group-item list-group-item-action" on:click={() => switchTab('robotics')}>Robotics</button>
                      </div>
                  </div>
                  <div class="col-md-9">
                      <div class="tab-content">
                          <div id="general" class="tab-pane show active">
                              General Statistics Content
                          </div>
                          <div id="nlp" class="tab-pane">
                              NLP Statistics Content
                          </div>
                          <div id="cv" class="tab-pane">
                              CV Statistics Content
                          </div>
                          <div id="robotics" class="tab-pane">
                              Robotics Statistics Content
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>

  <!-- Dashboard Section -->
  <div class="dashboard">
    <h1>Dashboard</h1>

    <div class="metrics-grid">
        <div class="metric-card">
            <h2>H-Index</h2>
            <p class="metric-value">{hIndex}</p>
            <p class="metric-change">+2 from last month</p>
        </div>
        <div class="metric-card">
            <h2>I-Index</h2>
            <p class="metric-value">{iIndex}</p>
            <p class="metric-change">+5 from last month</p>
        </div>
        <div class="metric-card">
            <h2>Published Papers</h2>
            <p class="metric-value">{papers}</p>
            <p class="metric-change">+3 new papers</p>
        </div>
        <div class="metric-card">
            <h2>Citations</h2>
            <p class="metric-value">{citations}</p>
            <p class="metric-change">+120 in the last 3 months</p>
        </div>
    </div>

    <div class="content-flex">
        <div class="chart-container">
            <h2>Citations per Year</h2>
            <Bar data={citationsData}/>
        </div>
        <div class="recent-publications">
            <h2>Recent Publications</h2>
            {#each recentPublications as publication}
                <div class="publication">
                    <h3>{publication.title}</h3>
                    <p class="text-muted">{publication.category}</p>
                </div>
            {/each}
        </div>
    </div>
  </div>
  <!-- Awards and Achievements Section -->
<div class="row mt-4">
  <div class="col-md-12">
    <div class="card">
      <div class="card-header">
        <h4>Awards and Achievements</h4>
      </div>
      <div class="card-body d-flex flex-wrap justify-content-start">
        <div class="award-item m-3">
          <p><strong>Award 1</strong></p>
          <p>Description of Award 1</p>
        </div>
        <div class="award-item m-3">
          <p><strong>Award 2</strong></p>
          <p>Description of Award 2</p>
        </div>
        <div class="award-item m-3">
          <p><strong>Award 3</strong></p>
          <p>Description of Award 3</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Testimonials Section -->
<div class="row mt-4">
  <div class="col-md-12">
    <div class="card">
      <div class="card-header">
        <h4>Testimonials and Endorsements</h4>
      </div>
      <div class="card-body">
        <div class="testimonials-section">
          <div class="testimonial-item d-flex mb-3">
            <span class="avatar-icon mr-3">👤</span>
            <div>
              <h5>Person 1</h5>
              <p>"This is a great testimonial for Dr. XYZ!"</p>
            </div>
          </div>
          <div class="testimonial-item d-flex mb-3">
            <span class="avatar-icon mr-3">👤</span>
            <div>
              <h5>Person 2</h5>
              <p>"Another amazing testimonial."</p>
            </div>
          </div>
          <div class="testimonial-item d-flex mb-3">
            <span class="avatar-icon mr-3">👤</span>
            <div>
              <h5>Person 3</h5>
              <p>"Dr. XYZ is highly recommended!"</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</main>
