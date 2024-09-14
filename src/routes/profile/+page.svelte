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
      fetchSummary();
      switchTab(activeTab);
    });
  </script>

<style>
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
      align-items: flex-start;
      padding: 20px;
  }

  .profile-avatar {
      position: relative;
      width: 150px;
      height: 150px;
      border-radius: 50%;
      overflow: hidden;
      margin-right: 20px;
  }

  .profile-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }

  .profile-info {
      flex: 1;
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

  .associated-orgs {
      margin-left: auto;
      max-width: 250px;
      padding-left: 20px;
  }

  .associated-orgs h2 {
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 10px;
  }

  .associated-orgs ul {
      list-style-type: none;
      padding: 0;
  }

  .associated-orgs li {
      margin-bottom: 5px;
      font-size: 16px;
  }

  .tab-container, .card {
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      padding: 15px;
      margin-bottom: 20px;
      transition: transform 0.3s ease; /* Added transition for animation */
  }

  /* Zoom effect for cards on hover */
  .tab-container:hover, .card:hover {
      transform: scale(1.05); /* Zoom-in effect */
  }

  .tab-container .summaries-heading,
  .card-title {
      text-align: center;
      font-size: 22px;
      font-weight: bold;
      margin-bottom: 20px;
  }

  .tab-content {
      padding: 15px;
  }

  .tab-pane {
      opacity: 0;
      transition: opacity 0.5s ease-in-out;
      position: absolute;
      width: 100%;
      top: 0;
      left: 0;
  }

  .tab-pane.show {
      opacity: 1;
      position: relative;
  }

  .list-group-item {
      cursor: pointer;
  }

  .btn-outline-primary {
      border-radius: 20px;
  }

  .btn-group .btn {
      border: 1px solid transparent;
      transition: all 0.3s ease;
  }

  .btn-group .btn-outline-primary {
      color: #f4f6f9;
      background-color: black;
      
  }

  .btn-group .btn-outline-primary:hover {
      background-color: #f37a43;
      color: white;
  }

  .award-item {
      flex: 1 1 200px;
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      padding: 15px;
      text-align: center;
      margin: 5px;
      transition: transform 0.3s ease; /* Added transition for animation */
  }

  /* Zoom effect for award items on hover */
  .award-item:hover {
      transform: scale(1.05);
  }

  .testimonials-section {
      display: flex;
      flex-direction: column;
      gap: 15px;
  }

  .testimonial-item {
      display: flex;
      align-items: center;
      gap: 15px;
      padding: 15px;
      border-radius: 8px;
      background-color: #ffffff;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease; /* Added transition for animation */
  }

  /* Zoom effect for testimonial items on hover */
  .testimonial-item:hover {
      transform: scale(1.05);
  }

  .testimonial-item .avatar-icon {
      font-size: 40px;
      color: #007bff;
  }

  .testimonial-item p {
      margin: 0;
  }

  .testimonial-item h5 {
      margin: 0;
      font-weight: 500;
  }

  @media (max-width: 768px) {
      .profile-content {
          flex-direction: column;
          align-items: center;
      }

      .profile-avatar {
          margin-bottom: 20px;
      }

      .associated-orgs {
          margin-left: 0;
          max-width: none;
          padding-left: 0;
          text-align: center;
      }

      .award-item {
          flex: 1 1 100%;
      }
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
                            <button class="list-group-item list-group-item-action {activeTab === 'general' ? 'active' : ''}" on:click={() => switchTab('general')}>General</button>
                            <button class="list-group-item list-group-item-action {activeTab === 'nlp' ? 'active' : ''}" on:click={() => switchTab('nlp')}>NLP</button>
                            <button class="list-group-item list-group-item-action {activeTab === 'cv' ? 'active' : ''}" on:click={() => switchTab('cv')}>CV</button>
                            <button class="list-group-item list-group-item-action {activeTab === 'robotics' ? 'active' : ''}" on:click={() => switchTab('robotics')}>Robotics</button>
                        </div>
                    </div>
                    <div class="col-md-9">
                        <div class="tab-content">
                            <div id="general" class="tab-pane {activeTab === 'general' ? 'show active' : ''}">
                                {#if summaryData.general_summary}
                                  <p>{summaryData.general_summary}</p>
                                {:else}
                                  <p>Loading...</p>
                                {/if}
                            </div>
                            <div id="nlp" class="tab-pane {activeTab === 'nlp' ? 'show active' : ''}">
                                {#if summaryData.research_summaries['NLP']}
                                  <p>{summaryData.research_summaries['NLP']}</p>
                                {:else}
                                  <p>Loading...</p>
                                {/if}
                            </div>
                            <div id="cv" class="tab-pane {activeTab === 'cv' ? 'show active' : ''}">
                                {#if summaryData.research_summaries['CV']}
                                  <p>{summaryData.research_summaries['CV']}</p>
                                {:else}
                                  <p>Loading...</p>
                                {/if}
                            </div>
                            <div id="robotics" class="tab-pane {activeTab === 'robotics' ? 'show active' : ''}">
                                {#if summaryData.research_summaries['Robotics']}
                                  <p>{summaryData.research_summaries['Robotics']}</p>
                                {:else}
                                  <p>Loading...</p>
                                {/if}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
  

  <!-- Awards and Achievements Section -->
  <div class="row">
      <div class="col-md-12">
          <div class="card">
              <div class="card-title">Awards and Achievements</div>
              <div class="d-flex flex-wrap justify-content-start">
                  <div class="award-item">
                      <p><strong>Award 1</strong></p>
                      <p>Description of Award 1</p>
                  </div>
                  <div class="award-item">
                      <p><strong>Award 2</strong></p>
                      <p>Description of Award 2</p>
                  </div>
                  <div class="award-item">
                      <p><strong>Award 3</strong></p>
                      <p>Description of Award 3</p>
                  </div>
              </div>
          </div>
      </div>
  </div>

  <!-- Testimonials Section -->
  <div class="row">
      <div class="col-md-12">
          <div class="card">
              <div class="card-title">Testimonials and Endorsements</div>
              <div class="testimonials-section">
                  <div class="testimonial-item">
                      <span class="avatar-icon">👤</span>
                      <div>
                          <h5>Person 1</h5>
                          <p>"This is a great testimonial for Dr. XYZ!"</p>
                      </div>
                  </div>
                  <div class="testimonial-item">
                      <span class="avatar-icon">👤</span>
                      <div>
                          <h5>Person 2</h5>
                          <p>"Another amazing testimonial."</p>
                      </div>
                  </div>
                  <div class="testimonial-item">
                      <span class="avatar-icon">👤</span>
                      <div>
                          <h5>Person 3</h5>
                          <p>"Dr. XYZ is highly recommended!"</p>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</main>