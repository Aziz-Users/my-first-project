<script setup>
  import { RouterView } from 'vue-router';
  import FooterVue from './components/Footer.vue';
  import Header from './components/Header.vue';

</script>

<template>
  <div class="bg-black min-h-[100vh] text-white">
    <header>
      <Header />
    </header>
    <main>
      <RouterView />
    </main>

    <footer>
      <FooterVue />
    </footer>
  </div>
</template>

<style scoped>
  
</style>
