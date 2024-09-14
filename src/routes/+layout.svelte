<script>
	let showMenu = false;
	let showFilters = false;
	let authorName = '';
	let hIndex = 0;
	let iIndex = 0;
	let year = 0;
	let limit = 0;
  
	function toggleMenu() {
	  showMenu = !showMenu;
	}
  
	function toggleFilters() {
	  showFilters = !showFilters;
	}
  
	async function fetchAuthorDetails() {
	  const response = await fetch(`http://127.0.0.1:5173/scrape?author=${authorName}&h_index=${hIndex}&i10_index=${iIndex}&year=${year}&limit=${limit}`);
	  const data = await response.json();
	  console.log(data);
	  // Display the fetched data here
	}
  
	import '../app.css';
	const currentYear = new Date().getFullYear();
	let years = [];
	for (let year = 2024; year >= 2003; year--) {
	  years.push(year);
	}
  </script>
  
  <!-- Menu Toggle Button -->
  <!-- Menu Toggle Button 
  <button class="menu-toggle" on:click={toggleMenu} class:active={showMenu}>
	<span class="material-icons">menu</span>
  </button>-->
  
  <header>
	<nav class="top-nav">
	  <!-- Site Name -->
	  <div class="site-name" >
		<a href="/" class="site-link">
		  <div class="site-logo-container">
			<img src="./src/lib/images/logo.png" alt="Logo" class="site-logo" />
		  </div>
		  <h1>Academia Assistant</h1>
		</a>
	  </div>
  
	  <!-- Centered Search Field with Filter Icon -->
	  <div class="search-wrapper">
		<input type="text" placeholder="Search..." class="search-field" bind:value={authorName} />
		<button class="filter-icon" on:click={toggleFilters}>
		  <span class="material-icons">filter_list</span>
		</button>
		<!-- Generate and Upload Buttons -->
		<button class="generate-button" on:click={fetchAuthorDetails}>
		  <span class="material-icons">add_circle</span>
		  <span class="button-text">Generate</span>
		</button>
		<button class="upload-button">
		  <span class="material-icons">upload</span>
		  <span class="button-text">Upload</span>
		</button>
		{#if showFilters}
		<div class="filter-popup show">
		  <div class="filter-section">
			<h3>Filter Options</h3>
			<div id="filter-option">
			  <div class="filter-group">
				<label for="year-select">Year:</label>
				<select id="year-select" bind:value={year}>
				  {#each years as year}
					<option value={year}>{year}</option>
				  {/each}
				</select>
			  </div>
			  <div class="filter-option">
				<label for="h-index">H-index:</label>
				<input type="number" id="h-index" name="h-index" min="0" step="1" bind:value={hIndex}>
			  </div>
			  <div class="filter-option">
				<label for="i-index">I-index:</label>
				<input type="number" id="i-index" name="i-index" min="0" step="1" bind:value={iIndex}>
			  </div>
			  <div class="filter-option">
				<label for="limit">Limit:</label>
				<input type="number" id="limit" name="limit" min="0" step="1" bind:value={limit}>
			  </div>
			</div>
			<div class="filter-buttons">
			  <button class="apply-button" on:click={() => { fetchAuthorDetails(); showFilters = false; }}>Apply Filters</button>
			  <button class="reset-button" on:click={() => showFilters = false}>Clear Filters</button>
			</div>
		  </div>
		</div>
		{/if}
  
	  </div>

		<!-- Right Side Buttons -->
		<div class="nav-buttons">
			<div class="profile-menu">
				<!-- Profile Button with Profile Picture -->
				<button class="profile-button">
					<img src="./src/lib/images/avatar.png" alt="Profile" class="profile-pic" />
				</button>
				<div class="profile-dropdown">
					<a href="/profile">View Profile</a>
		
					<!-- Manage Option with Submenu -->
					<div class="manage-menu">
						<a href="/manage" class="manage-link">Manage</a>
						<div class="manage-submenu">
							<a href="/manage/pages">Manage Pages</a>
							<a href="/manage/groups">Manage Groups</a>
							<a href="/manage/events">Manage Events</a>
						</div>
					</div>
		
					<a href="/settings">Settings</a>
					<div class="dropdown-divider"></div>
					<a href="/logout" class="dropdown-item">Logout</a>
				</div>
			</div>
			<button class="notifications-button">
				<span class="material-icons">notifications</span>
			</button>
		</div>
	</nav>	
</header>

<!--<aside class:show={showMenu} class="side-menu">
	<div class="user-avatar">
		<img src="./src/lib/images/avatar.png" alt="User Avatar" />
	</div>
	<button>Find Co-Author</button>
	<button>Manage Pages</button>
	<button>Manage Groups</button>
	<button>Manage Events</button>
	<button>Manage Interests</button>
	<button>Export Options</button>
</aside>-->

<main>
	<slot></slot>
</main>

<style>
	/* Color Theme: White, Blue, Yellow, Black */
	header {
    background: #000000;
    color: #fff;
    padding: 0.5rem 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 10px; /* Adjust the top position to include the margin */
    width: 100%;
    z-index: 1000;
    border-radius: 30px;
    max-width: 1650px; /* Limit the width of the header */
    margin: 10px auto 0 auto; /* Set the margin on top and auto on sides */
}
	.top-nav {
		margin-left: 50px;
		margin-right: 50px;
		display: flex;
		align-items: center;
		width: 100%;
		justify-content: space-between;
		transition: margin-left 0.3s ease;
	}

	.menu-toggle {
		background: none;
		color: #fff;
		border: none;
		font-size: 1.25rem;
		cursor: pointer;
		position: fixed;
		top: 1rem;
		left: 1rem;
		z-index: 1100;
		padding: 0.5rem;
		border-radius: 5px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
	}

	/*.site-name {
		text-align: left;
		flex: 1;
		display: flex;
		align-items: center;
		padding-left: 3rem;
		font-family: 'Poppins', sans-serif;
	}   uncomment to put search to right*/ 
	.site-name.with-menu {
		margin-left: 200px; /* Shifts the site name when the menu is open */
	}

	.site-link {
		text-decoration: none;
		color: #fff;
		display: flex;
  align-items: center;
  text-decoration: none;
	}

	.site-link h1 {
		font-size: 1.5rem;
		margin: 0;
		transition: transform 0.3s ease;
	}

	.site-link:hover h1 {
		transform: scale(1.05);
	}

	.search-wrapper {
		display: flex;
		align-items: center;
		background-color: transparent;
		border-radius: 5px;
		padding: 0.1rem;
		flex: 1;
		max-width: 400px;
		margin: 0 1rem; /* Keep the existing margin */
		position: relative;
		transform: translateX(30px); /* Adjust the value as needed */
	}

	.search-field {
		border: 1px solid #ddd;
		padding: 0.2rem 0.5rem;
		border-radius: 12px;
		flex: 1;
		font-size: 1.25rem;
	}

	.filter-icon {
		background: none;
		border: none;
		cursor: pointer;
		font-size: 1.5rem;
		color: #ffffff;
		padding: 0.5rem;
		margin-left: 0.5rem;
	}
	/* Apply fonts */
.filter-popup {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: #ffffff;
  color: #333;
  box-shadow: 0 4.5px 6.5px rgba(0, 0, 0, 0.278);
  border-radius: 0.5rem;
  padding: 1rem;
  width: 250px;
  z-index: 1050;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
  font-family: 'Poppins', sans-serif; /* Use Poppins for filter popup text */
}

.filter-popup.show {
  opacity: 1;
  visibility: visible;
}

.filter-section {
  margin-bottom: 1rem;
  
}
h3 {
    font-family: 'Poppins', sans-serif;
  }

.filter-option {
  margin-bottom: 1rem;
  font-family: 'Poppins', sans-serif;
}

.filter-option label {
  display: block;
  margin-bottom: 0.5rem;
  font-family: 'Poppins', sans-serif; /* Use Playfair Display for labels */
}

.filter-option select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  font-family: 'Poppins', sans-serif; /* Ensure select uses Poppins */
}

.filter-buttons {
  display: flex;
  justify-content: space-between;
}

.apply-button, .reset-button {
    background-color: #000000;
    color: #fff;
    border: none;
    padding: 0.5rem 1rem; /* Reduced padding for smaller size */
    border-radius: 5px;
    cursor: pointer;
    font-size: 0.75rem; /* Reduced font size */
    font-family: 'Poppins', sans-serif;
    transition: background-color 0.3s ease, transform 0.3s ease;

}

.apply-button:hover, .reset-button:hover {
    background-color: #0000008f;
}

.apply-button:active, .reset-button:active {
    transform: scale(0.98);
}



	.generate-button, .upload-button {
		background-color: transparent;
		color: #fff;
		border: none;
		cursor: pointer;
		padding: 0.5rem;
		display: flex;
		align-items: center;

		justify-content: center;
	}

	.generate-button {
		color: #ffffff;
	}

	.upload-button {
		color: #ffffff;
	}

	.generate-button .material-icons, .upload-button .material-icons {
		font-size: 1.5rem;
	}

	.button-text {
		display: none;
		margin-left: 0.5rem;
		font-family: 'Poppins', sans-serif;
	}

	.generate-button:hover .button-text, .upload-button:hover .button-text {
		display: inline;
	}

	.generate-button:hover {
		background-color: rgba(255, 255, 255, 0.1);
	}

	.upload-button:hover {
		background-color: rgba(255, 255, 255, 0.1);
	}

	.profile-menu {
		position: relative;
		display: flex;
		align-items: center;
		margin-left: 1rem;
	}

	.profile-button {
		background: none;
		border: none;
		color: #fff;
		cursor: pointer;
		transform: translateX(10px); /* Adjust the value as needed */
	}

	.profile-pic {
		border-radius: 50%;
		width: 40px;
		height: 40px;
		object-fit: cover;
	}

	.profile-dropdown {
    position: absolute;
    top: 100%;
    right: 0;
    background: linear-gradient(145deg, #ffffff, #f9f9f9);
    color: #333;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2), 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 0.75rem;
    padding: 0.5rem 0;
    width: 160px;
    z-index: 1050;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease, transform 0.3s ease;
    font-family: 'Poppins', sans-serif;
    transform: translateY(10px);
}

.profile-menu:hover .profile-dropdown {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.profile-dropdown a {
    color: #333;
    text-decoration: none;
    padding: 0.5rem 1rem;
    display: block;
    transition: background-color 0.2s ease, color 0.2s ease;
    border-bottom: 1px solid #eee;
}

.profile-dropdown a:hover {
    background-color: #f0f0f0;
    color: #007bff;
}

.profile-dropdown a:last-child {
    border-bottom: none;
}

.dropdown-divider {
    border-top: 1.5px solid #ddd;
    margin: 0.5rem 0;
}

.manage-menu {
    position: relative;
}

.manage-submenu {
    position: absolute;
    top: 0;
    right: 100%;
    background: linear-gradient(145deg, #ffffff, #f9f9f9);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2), 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 0.75rem;
    padding: 1rem;
    display: none;
    z-index: 1060;
    width: 270px;
    border: 2px solid #ddd;
    transition: opacity 0.3s ease, transform 0.3s ease;
    opacity: 0;
    transform: translateX(-10px);
}

.manage-link:hover + .manage-submenu,
.manage-submenu:hover {
    display: block;
    opacity: 1;
    transform: translateX(0);
}

.manage-submenu a {
    display: block;
    color: #333;
    text-decoration: none;
    padding: 0.5rem 1rem;
    transition: background-color 0.2s ease, color 0.2s ease;
    border-bottom: 1px solid #eee;
}

.manage-submenu a:hover {
    background-color: #f8f9fa;
    color: #1A4870;
}

.manage-submenu a:last-child {
    border-bottom: none;
}

	.nav-buttons {
		display: flex;
		align-items: center;
		gap: 0.5 rem; /* Space between items */
	}

	.notifications-button {
		background: none;
		border: none;
		color: #fff;
		font-size: 1.5rem;
		cursor: pointer;
		margin-left: 1rem;
	}

	aside.side-menu {
		position: fixed;
		top: 0;
		left: 0;
		height: 100%;
		width: 250px;
		background-color: #ffffff; 
		padding: 1.5rem 1rem;
		transform: translateX(-100%);
		transition: transform 0.3s ease, box-shadow 0.3s ease;
		z-index: 1001;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
		font-family: 'Poppins', sans-serif;
	}

	aside.side-menu.show {
		transform: translateX(0);
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
	}
	.menu-toggle.active {
		color: #000000; /* Change icon color to blue when menu is open */
	}

	.user-avatar {
		text-align: center;
		margin-bottom: 2rem;
	}

	.user-avatar img {
		border-radius: 50%;
		width: 100px;
		height: 100px;
		object-fit: cover;
		border: 3px solid #fff; /* White border for contrast */
	}

	.side-menu button {
		background-color: #f4f4f4; /* Light grey button background */
		color: #000000; /* Blue text */
		border: none;
		padding: 0.75rem 1rem;
		border-radius: 10px;
		margin-bottom: 1rem;
		cursor: pointer;
		width: 100%;
		font-size: 1rem;
		font-weight: 600;
		text-align: left;
		display: flex;
		align-items: center;
		transition: background-color 0.3s ease, transform 0.3s ease;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.side-menu button:hover {
		background-color: #000000; /* Button changes to blue on hover */
		color: #ffffff; /* White text on hover */
		transform: scale(1.05); /* Slight grow effect on hover */
	}

	.side-menu button:active {
		transform: scale(1);
	}

	main {
		margin-left: 50px;
		padding: 1rem;
		background-color: #fff;
		color: #333;
		transition: margin-left 0.3s ease;
	}
	.site-logo-container {
  margin-right: 10px; /* Adjust space between logo and text */
  
}

.site-logo {
  width: 60px; /* Adjust size as needed */
  height: auto; /* Keeps the aspect ratio */
  border-radius: 50%;
  object-fit: cover;
}

	
</style>
