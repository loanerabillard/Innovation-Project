<template>
  <div class="main">
    <Header></Header>
    <div class="separator"></div>
    <div class="content">
      <h1 class="main-title">Discover Your Perfect Investment Package</h1>
      <p class="main-paragraph">Select from our carefully crafted packages designed to maximize your gains while minimizing risks. Whether you seek high stability or high potential gains, we have the perfect package for you.</p>
      <div class="packages">
        <CardPackage
          v-for="pkg in packages"
          :key="pkg.id"
          :name="pkg.name"
          :description="pkg.description"
          :bgColor="pkg.color"
          :avgGain2023="pkg.avgGain2023"
          :avgGain2024="pkg.avgGain2024"
          :extraInfo="pkg.extraInfo"
        />
      </div>
      <div class="simulation">
        <h2 class="simulation-title">Investment Simulation</h2>
        <p class="simulation-text">Simulate your investment with the last week's package performance.</p>
      </div>
      <OldPageContent :matches="matches" :showButtons="false" />
      <div class="simulation">
        <div class="simulation-input">
          <label for="amount">Simulation Amount:</label>
          <div class="input-container">
            <input type="number" v-model="amount" id="amount" />
            <span class="euro-sign">€</span>
          </div>
          <button @click="simulateInvestment">Simulate</button>
        </div>
        <div class="simulation-results" v-if="simulationResults.length">
          <h3>Simulation Results:</h3>
          <div class="result-packages">
            <CardResult
              v-for="result in simulationResults"
              :key="result.packageName"
              :name="result.packageName"
              :description="getDescription(result.packageName)"
              :bgColor="getColor(result.packageName)"
              :gainEuro="result.gain"
              :gainPercent="((result.gain / amount) * 100).toFixed(2)"
              :extraInfo="getExtraInfo(result.packageName)"
            />
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import CardPackage from "../components/CardPackage.vue";
import OldPageContent from "../components/OldPageContent.vue"; // Import the new component
import CardResult from "../components/CardResult.vue"; // Import the CardResult component

export default {
  name: "ChoosePackage",
  components: {
    Header,
    Footer,
    CardPackage,
    OldPageContent,
    CardResult // Register the new component
  },
  data() {
    return {
      packages: [
        {
          id: 1,
          name: "Short Package",
          description: "High Stability",
          color: "#3498db", // Keep color as blue
          avgGain2023: "23%",
          avgGain2024: "25%",
          extraInfo: "+98% of weeks are winning weeks"
        },
        {
          id: 2,
          name: "Slice Package",
          description: "Good Gain and Stability", // Changed description
          color: "#f1c40f", // Changed color to yellow
          avgGain2023: "19%",
          avgGain2024: "21%",
          extraInfo: "+29% in 2024"
        },
        {
          id: 3,
          name: "Ace Package",
          description: "High Potential Gain",
          color: "#e67e22", // Changed color to orange
          avgGain2023: "17%",
          avgGain2024: "20%",
          extraInfo: "+400% for the best weeks"
        }
      ],
      amount: 0,
      matches: [], // This should be populated with matches data
      simulationResults: []
    };
  },
  methods: {
    async fetchMatches(numMatches) {
      const cacheKey = `matches_${numMatches}`;
      
      try {
        const response = await fetch(
          `${process.env.VUE_APP_BACKEND_URL}/get_matches?num_matches=${numMatches}`
        );

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const matches = await response.json();
        this.matches = this.processMatches(matches);
      } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
      }
    },
    processMatches(matches) {
      return matches.map(match => {
        if (match.player_1_logo == null) {
          match.player_1_logo = "/no_photo.jpeg";
        }
        if (match.player_2_logo == null) {
          match.player_2_logo = "/no_photo.jpeg";
        }

        // Ensure winner is always player_1
        if (match.meilleur_joueur === 2) {
          [match.player_1, match.player_2] = [match.player_2, match.player_1];
          [match.player_1_logo, match.player_2_logo] = [
            match.player_2_logo,
            match.player_1_logo
          ];
          [match.win_percentage_player_1, match.win_percentage_player_2] = [
            match.win_percentage_player_2,
            match.win_percentage_player_1
          ];
          [match.odd_player_1, match.odd_player_2] = [
            match.odd_player_2,
            match.odd_player_1
          ];
          match.meilleur_joueur = 1;
        }

        match.winner = match.meilleur_joueur === 1 ? "player_1" : "player_2";
        match.repartition = match.repartition.map(rep =>
          parseFloat(rep).toFixed(1)
        ); // Round to 1 decimal
        match.risk_level = match.meilleur_ratio.toFixed(2);
        match.max_gain = this.computeMaxGain(match);
        return match;
      });
    },
    
    computeMaxGain(match) {
      let max_gain;
      if (match.meilleur_joueur === 1) {
        max_gain = match.odd_player_1;
      } else {
        max_gain = match.odd_player_2;
      }
      return max_gain.toFixed(2); // Max gain formula
    },
    calculateAverageGain(matches, amount, packageName) {
      let totalGain = 0;
      let repartitionIndex;
      if (packageName === "ace") {
        repartitionIndex = 0;
      } else if (packageName === "slice") {
        repartitionIndex = 1;
      } else if (packageName === "short") {
        repartitionIndex = 2;
      }

      matches.forEach(match => {
        // console.log(`Match: ${JSON.stringify(match)}`);
        const repartitionValue = parseFloat(match.repartition[repartitionIndex]);
        const maxGainValue = parseFloat(match.max_gain);
        const riskLevelValue = parseFloat(match.risk_level);
        const calculatedGain = amount * (repartitionValue / 100) * maxGainValue * riskLevelValue;

        // console.log(`Amount: ${amount}`);
        // console.log(`Repartition (${packageName}): ${repartitionValue}`);
        // console.log(`Max Gain: ${maxGainValue}`);
        // console.log(`Risk Level: ${riskLevelValue}`);
        // console.log(`Calculated Gain: ${calculatedGain}`);

        if (!isNaN(calculatedGain)) {
          totalGain += calculatedGain;
        }
      });
      return totalGain;
    },
    simulateInvestment() {
      const packages = ["Short", "Slice", "Ace"];
      this.simulationResults = packages.map(packageName => {
        const gain = this.calculateAverageGain(this.matches, this.amount, packageName);
        console.log(`Package: ${packageName}, Gain: ${gain}`);
        return { packageName, gain };
      });
      // console.log("Simulation Results:", this.simulationResults);
    },
    getDescription(packageName) {
      const pkg = this.packages.find(p => p.name === packageName);
      return pkg ? pkg.description : "";
    },
    getColor(packageName) {
      const pkg = this.packages.find(p => p.name === packageName);
      return pkg ? pkg.color : "#ffffff";
    },
    getExtraInfo(packageName) {
      const pkg = this.packages.find(p => p.name === packageName);
      return pkg ? pkg.extraInfo : "";
    }
  },
  created() {
    // console.log("Choose Package");
    this.fetchMatches(10); // Fetch matches data
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
  font-family: 'Roboto', sans-serif;
}

.main {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.separator {
  background-color: #fbfaf9;
  height: 11vh;
}

.content {
  flex: 1;
  text-align: center;
  padding: 20px;
}

.main-title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 36px;
  font-weight: bold;
  color: #2c3e50;
}

.main-paragraph {
  text-align: center;
  margin-bottom: 40px;
  font-size: 18px;
  color: #34495e;
}

.title {
  text-align: left;
  margin-bottom: 20px;
  font-size: 30px;
  font-weight: bold;
  color: #2c3e50;
}

.explanation {
  text-align: left;
  margin: 20px 0;
  font-size: 16px;
  color: #333;
  margin-bottom: 40px;
  max-width: 50%;
}

.packages {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-top: 20px;
  margin: 100px;
}

.simulation {
  text-align: center;
  margin-top: 40px;
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
}

.simulation-title {
  font-size: 32px;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 20px;
}

.simulation-text {
  font-size: 20px;
  margin-bottom: 20px;
}

.simulation-input {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.simulation-input label {
  margin-right: 10px;
  font-size: 18px;
}

.simulation-input .input-container {
  position: relative;
  display: inline-block;
}

.simulation-input input {
  padding: 10px;
  font-size: 18px;
  width: 200px;
  border: 2px solid #27ae60; /* Highlight the input box */
  border-radius: 5px;
}

.simulation-input .euro-sign {
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 18px;
  color: #27ae60;
}

.simulation-input button {
  margin-left: 20px;
  padding: 10px 20px;
  font-size: 18px;
  background-color: #27ae60; /* Green color for the button */
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.simulation-input button:hover {
  background-color: #2ecc71;
}

.simulation-results {
  margin-top: 20px;
}

.simulation-results h3 {
  font-size: 24px;
  color: #2c3e50;
}

.result-packages {
  display: flex;
  justify-content: space-around;
}

.result-package {
  width: 23%; /* Dynamic width */
  display: flex;
  flex-direction: column;
  border-radius: 25px;
  margin-bottom: 20px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  border: 10px solid;
}

.result-package.short {
  background-color: #3498db; /* Blue for Short Package */
}

.result-package.slice {
  background-color: #f1c40f; /* Yellow for Slice Package */
}

.result-package.ace {
  background-color: #e67e22; /* Orange for Ace Package */
}

.result-package .card-header {
  color: #fff;
  text-align: center;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.result-package .package-name {
  font-size: 36px; /* Increased font size */
  font-weight: bold;
  margin-bottom: 10px; /* Increased margin for space */
}

.result-package .package-description {
  font-size: 28px; /* Increased font size */
  font-weight: 500;
  margin-bottom: 5px; /* Reduced margin for space */
}

.result-package .card-content {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #fff;
}

.result-package .gain-info {
  font-size: 60px; /* Large font size for percentage */
  font-weight: bold;
  display: flex;
  align-items: center;
}

.result-package .percentage,
.result-package .euro-gain {
  margin-right: 10px;
}

.result-package .arrow {
  width: 100px; /* Increased size of the stonks image */
  height: 100px;
}

.result-package .extra-info {
  font-size: 28px; /* Slightly smaller font size */
  margin-top: 15px; /* Increased margin for space */
  font-weight: bold; /* Made the number bold */
}

.result-package .card-footer {
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: inherit; /* Fix the background color */
}

.result-package .invest-button {
  font-size: 24px; /* Big font size for the button */
  font-weight: bold;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  color: #fff;
}
</style>
