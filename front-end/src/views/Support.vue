<template>
    <div class="home-container">
        <Header></Header>
        <div class="empty"></div>
        <div class="main">
            <h1>Support</h1>
            <h1>Support</h1>
            <h1>Support</h1>
            <h1>Support</h1>
            <h1>Support</h1>
            <h1>Support</h1>
            <h1>Support</h1>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

export default {
    nmae: "Support",
    components: {
        Header,
        Footer
    }
}
</script>

<style>
.empty {
    width: 100%;
    height: 20vh;
    background-color: red;
}
.home-container {
    width: 100%;
    display: flex;
    overflow: auto;
    min-height: 100vh;
    align-items: center;
    flex-direction: column;
}

.main {
    height: 100hv;
}
</style>