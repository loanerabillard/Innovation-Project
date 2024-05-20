<template>
  <div class="home-container">
    <Header></Header>
    <div class="separator"></div>
    <div class="content-container">
      <div class="betting-container">
        <h1>Sports Betting Page</h1>
        <table class="matches-table">
          <thead>
            <tr>
              <th>Match</th>
              <th>Winning Percentage</th>
              <th>Odds</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(match, index) in matches" :key="index">
              <td>
                <div class="team-info">
                  <img :src="match.team_1_logo" alt="Team 1 Logo" class="team-logo">
                  {{ match.team_1 }}
                </div>
                vs
                <div class="team-info">
                  <img :src="match.team_2_logo" alt="Team 2 Logo" class="team-logo">
                  {{ match.team_2 }}
                </div>
              </td>
              <td>{{ match.win_percent_team_1 }}% / {{ match.win_percent_team_2 }}%</td>
              <td>{{ match.odd_team_1 }} / {{ match.odd_team_2 }}</td>
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

const team_data = {
  team_1: "Team A",
  team_2: "Team B",
  team_1_logo: "https://media.api-sports.io/hockey/teams/12.png",
  team_2_logo: "https://media.api-sports.io/hockey/teams/14.png",
  win_percent_team_1: 60,
  win_percent_team_2: 40,
  odd_team_1: 1.5,
  odd_team_2: 2.5
};

const num = 6;
const teams_data = Array.from({ length: num }, () => ({ ...team_data }));

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
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
}

.matches-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.matches-table th,
.matches-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: center;
}

.matches-table th {
  background-color: #5d576b;
  color: white;
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

.team-info {
  display: flex;
  align-items: center;
}

.team-logo {
  width: 20px;
  height: 20px;
  margin-right: 8px;
}
</style>
