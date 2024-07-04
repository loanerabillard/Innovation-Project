<template>
  <div class="old-page-content">
    <div class="content-container">
      <div class="betting-container">
        <table class="matches-table">
          <thead>
            <tr>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
              <th class="short header-cell">
                <div class="package-name">Short Package</div>
                <div class="desc">High Stability</div>
              </th>
              <th class="slice header-cell">
                <div class="package-name">Slice Package</div>
                <div class="desc">Good Gain and Stability</div>
              </th>
              <th class="ace header-cell">
                <div class="package-name">Ace Package</div>
                <div class="desc">High Potential Gain</div>
              </th>
              <th class="header-cell white"></th>
              <th class="header-cell white"></th>
            </tr>
            <tr>
              <th class="white"></th>
              <th class="white"></th>
              <th colspan="3">Package Investment Repartition</th>
              <th class="subheader">Risk Level</th>
              <th class="subheader">Max Gain</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(match, index) in firstFiveMatches"
              :key="index"
              :style="{ opacity: index < 3 ? 1 : 1 - getOpacityTop(index - 3) }"
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
              <td class="package-cell short-row">{{ match.repartition[2] }}%</td>
              <td class="package-cell slice-row">{{ match.repartition[1] }}%</td>
              <td class="package-cell ace-row">{{ match.repartition[0] }}%</td>
              <td>{{ match.risk_level }}</td>
              <td>{{ match.max_gain }}</td>
            </tr>
            <tr class="ellipsis-row">
              <td>⋮</td>
              <td>⋮</td>
              <td>⋮</td>
              <td>⋮</td>
              <td>⋮</td>
              <td>⋮</td>
              <td>⋮</td>
            </tr>
            <tr
              v-for="(match, index) in lastFiveMatches"
              :key="(index * 3000) + 300"
              :style="{ opacity: index >= 2 ? 1 : 1 - getOpacityBottom(index) }"
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
              <td class="package-cell short-row">{{ match.repartition[2] }}%</td>
              <td class="package-cell slice-row">{{ match.repartition[1] }}%</td>
              <td class="package-cell ace-row">{{ match.repartition[0] }}%</td>
              <td>{{ match.risk_level }}</td>
              <td>{{ match.max_gain }}</td>
            </tr>
            <tr v-if="showButtons">
              <td class="white"></td>
              <td class="white"></td>
              <td class="package-cell short">
                <button class="invest-button short">Choose Short Package</button>
              </td>
              <td class="package-cell slice">
                <button class="invest-button slice">Choose Slice Package</button>
              </td>
              <td class="package-cell ace">
                <button class="invest-button ace">Choose Ace Package</button>
              </td>
              <td class="white"></td>
              <td class="white"></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  name: "OldPageContent",
  props: {
    matches: {
      type: Array,
      default: () => []
    },
    showButtons: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    firstFiveMatches() {
      return this.matches.slice(0, 5);
    },
    lastFiveMatches() {
      return this.matches.slice(-5);
    }
  },
  methods: {
    getOpacityTop(index) {
      return (index + 1) * 0.35;
    },
    getOpacityBottom(index) {
      return (2 - index) * 0.35;
    },
    handleImgError(event) {
      event.target.src = "/no_photo.jpeg";
    }
  }
};
</script>
  
<style scoped>
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
  margin-left: -5px;
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

/* Removed the alternating row color rule */
/*
.matches-table tr:nth-child(even) {
  background-color: #f2f2f2;
}
*/

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
  margin-right: -10px;
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
  margin-left: 0px;
  color: black;
  font-size: 15px;
}

.invest-button {
  font-size: 24px;
  font-weight: bold;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  color: #fff;
}

.invest-button.ace {
  background-color: #e67e22;
}

.invest-button.slice {
  background-color: #f1c40f;
}

.invest-button.short {
  background-color: #2980b9;
}

.header-cell {
  border: none;
  color: white;
}

.header-cell.short,
.package-cell.short {
  background-color: #3498db;
  color: white;
  padding: 20px;
}

.header-cell.slice,
.package-cell.slice {
  background-color: #f1c40f;
  color: white;
  padding: 20px;
}

.header-cell.ace,
.package-cell.ace {
  background-color: #e67e22;
  color: white;
  padding: 20px;
}

.package-cell {
  padding: 20px;
}

.short-row {
  color: black;
  background-color: rgba(52, 152, 219, 0.2);
}

.slice-row {
  color: black;
  background-color: rgba(241, 196, 15, 0.2);
}

.ace-row {
  color: black;
  background-color: rgba(230, 126, 34, 0.2);
}

.ellipsis {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  color: black;
}

.ellipsis-row {
  background-color: white;
}

.ellipsis-row td {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  color: black;
}
</style>
