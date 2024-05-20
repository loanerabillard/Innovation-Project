<template>
  <div class="not-found1-container">
    <h3>OOPS! PAGE NOT FOUND</h3>
    <div class="not-found1-container1"><h1 class="not-found1-text1">404</h1></div>
    <div class="not-found1-container2">
      <h2 class="not-found1-text2">
        WE ARE SORRY, BUT THE PAGE YOU REQUESTED WAS NOT FOUND
      </h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound1',
  metaInfo: {
    title: 'Spotless Hungry Crocodile',
  },
}
</script>

<style scoped>
.not-found1-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.not-found1-container1 {
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.not-found1-text1 {
  color: rgb(38, 38, 38);
  font-size: 252px;
  margin-top: -20px;
  font-weight: 900;
  margin-bottom: -20px;
  letter-spacing: -20px;
}
.not-found1-container2 {
  width: 421px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.not-found1-text2 {
  text-align: center;
  font-weight: 400;
}
</style>
