<template>
    <div class="home-footer">
        <footer class="footerContainer home-footer1">
            <div class="home-container31">
                <span class="logo">PARI FREE</span>
                <nav class="home-nav1">
                    <span class="home-nav22 bodySmall">Home</span>
                    <span class="home-nav22 bodySmall">Sports Betting</span>
                    <span class="home-nav22 bodySmall">Live Betting</span>
                    <span class="home-nav22 bodySmall">Promotions</span>
                    <span class="home-nav22 bodySmall">Support</span>
                </nav>
            </div>
            <div class="home-separator"></div>
        </footer>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
    name: 'Footer',
    components: {
        RouterLink
    }
}
</script>

<style>
.home-nav221 {
    margin-bottom: var(--dl-space-space-unit);
}

.home-footer {
    flex: 0 0 auto;
    width: 100%;
    height: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    border-top: 1px solid;
}

.home-footer1 {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
}


.home-footer1 {
    padding: var(--dl-space-space-unit);
}

.home-container31 {
    gap: var(--dl-space-space-unit);
    display: flex;
    max-width: var(--dl-size-size-maxwidth);
    align-items: center;
    flex-direction: column;
    justify-content: flex-start;
}

.home-nav1 {
    flex: 0 0 auto;
    display: flex;
    margin-top: 0px;
    align-items: center;
    flex-direction: row;
}
</style>