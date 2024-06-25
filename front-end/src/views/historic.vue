<template>
  <div class="home-container">
    <Header></Header>
    <div class="separator"></div>
    <div class="content-container">
      <div class="betting-container">
        <h1>My Packages</h1>

        <!-- Loop through each package -->
        <div
          v-for="(pkg, index) in packages"
          :key="index"
          class="package-card"
          :class="pkg.Package.toLowerCase() + '-row'"
        >
          <div class="package-header">
            <div class="package-name">{{ pkg.Package }} Package - {{ formatDate(pkg.Date) }}</div>
          </div>
          <div class="package-details">
            <div class="column">
              <div class="detail">
                <i class="emoji">💵</i>
                <span class="info">Amount Invested: {{ formatNumber(pkg.Amount) }} €</span>
              </div>
              <div class="detail">
                <i class="emoji">🎾</i>
                <span class="info">Matches:  {{ pkg.Num_matches }}</span>
              </div>
            </div>
            <div class="column gain-column">
              <div class="detail gain">
                <i class="emoji">📈 </i>
                <span class="info">Gain:  +{{ formatNumber(pkg.Gain) }} €</span>
              </div>
            </div>
          </div>
        </div>
        <div class="balance-container">
          <h2>Total Balance: {{ totalBalance }} €</h2>
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
          Package: "Ace",
          Date: "2024-06-25",
          Amount: 100,
          Num_matches: 10,
          Gain: 300
        },
        {
          Package: "Short",
          Date: "2024-06-24",
          Amount: 50,
          Num_matches: 8,
          Gain: 180
        },
        {
          Package: "Slice",
          Date: "2024-06-23",
          Amount: 120,
          Num_matches: 12,
          Gain: 288
        },
        {
          Package: "Ace",
          Date: "2024-06-22",
          Amount: 80,
          Num_matches: 7,
          Gain: 240
        },
        {
          Package: "Short",
          Date: "2024-06-21",
          Amount: 150,
          Num_matches: 9,
          Gain: 600
        }
      ]
    };
  },
  methods: {
    formatDate(date) {
      const options = { year: "numeric", month: "2-digit", day: "2-digit" };
      return new Date(date).toLocaleDateString("en-GB", options);
    },
    formatNumber(value) {
      console.log(value)
      return value.toLocaleString("fr-FR");
    }
  },
  computed: {
    totalBalance() {
      const totalGain = this.packages.reduce((acc, pkg) => acc + pkg.Gain, 0);
      const totalInvestment = this.packages.reduce(
        (acc, pkg) => acc + pkg.Amount,
        0
      );
      return this.formatNumber(totalGain - totalInvestment);
    }
  }
};
</script>
  
  <style scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css");

.emoji {
  font-size: 30px;
}

.info {
  font-weight: bold;
  font-size: 22px;
}

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
  width: 70%;
  margin-left: auto;
  margin-right: auto;
}

.package-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.package-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.package-name {
  font-family: Arial, sans-serif;
  font-size: 24px;
  font-weight: bold;
}

.package-details {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.column {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.detail {
  display: flex;
  align-items: center;
  font-size: 18px;
}

.detail i {
  margin-right: 10px;
  color: #555;
}

.gain-column {
  display: flex;
  flex-direction: column;
  align-items: flex-end; /* Align to the right */
  justify-content: flex-start;
  margin-top: 1%; /* Adjust this percentage to move the Gain value up or down */
}

.gain {
  font-size: 25px; /* Made the Gain non-bold and 30px */
  color: #0c8a41;
}

.ace-row {
  background-color: rgba(241, 196, 15, 0.2);
  border-left: 5px solid #f1c40f;
}

.slice-row {
  background-color: rgba(230, 126, 34, 0.2);
  border-left: 5px solid #e67e22;
}

.short-row {
  background-color: rgba(52, 152, 219, 0.2);
  border-left: 5px solid #3498db;
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
  display: flex;
  flex-direction: column;
  align-items: center; /* Center the package boxes */
}

.balance-container {
  width: 100%;
  padding: 20px;
  background-color: #ecf0f1;
  text-align: center;
  font-size: 28px;
  color: #2c3e50;
  margin-top: 20px;
  border-radius: 10px;
}
</style>
  