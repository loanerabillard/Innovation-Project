<template>
    <div class="home-container">
      <Header></Header>
      <div class="separator"></div>
      <div class="content-container">
        <div class="betting-container">
          <h1>My Packages</h1>
          
          <!-- Loop through each package -->
          <div v-for="(pkg, index) in packages" :key="index" class="package-card" :class="pkg.Package.toLowerCase() + '-row'">
            <div class="package-header">
              <div class="package-name">{{ pkg.Package }}</div>
            </div>
            <div class="package-details">
              <div class="detail">
                <i class="fas fa-calendar-alt"></i>
                <span>Date: {{ pkg.Date }}</span>
              </div>
              <div class="detail">
                <i class="fas fa-euro-sign"></i>
                <span>Amount: €{{ pkg.Amount }}</span>
              </div>
              <div class="detail">
                <i class="fas fa-futbol"></i>
                <span>Matches: {{ pkg.Num_matches }}</span>
              </div>
              <div class="detail gain">
                <i class="fas fa-chart-line"></i>
                <span>Gain: €{{ pkg.Gain }}</span>
              </div>
            </div>
          </div>
          
        </div>
        <Footer></Footer>
      </div>
    </div>
  </template>
  
  <script>
  import Header from "../components/Header.vue";
  import Footer from "../components/Footer.vue";
  
  export default {
    components: {
      Header,
      Footer
    },
    data() {
      return {
        packages: [
          {
            "Package": "Ace",
            "Date": "2024-06-25",
            "Amount": 100,
            "Num_matches": 10,
            "Gain": 30000
          },
          {
            "Package": "Short",
            "Date": "2024-06-24",
            "Amount": 50,
            "Num_matches": 8,
            "Gain": 15000
          },
          {
            "Package": "Slice",
            "Date": "2024-06-23",
            "Amount": 120,
            "Num_matches": 12,
            "Gain": 28800
          },
          {
            "Package": "Ace",
            "Date": "2024-06-22",
            "Amount": 80,
            "Num_matches": 7,
            "Gain": 24000
          },
          {
            "Package": "Short",
            "Date": "2024-06-21",
            "Amount": 150,
            "Num_matches": 9,
            "Gain": 60000
          }
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
  
  .package-card {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
  }
  
  .package-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  
  .package-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 15px;
  }
  
  .package-name {
    font-family: Arial, sans-serif;
    font-size: 24px;
    font-weight: bold;
  }
  
  .package-details {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  
  .detail {
    display: flex;
    align-items: center;
    font-size: 18px;
  }
  
  .detail i {
    margin-right: 8px;
    color: #555;
  }
  
  .gain {
    font-weight: bold;
    color: #2ecc71;
  }
  
  .ace-row {
    background-color: rgba(241, 196, 15, 0.2);
  }
  
  .slice-row {
    background-color: rgba(230, 126, 34, 0.2);
  }
  
  .short-row {
    background-color: rgba(52, 152, 219, 0.2);
  }
  
  h1 {
    font-family: Arial, sans-serif;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
    margin-top: 20px; /* Add top margin to create space from the header */
  }
  
  .separator {
    height: 2px;
    background-color: #ddd;
    margin: 20px 0;
  }
  
  body,
  html {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: Arial, sans-serif;
  }
  
  .home-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  .content-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    width: 90%;
    margin: 0 auto;
  }
  
  .betting-container {
    flex: 1;
    background-color: white;
    padding: 20px;
    margin-top: 20px;
  }
  </style>
  