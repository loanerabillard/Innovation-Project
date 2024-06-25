<template>
  <div class="home-container">
    <Header></Header>
    <div class="separator"></div>
    <div class="content-container">
      <div class="betting-container">
        <h1>Package</h1>
        <table class="matches-table">
          <thead>
            <tr>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
              <th class="ace header-cell">
                <div class="package-name">Ace Package</div>
                <div class="desc">High Potential Gain</div>
              </th>
              <th class="slice header-cell">
                <div class="package-name">Slice Package</div>
                <div class="desc">Balanced Gain and Stability</div>
              </th>
              <th class="short header-cell">
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
              <th colspan="3" class>Investment Repartition</th>
              <!-- <th class="slice-row">Medium Potential Gain</th>
              <th class="short-row">High Stability</th>-->
              <th class="subheader">Risk Level</th>
              <th class="subheader">Max Gain</th>
              <th class="subheader">League</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match, index) in matches" :key="index">
              <td>
                <div class="team-row">
                  <div
                    class="image-container"
                    :class="{ 'winner-border': match.winner === 'player_1', 'loser-border': match.winner === 'player_2' }"
                  >
                    <img :src="match.player_1_logo" alt="Player 1 Logo" class="player-logo" />
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
                    <img :src="match.player_2_logo" alt="Player 2 Logo" class="player-logo" />
                  </div>
                  <div class="player-name">{{ match.player_2 }}</div>
                </div>
              </td>
              <td class="package-cell ace-row">{{ match.repartition[0] }}%</td>
              <td class="package-cell slice-row">{{ match.repartition[1] }}%</td>
              <td class="package-cell short-row">{{ match.repartition[2] }}%</td>
              <td>{{ match.risk_level }}</td>
              <td>{{ match.max_gain }}</td>
              <td>{{ match.tournament_name }}</td>
            </tr>
            <tr>
              <td class="white"></td>
              <td class="white"></td>
              <td class="package-cell ace">
                <button class="choose-btn ace">Choose Ace Package</button>
              </td>
              <td class="package-cell slice">
                <button class="choose-btn slice">Choose Slice Package</button>
              </td>
              <td class="package-cell short">
                <button class="choose-btn short">Choose Short Package</button>
              </td>
              <td class="white"></td>
              <td class="white"></td>
              <td class="white"></td>
            </tr>
          </tbody>
        </table>
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
  name: "SportsBetting",
  components: {
    Header,
    Footer
  },
  data() {
    return {
      matches: [],
      numMatches: 10 // Default number of matches to fetch
    };
  },
  created() {
    this.fetchMatches(this.numMatches);
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
            `http://localhost:5000/get_matches?num_matches=${numMatches}`
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
      console.log(matches.length);
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
    }
  }
};
</script>
  
  
  <style scoped>
.package-name {
  font-family: Arial, sans-serif; /* Setting Arial as the font, with sans-serif as the fallback */
  font-size: 30px; /* Increased font size */
  font-weight: bold; /* Keeping the text bold */
}
.desc {
  font-size: 20px;
}
/* Styles remain the same */
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
  padding: 4px; /* Reduced padding */
  text-align: center;
  font-weight: bold;
  font-size: 16px; /* Reduced font size */
}

.matches-table th {
  background-color: #5d576b;
  color: white;
  height: 30px; /* Reduced height */
  padding: 6px; /* Reduced padding */
  font-size: 20px; /* Reduced font size */
}

.matches-table th.white,
.matches-table td.white {
  background-color: white;
  border: none; /* Remove border for white cells */
}

.matches-table .subheader {
  font-size: 18px; /* Reduced font size */
}

.matches-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.matches-table tr:hover {
  background-color: #ddd;
}

.separator {
  background-color: #f0f0f0;
  height: 10vh; /* Reduced height */
}

.team-row {
  display: flex;
  align-items: center;
}

.image-container {
  position: relative;
  display: inline-block;
  border-radius: 50%;
  padding: 3px; /* Reduced padding */
}

.image-container.winner-border {
  border: 2px solid green; /* Reduced border width */
}

.image-container.loser-border {
  border: 2px solid red; /* Reduced border width */
}

.player-logo {
  width: 40px; /* Reduced size */
  height: 40px; /* Reduced size */
  border-radius: 50%;
}

.player-name {
  font-weight: bold;
  margin-left: 8px; /* Reduced margin */
  color: black;
}

.choose-btn {
  width: 100%;
  padding: 20px; /* Reduced padding */
  border: none;
  cursor: pointer;
  font-size: 20px; /* Reduced font size */
  margin: 5px; /* Reduced margin */
}

.choose-btn.ace {
  background-color: #f1c40f; /* Yellow color for Ace */
  color: white;
}

.choose-btn.ace:hover {
  background-color: #d4ac0d;
}

.choose-btn.slice {
  background-color: #e67e22; /* Orange color for Slice */
  color: white;
}

.choose-btn.slice:hover {
  background-color: #ca6f1e;
}

.choose-btn.short {
  background-color: #3498db; /* Blue color for Short */
  color: white;
}

.choose-btn.short:hover {
  background-color: #2980b9;
}

.header-cell {
  border: none;
  color: white;
}

.header-cell.ace,
.package-cell.ace {
  background-color: #f1c40f; /* Yellow color for Ace without alpha */
  color: white;
  padding: 20px; /* Reduced padding */
}

.header-cell.slice,
.package-cell.slice {
  background-color: #e67e22; /* Orange color for Slice without alpha */
  color: white;
  padding: 20px; /* Reduced padding */
}

.header-cell.short,
.package-cell.short {
  background-color: #3498db; /* Blue color for Short without alpha */
  color: white;
  padding: 20px; /* Reduced padding */
}

.package-cell {
  padding: 20px; /* Reduced padding */
}

.ace-row {
  color: black;
  background-color: rgba(
    241,
    196,
    15,
    0.2
  ); /* Yellow color for Ace with alpha */
}

.slice-row {
  color: black;
  background-color: rgba(
    230,
    126,
    34,
    0.2
  ); /* Orange color for Slice with alpha */
}

.short-row {
  color: black;
  background-color: rgba(
    52,
    152,
    219,
    0.2
  ); /* Blue color for Short with alpha */
}
</style>