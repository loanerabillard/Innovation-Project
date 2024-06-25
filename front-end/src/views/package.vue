<template>
  <div class="home-container">
    <Header></Header>
    <div class="separator"></div>
    <div class="content-container">
      <div class="betting-container">
        <h1 class="logo">
          Package -
          <span
            :class="`${packageName.toLowerCase()}-text`"
          >{{ packageName.charAt(0).toUpperCase() + packageName.slice(1) }}</span>
        </h1>
        <table class="matches-table">
          <thead>
            <tr>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
              <th v-if="shouldShowPackage('ace')" class="ace header-cell">
                <div class="package-name">Ace Package</div>
                <div class="desc">High Potential Gain</div>
              </th>
              <th v-if="shouldShowPackage('slice')" class="slice header-cell">
                <div class="package-name">Slice Package</div>
                <div class="desc">Balanced Gain and Stability</div>
              </th>
              <th v-if="shouldShowPackage('short')" class="short header-cell">
                <div class="package-name">Short Package</div>
                <div class="desc">High Stability</div>
              </th>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
            </tr>
            <tr>
              <th class="white"></th>
              <th class="white"></th>
              <th v-if="shouldShowPackage('ace')" colspan="1">Investment Repartition</th>
              <th v-if="shouldShowPackage('slice')" colspan="1">Investment Repartition</th>
              <th v-if="shouldShowPackage('short')" colspan="1">Investment Repartition</th>
              <th class="subheader">Risk Level</th>
              <th class="subheader">Max Gain</th>
              <th class="subheader">League</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(match, index) in matches"
              :key="index"
              :class="`${packageName.toLowerCase()}-row`"
            >
              <td>
                <div class="team-row">
                  <div
                    class="image-container"
                    :class="{ 'winner-border': match.winner === 'player_1', 'loser-border': match.winner === 'player_2' }"
                  >
                    <img
                      :src="match.player_1_logo"
                      alt="Player 1 Logo"
                      class="player-logo"
                      @error="handleImgError"
                    />
                  </div>
                  <div class="player-name">{{ match.player_1 }}</div>
                </div>
              </td>
              <td>
                <div class="team-row">
                  <div
                    class="image-container"
                    :class="{ 'winner-border': match.winner === 'player_2', 'loser-border': match.winner === 'player_1' }"
                  >
                    <img
                      :src="match.player_2_logo"
                      alt="Player 2 Logo"
                      class="player-logo"
                      @error="handleImgError"
                    />
                  </div>
                  <div class="player-name">{{ match.player_2 }}</div>
                </div>
              </td>
              <td
                v-if="shouldShowPackage('ace')"
                class="package-cell ace-row"
              >{{ match.repartition[0] }}%</td>
              <td
                v-if="shouldShowPackage('slice')"
                class="package-cell slice-row"
              >{{ match.repartition[1] }}%</td>
              <td
                v-if="shouldShowPackage('short')"
                class="package-cell short-row"
              >{{ match.repartition[2] }}%</td>
              <td>{{ match.risk_level }}</td>
              <td>{{ match.max_gain }}</td>
              <td>{{ match.tournament_name }}</td>
            </tr>
          </tbody>
        </table>
        <div class="investment-container">
          <label for="investment-amount">How much do you want to invest?</label>
          <input
            type="number"
            id="investment-amount"
            v-model.number="investmentAmount"
            @input="calculateGains"
          />
          <span>€</span>
        </div>
        <div class="simulation-container">
          <h2>Investment Simulation</h2>
          <div v-if="investmentAmount > 0">
            <p>
              <strong>Average Gain:</strong>
              {{ averageGain.toFixed(2) }} €
            </p>
            <p>
              <strong>Max Gain:</strong>
              {{ maxGain.toFixed(2) }} €
            </p>
          </div>
        </div>
        <div class="button-container">
          <button :class="`invest-btn ${packageName.toLowerCase()}-btn`">Invest in this package!</button>
        </div>
      </div>
      <Footer></Footer>
    </div>
  </div>
</template>

    
<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";

function isCacheValid(cacheDate) {
  const today = new Date().toISOString().split("T")[0];
  return cacheDate === today;
}

function getCachedData(key) {
  const cachedData = localStorage.getItem(key);
  if (null) {
    const { date, data } = JSON.parse(cachedData);
    if (isCacheValid(date)) {
      return data;
    }
  }
  return null;
}

function setCachedData(key, data) {
  const today = new Date().toISOString().split("T")[0];
  const cacheData = {
    date: today,
    data: data
  };
  localStorage.setItem(key, JSON.stringify(cacheData));
}

export default {
  name: "Package",
  components: {
    Header,
    Footer
  },
  data() {
    return {
      matches: [],
      numMatches: 10, // Default number of matches to fetch
      packageName: "",
      investmentAmount: 0,
      averageGain: 0,
      maxGain: 0
    };
  },
  created() {
    this.packageName = this.$route.params.packageType;
    console.log(`Package Name: ${this.packageName}`);
    this.fetchMatches(this.numMatches);
  },
  watch: {
    "$route.params.packageType"(newVal) {
      this.packageName = newVal;
      console.log(`Package Name: ${this.packageName}`);
      this.renderPackageContent();
    }
  },
  methods: {
    async fetchMatches(numMatches) {
      const cacheKey = `matches_${numMatches}`;
      const cachedMatches = getCachedData(cacheKey);
      if (cachedMatches) {
        this.matches = this.processMatches(cachedMatches);
      } else {
        try {
          const response = await fetch(
            `${process.env.VUE_APP_BACKEND_URL}/get_matches?num_matches=${numMatches}`
          );
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          const matches = await response.json();
          this.matches = this.processMatches(matches);
          setCachedData(cacheKey, matches);
        } catch (error) {
          console.error("There was a problem with the fetch operation:", error);
        }
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
    handleImgError(event) {
      event.target.src = "/no_photo.jpeg";
    },
    computeRiskLevel(match) {
      let winRate, odds;
      if (match.meilleur_joueur === 1) {
        winRate = match.win_percentage_player_1;
        odds = match.odd_player_1;
      } else {
        winRate = match.win_percentage_player_2;
        odds = match.odd_player_2;
      }
      const impliedProbability = 1 / odds;
      const actualProbability = winRate / 100;
      const risk = Math.abs(impliedProbability - actualProbability);
      return risk.toFixed(2); // Risk level formula
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
    shouldShowPackage(packageType) {
      return this.packageName.toLowerCase() === packageType;
    },
    renderPackageContent() {
      // Logic to render content based on this.packageName
    },
    calculateMaxGain(matches, amount, packageName) {
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
        const gain =
          amount * (match.repartition[repartitionIndex] / 100) * match.max_gain;
        totalGain += gain;
      });
      return totalGain;
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
        const gain =
          amount *
          (match.repartition[repartitionIndex] / 100) *
          match.max_gain *
          match.risk_level;
        totalGain += gain;
      });
      return totalGain;
    },
    calculateGains() {
      this.averageGain = this.calculateAverageGain(
        this.matches,
        this.investmentAmount,
        this.packageName
      );
      this.maxGain = this.calculateMaxGain(
        this.matches,
        this.investmentAmount,
        this.packageName
      );
    }
  }
};
</script>

    
  <style scoped>
.logo {
  font-size: 2em;
  font-family: Lato;
  font-weight: 700;
  line-height: 150%;
  text-transform: uppercase;
}

.package-name {
  font-family: Arial, sans-serif;
  font-size: 30px;
  font-weight: bold;
}
.desc {
  font-size: 20px;
}
body,
html {
  margin: 0;
  padding: 0;
  height: 100%;
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
.matches-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  box-shadow: 0px 0px 0px red;
}
.matches-table th,
.matches-table td {
  border: 1px solid #ddd;
  padding: 4px;
  text-align: center;
  font-weight: bold;
  font-size: 16px;
}
.matches-table th {
  background-color: #5d576b;
  color: white;
  height: 30px;
  padding: 6px;
  font-size: 20px;
}
.matches-table th.white,
.matches-table td.white {
  background-color: white;
  border: none;
}
.matches-table .subheader {
  font-size: 18px;
}
.matches-table tr:nth-child(even) {
  background-color: #f2f2f2;
}
.matches-table tr:hover {
  background-color: #ddd;
}
.separator {
  background-color: #f0f0f0;
  height: 10vh;
}
.team-row {
  display: flex;
  align-items: center;
}
.image-container {
  position: relative;
  display: inline-block;
  border-radius: 50%;
  padding: 3px;
}
.image-container.winner-border {
  border: 2px solid green;
}
.image-container.loser-border {
  border: 2px solid red;
}
.player-logo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.player-name {
  font-weight: bold;
  margin-left: 8px;
  color: black;
}
.header-cell {
  border: none;
  color: white;
}
.header-cell.ace,
.package-cell.ace {
  background-color: #f1c40f;
  color: white;
  padding: 20px;
}
.header-cell.slice,
.package-cell.slice {
  background-color: #e67e22;
  color: white;
  padding: 20px;
}
.header-cell.short,
.package-cell.short {
  background-color: #3498db;
  color: white;
  padding: 20px;
}
.package-cell {
  padding: 20px;
}
.ace-row {
  color: black;
  background-color: rgba(241, 196, 15, 0.2);
}
.slice-row {
  color: black;
  background-color: rgba(230, 126, 34, 0.2);
}
.short-row {
  color: black;
  background-color: rgba(52, 152, 219, 0.2);
}
.ace-text {
  color: #f1c40f;
}
.slice-text {
  color: #e67e22;
}
.short-text {
  color: #3498db;
}
.investment-container {
  margin-top: 40px;
  font-size: 24px;
  text-align: center;
}
.investment-container label {
  margin-right: 10px;
  font-size: 24px;
}
.investment-container input {
  width: 150px;
  padding: 10px;
  font-size: 20px;
  border: 2px solid black;
  margin-right: 5px;
}
.investment-container span {
  font-size: 24px;
}
.simulation-container {
  margin-top: 20px;
  text-align: center;
  font-size: 24px;
}
.button-container {
  text-align: center;
  margin-top: 30px;
}
.invest-btn {
  padding: 15px 30px;
  font-size: 24px;
  font-weight: bold;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}
.ace-btn {
  background-color: #f1c40f;
  color: white;
}
.ace-btn:hover {
  background-color: #d4ac0d;
}
.slice-btn {
  background-color: #e67e22;
  color: white;
}
.slice-btn:hover {
  background-color: #ca6f1e;
}
.short-btn {
  background-color: #3498db;
  color: white;
}
.short-btn:hover {
  background-color: #2980b9;
}
</style>
  