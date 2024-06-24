<template>
  <div class="home-container">
    <span>test</span>
    <Header></Header>
    <div class="separator"></div>
    <div class="content-container">
      <div class="betting-container">
        <h1>Live Betting Page</h1>
        <table class="matches-table">
          <thead>
            <tr>
              <th>League</th>
              <th>Match</th>
              <th>Winning Percentage</th>
              <th>Odds</th>
              <th>Team to bet on</th>
              <th>Expected Gain</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match, index) in matches" :key="index">
              <td>{{ match.league }}</td>
              <td>
                <div class="match-cell">
                  <div class="team-row">
                    <img :src="match.team_1_logo" alt="Team 1 Logo" class="team-logo">
                    <span>{{ match.team_1 }}</span>
                  </div>
                  <div class="vs-row">
                    <span>Vs</span>
                  </div>
                  <div class="team-row">
                    <img :src="match.team_2_logo" alt="Team 2 Logo" class="team-logo">
                    <span>{{ match.team_2 }}</span>
                  </div>
                </div>
              </td>
              <td>
                <div class="split-cell">
                  <div class="team-row">
                    <img :src="match.team_1_logo" alt="Team 1 Logo" class="team-logo">
                    <span>{{ match.win_percent_team_1 }}%</span>
                  </div>
                  <div class="team-row">
                    <img :src="match.team_2_logo" alt="Team 2 Logo" class="team-logo">
                    <span>{{ match.win_percent_team_2 }}%</span>
                  </div>
                </div>
              </td>
              <td>
                <div class="split-cell">
                  <div class="team-row">
                    <img :src="match.team_1_logo" alt="Team 1 Logo" class="team-logo">
                    <span>{{ match.odd_team_1 }}</span>
                  </div>
                  <div class="team-row">
                    <img :src="match.team_2_logo" alt="Team 2 Logo" class="team-logo">
                    <span>{{ match.odd_team_2 }}</span>
                  </div>
                </div>
              </td>
              <td>
                <div class="split-cell">
                  <div class="team-row" v-if="match.team_to_bet_on === 1">
                    <img :src="match.team_1_logo" alt="Team 1 Logo" class="team-logo">
                    <span>{{ match.team_1 }}</span>
                  </div>
                  <div class="team-row" v-else>
                    <img :src="match.team_2_logo" alt="Team 2 Logo" class="team-logo">
                    <span>{{ match.team_2 }}</span>
                  </div>
                </div>
              </td>
              <td>{{ match.expected_gain }}%</td>
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

console.log('test')

// Function to generate a random integer between min and max (inclusive)
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Function to generate random match data
function generateRandomMatch() {
  const league = "League " + String.fromCharCode(65 + getRandomInt(0, 5)); // Random league from League A to League F
  const team_1 = "Team A";
  const team_2 = "Team B";
  const team_1_logo = "https://media.api-sports.io/hockey/teams/12.png";
  const team_2_logo = "https://media.api-sports.io/hockey/teams/14.png";
  const win_percent_team_1 = getRandomInt(0, 100);
  const win_percent_team_2 = 100 - win_percent_team_1;
  const odd_team_1 = (Math.random() * (3 - 1) + 1).toFixed(2); // Random odd between 1 and 3
  const odd_team_2 = (Math.random() * (3 - 1) + 1).toFixed(2); // Random odd between 1 and 3
  const team_to_bet_on = getRandomInt(1, 2);
  const expected_gain = getRandomInt(1, 20);

  return {
    league,
    team_1,
    team_2,
    team_1_logo,
    team_2_logo,
    win_percent_team_1,
    win_percent_team_2,
    odd_team_1,
    odd_team_2,
    team_to_bet_on,
    expected_gain,
  };
}

// Generate an array of random match data
const num = 6;
const teams_data = Array.from({ length: num }, generateRandomMatch);

export default {
  name: "SportsBetting",
  components: {
    Header,
    Footer
  },
  data() {
    return {
      matches: teams_data
    };
  }
};

</script>


<style>
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
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  /* Move shadow to the table */
}

.matches-table th,
.matches-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: center;
  font-weight: bold;
  font-size: 18px;
  /* Increase font size */
}

.matches-table th {
  background-color: #5d576b;
  color: white;
  height: 80px;
  /* Adjust this value to make the header bigger */
  padding: 15px;
  /* Adjust padding for better alignment */
  font-size: 22px;
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

.match-cell,
.split-cell {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.team-row,
.vs-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.team-logo {
  width: 30px;
  height: 30px;
}
</style>
