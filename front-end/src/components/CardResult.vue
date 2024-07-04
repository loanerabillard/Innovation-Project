<template>
    <div class="card" :style="{ borderColor: bgColor }">
      <div class="card-header" :style="{ backgroundColor: bgColor }">
        <div class="package-name">{{ name }}</div>
        <div class="package-description">{{ description }}</div>
      </div>
      <div class="card-content" :style="{ backgroundColor: bgColor }">
        <div class="gain-info">
          <span class="euro-gain">€{{ gainEuro.toFixed(2) }}</span>
        </div>
        <div class="gain-info">
          <span class="percentage">{{ gainPercent }}%</span>
          <img src="/stonks.png" alt="Stonks" class="arrow" />
        </div>
        <div class="extra-info">{{ extraInfo }}</div>
      </div>
      <div class="card-footer" :style="{ backgroundColor: bgColor }">
        <button class="invest-button">Invest now</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      name: String,
      description: String,
      bgColor: String,
      gainEuro: Number,
      gainPercent: String,
      extraInfo: String
    },
    mounted() {
    // Log bgColor when the component is mounted
    console.log('bgColor:', this.bgColor);
    },
    methods: {
    }
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
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    overflow: hidden;
    border: 10px solid;
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
  