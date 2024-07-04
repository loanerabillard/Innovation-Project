<template>
  <div class="card" :style="{ backgroundColor: bgColor }">
    <div class="card-header" :style="{ backgroundColor: bgColor }">
      <div class="package-name">{{ name }} Package</div>
      <!-- <div class="package-description">{{ description }}</div> -->
    </div>
    <div class="card-content">
      <div class="gain-info">
        <span class="euro-gain">{{ formattedGainEuro }}</span>
      </div>
      <div class="gain-info">
        <span class="percentage">{{ formattedGainPercent }}</span>
        <img :src="arrowImage" alt="Stonks" class="arrow" />
      </div>
    </div>
    <div class="card-footer">
      <button class="invest-button" :style="{backgroundColor: btBgColor}">Invest for next week</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    description: String,
    bgColor: String,
    extraInfo: String,
    amount: Number
  },
  data() {
    return {
      gainEuro: 0,
      gainPercent: 0,
      btBgColor: ''
    };
  },
  created() {
    // Log bgColor when the component is mounted
    console.log("bgColor:", this.bgColor);
    console.log("name:", this.name);
    console.log("description:", this.description);
    console.log("gainEuro:", this.gainEuro);
    console.log("amount:", this.amount);
    console.log("this.name:", this.name);

    switch (this.name) {
      case "Short":
        this.gainEuro = 0.07 * this.amount;
        this.gainPercent =
          ((this.gainEuro + this.amount) / this.amount) * 100 - 100;
        this.btBgColor = '#0266a9';
        break;
      case "Slice":
        this.gainEuro = 0.11 * this.amount;
        this.gainPercent =
          ((this.gainEuro + this.amount) / this.amount) * 100 - 100;
        this.btBgColor = '#bf9200';
        break;
      case "Ace":
        this.gainEuro = 0.03 * -this.amount;
        this.gainPercent =
          ((this.gainEuro + this.amount) / this.amount) * 100 - 100;
        this.btBgColor = '#b44c00';
        break;
      default:
        this.gainEuro = 0;
        this.gainPercent = 0;
        break;
    }

    console.log("Updated gainEuro:", this.gainEuro);
    console.log("Updated gainPercent:", this.gainPercent);
  },
  computed: {
    formattedGainEuro() {
      return (this.gainEuro >= 0 ? '+' : '') + this.gainEuro.toFixed(0) + '€';
    },
    formattedGainPercent() {
      return (this.gainPercent >= 0 ? '+' : '') + this.gainPercent.toFixed(0) + '%';
    },
    arrowImage() {
      return this.gainPercent >= 0 ? '/stonks.png' : '/not-stonks.webp';
    }
  },
  methods: {}
};
</script>

<style scoped>
/* Component-specific styles */
.card {
  width: 23%; /* Dynamic width */
  display: flex;
  flex-direction: column;
  border-radius: 25px;
  margin-bottom: 20px;
  background-color: black; /* Default background color */
  box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.card-header {
  color: #fff;
  text-align: center;
  padding: 20px;
  display: flex;
  flex-direction: column;
  background-color: black;
}

.package-name {
  font-size: 36px; /* Increased font size */
  font-weight: bold;
  margin-bottom: 10px; /* Increased margin for space */
}

.package-description {
  font-size: 28px; /* Increased font size */
  font-weight: 500;
  margin-bottom: 5px; /* Reduced margin for space */
}

.card-content {
  flex: 1;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #fff;
}

.gain-info {
  font-size: 60px; /* Large font size for percentage */
  font-weight: bold;
  display: flex;
  align-items: center;
}

.percentage,
.euro-gain {
  margin-right: 10px;
}

.arrow {
  width: 100px; /* Increased size of the stonks image */
  height: 100px;
}

.extra-info {
  font-size: 28px; /* Slightly smaller font size */
  margin-top: 15px; /* Increased margin for space */
  font-weight: bold; /* Made the number bold */
}

.card-footer {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.invest-button {
  font-size: 24px; /* Big font size for the button */
  font-weight: bold;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  color: #fff;
}
</style>
