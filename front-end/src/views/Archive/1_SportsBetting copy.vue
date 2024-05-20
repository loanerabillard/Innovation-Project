<template>
  <div class="home-container">
    <Header></Header>
    <div class="separator"></div>
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
            <td>{{ match.team_1 }} vs {{ match.team_2 }}</td>
            <td>{{ match.win_percent_team_1 }}% / {{ match.win_percent_team_2 }}%</td>
            <td>{{ match.odd_team_1 }} / {{ match.odd_team_2 }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

export default {
  name: "SportsBetting",
  components: {
    Header,
    Footer
  },
  data() {
    return {
      matches: [
        {
          team_1: "Team A",
          team_2: "Team B",
          win_percent_team_1: 60,
          win_percent_team_2: 40,
          odd_team_1: 1.5,
          odd_team_2: 2.5
        },
        {
          team_1: "Team C",
          team_2: "Team D",
          win_percent_team_1: 55,
          win_percent_team_2: 45,
          odd_team_1: 1.7,
          odd_team_2: 2.2
        },
        {
          team_1: "Team E",
          team_2: "Team F",
          win_percent_team_1: 70,
          win_percent_team_2: 30,
          odd_team_1: 1.2,
          odd_team_2: 3.0
        }
      ]
    }
  }
}
</script>

<style>
.separator {
  background-color: blue;
  height: 14vh;
}
.home-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
}

.betting-container {
  width: 100%;
  height: 70vh;
  background-color: red;
}

.matches-table {
  width: 100%;
  background-color: orange;
  border: 1px solid black;
  border-collapse: collapse;
}

.matches-table th,
.matches-table td {
  border: 1px solid black;
  padding: 8px;
  text-align: center;
}
</style>
