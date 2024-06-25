<template>
  <div class="home-header">
    <header class="navbarContainer home-navbar-interactive">
      <span class="logo">PARI FREE</span>
      <div class="home-desktop-menu">
        <nav class="home-links">
          <router-link to="/" class="home-nav22 bodyLarge">Home</router-link>
          <router-link to="/sports-betting" class="home-nav22 bodyLarge">Invest Now</router-link>
          <router-link to="/historic" class="home-nav22 bodyLarge">My Packages</router-link>
          <!-- <router-link to="/pakacge" class="home-nav22 bodyLarge">Live Betting</router-link> -->
          <router-link to="/support" class="home-nav22 bodyLarge">Support</router-link>
        </nav>
        <div class="home-buttons">
          <button class="home-login buttonFlat">Login</button>
          <button class="buttonFilled">Register</button>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  name: 'Header',
  components: {
    RouterLink
  }
}
</script>

<style>
@media(max-width: 991px) {}

@media(max-width: 767px) {
  .home-navbar-interactive {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }

  .home-desktop-menu {
    display: none;
  }
}

@media(max-width: 479px) {
  .home-navbar-interactive {
    padding: var(--dl-space-space-unit);
  }
}

.home-desktop-menu {
  flex: 1;
  display: flex;
  justify-content: space-between;
}

.home-header {
  width: 100%;
  display: flex;
  position: fixed;
  align-items: center;
  flex-direction: column;
  background-color: var(--dl-color-gray-white);
  border-bottom: solid 1px;
  z-index: 1000;
}

.home-links {
  flex: 1;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: center;
}

.home-nav22 {
  /* font-size: 25px; */
  cursor: pointer;
  margin-left: 30px;
}

.home-buttons {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}

.home-login {
  margin-right: 32px;
}
</style>
