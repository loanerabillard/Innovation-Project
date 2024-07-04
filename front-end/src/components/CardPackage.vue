<template>
  <div class="card" :style="{ borderColor: bgColor }">
    <div class="card-header" :style="{ backgroundColor: bgColor }">
      <div class="package-name">{{ name }}</div>
      <div class="package-description">{{ description }}</div>
    </div>
    <div class="card-content" :style="{ backgroundColor: bgColor }">
      <div class="gain-info">
        <span class="percentage">+{{ avgGain2024 }}</span>
        <img src="/stonks.png" alt="Stonks" class="arrow" /> <!-- Updated image source -->
      </div>
      <div class="year-info">in 2024</div>
      <div class="extra-info">{{ extraInfo }}</div> <!-- Added extra info line -->
    </div>
    <div class="card-footer" :style="{ backgroundColor: bgColor }">
      <button class="invest-button" :style="{ backgroundColor: buttonColor }">Invest for next week</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    description: String,
    bgColor: String,
    avgGain2023: String,
    avgGain2024: String,
    extraInfo: String // Added extraInfo prop
  },
  computed: {
    buttonColor() {
      // Adjust the main color to be more distinguishable for the button
      return this.adjustColor(this.bgColor, -50);
    }
  },
  methods: {
    adjustColor(color, amount) {
      // Simple color adjustment function
      return '#' + color.replace(/^#/, '').replace(/../g, color =>
        ('0' + Math.min(255, Math.max(0, parseInt(color, 16) + amount)).toString(16)).substr(-2)
      );
    }
  }
};
</script>

<style scoped>
.card {
  width: 24%; /* Dynamic width */
  display: flex;
  flex-direction: column;
  border-radius: 25px;
  margin-bottom: 20px;
  background-color: #fff;
  box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  border: 1px solid;
}

.card-header {
  color: #fff;
  text-align: center;
  padding: 20px;
  display: flex;
  flex-direction: column;
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

.percentage {
  margin-right: 10px;
}

.arrow {
  width: 100px; /* Increased size of the stonks image */
  height: 100px;
}

.year-info {
  font-size: 32px; /* Increased font size */
  margin-top: 10px; /* Reduced margin for space */
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
  background-color: inherit; /* Fix the background color */
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
