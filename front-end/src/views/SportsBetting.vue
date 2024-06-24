<template>
  <div class="home-container">
    <Header></Header>
    <div class="separator"></div>
    <div class="content-container">
      <div class="betting-container">
        <h1>Live Betting Page</h1>
        <table class="matches-table">
          <thead>
            <tr>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
              <th class="header-cell ace">Ace</th>
              <th class="header-cell slice">Slice</th>
              <th class="header-cell short">Short</th>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
            </tr>
            <tr>
              <th class="white"></th>
              <th class="white"></th>
              <th class="subheader">Ace Investment Repartition</th>
              <th class="subheader">Slice Investment Repartition</th>
              <th class="subheader">Short Investment Repartition</th>
              <th class="subheader">Risk Level</th>
              <th class="subheader">Max Gain</th>
              <th class="subheader">League</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match, index) in matches" :key="index">
              <td>
                <div class="team-row">
                  <div class="image-container">
                    <img :src="match.player_1_logo" alt="Player 1 Logo" class="player-logo" />
                  </div>
                  <div :class="['player-name', { 'winner': match.winner === 'player_1', 'loser': match.winner === 'player_2' }]">
                    {{ match.player_1 }}
                  </div>
                </div>
              </td>
              <td>
                <div class="team-row">
                  <div class="image-container">
                    <img :src="match.player_2_logo" alt="Player 2 Logo" class="player-logo" />
                  </div>
                  <div :class="['player-name', { 'winner': match.winner === 'player_2', 'loser': match.winner === 'player_1' }]">
                    {{ match.player_2 }}
                  </div>
                </div>
              </td>
              <td>{{ match.repartition[0] }}%</td>
              <td>{{ match.repartition[1] }}%</td>
              <td>{{ match.repartition[2] }}%</td>
              <td>{{ match.risk_level }}</td>
              <td>{{ match.max_gain }}</td>
              <td>{{ match.tournament_name }}</td>
            </tr>
            <tr>
              <td class="white"></td>
              <td class="white"></td>
              <td><button class="choose-btn ace">Choose Ace</button></td>
              <td><button class="choose-btn slice">Choose Slice</button></td>
              <td><button class="choose-btn short">Choose Short</button></td>
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
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

const teams_data = [
  {
    "bookmaker_odd_player_1": "Betfair",
    "bookmaker_odd_player_2": "Betfair",
    "meilleur_ratio": 376.9230769230769,
    "note": 376.9230769230769,
    "odd_player_1": 1.16,
    "odd_player_2": 7.0,
    "player_1": "I. Swiatek",
    "player_1_logo": "https://api.api-tennis.com/logo-tennis/1910_i-swiatek.jpg",
    "player_2": "C. Gauff",
    "player_2_logo": "https://api.api-tennis.com/logo-tennis/2176_c-gauff.jpg",
    "player_2_flag": 'france-flag.png',
    "player_1_flag": 'france-flag.png',
    "rang": 1,
    "repartition": [
      "50",
      "33",
      "25"
    ],
    "tournament_name": "WTA French Open",
    "win_percentage_player_1": 76.92307692307693,
    "win_percentage_player_2": 53.84615384615385
  },
  {
    "bookmaker_odd_player_1": "Betfair",
    "bookmaker_odd_player_2": "Betfair",
    "meilleur_ratio": 142.67999999999998,
    "note": 142.67999999999998,
    "odd_player_1": 1.67,
    "odd_player_2": 2.46,
    "player_1": "C. Alcaraz",
    "player_1_logo": "https://api.api-tennis.com/logo-tennis/2382_c-alcaraz.jpg",
    "player_2": "J. Sinner",
    "player_2_logo": "https://api.api-tennis.com/logo-tennis/2072_j-sinner.jpg",
    "player_2_flag": 'france-flag.png',
    "player_1_flag": 'france-flag.png',
    "rang": 2,
    "repartition": [
      "25",
      "33",
      "25"
    ],
    "tournament_name": "ATP French Open",
    "win_percentage_player_1": 61.53846153846154,
    "win_percentage_player_2": 57.99999999999999
  },
  {
    "bookmaker_odd_player_1": "Betfair",
    "bookmaker_odd_player_2": "Betfair",
    "meilleur_ratio": 128.88888888888889,
    "note": 128.88888888888889,
    "odd_player_1": 2.32,
    "odd_player_2": 1.74,
    "player_1": "J. Paolini",
    "player_1_logo": "https://api.api-tennis.com/logo-tennis/2811_j-paolini.jpg",
    "player_2": "M. Andreeva",
    "player_2_logo": null,
    "player_2_flag": 'france-flag.png',
    "player_1_flag": 'france-flag.png',
    "rang": 3,
    "repartition": [
      "25",
      "33",
      "50"
    ],
    "tournament_name": "WTA French Open",
    "win_percentage_player_1": 55.55555555555556,
    "win_percentage_player_2": 43.103448275862064
  },
];

export default {
  name: "SportsBetting",
  components: {
    Header,
    Footer
  },
  data() {
    return {
      matches: []
    };
  },
  created() {
    this.matches = this.processMatches(teams_data);
  },
  methods: {
    processMatches(matches) {
      return matches.map(match => {
        match.winner = match.win_percentage_player_1 > match.win_percentage_player_2 ? 'player_1' : 'player_2';
        match.risk_level = this.computeRiskLevel(match);
        match.max_gain = this.computeMaxGain(match);
        return match;
      });
    },
    computeRiskLevel(match) {
      const risk = Math.abs(match.win_percentage_player_1 - match.win_percentage_player_2);
      return risk.toFixed(2); // Risk level formula (can be adjusted)
    },
    computeMaxGain(match) {
      const max_gain = Math.max(match.odd_player_1, match.odd_player_2);
      return max_gain.toFixed(2); // Max gain formula (can be adjusted)
    }
  }
};
</script>

<style scoped>
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
  padding: 12px;
  text-align: center;
  font-weight: bold;
  font-size: 18px;
}

.matches-table th {
  background-color: #5d576b;
  color: white;
  height: 80px;
  padding: 15px;
  font-size: 22px;
}

.matches-table th.white,
.matches-table td.white {
  background-color: white;
  border: none; /* Remove border for white cells */
}

.matches-table .subheader {
  font-size: 16px; /* Reduced font size */
}

.matches-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.matches-table tr:hover {
  background-color: #ddd;
}

.separator {
  background-color: #f0f0f0;
  height: 14vh;
}

.team-row {
  display: flex;
  align-items: center;
}

.image-container {
  position: relative;
  display: inline-block;
}

.player-logo {
  width: 70px;
  height: 70px;
  border-radius: 50%;
}

.player-name {
  font-weight: bold;
  margin-left: 10px;
  color: black;
}

.player-name.winner {
  text-decoration: underline;
  text-decoration-color: green;
  text-decoration-thickness: 3px; /* Increase underline thickness */
}

.player-name.loser {
  text-decoration: underline;
  text-decoration-color: red;
  text-decoration-thickness: 3px; /* Increase underline thickness */
}

.choose-btn {
  width: 100%;
  padding: 15px;
  border: none;
  cursor: pointer;
  font-size: 18px;
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
}

.header-cell.ace {
  background-color: #f1c40f; /* Yellow color for Ace */
  color: white;
}

.header-cell.slice {
  background-color: #e67e22; /* Orange color for Slice */
  color: white;
}

.header-cell.short {
  background-color: #3498db; /* Blue color for Short */
  color: white;
}
</style>
