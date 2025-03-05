<script setup>
  import { RouterView } from 'vue-router';
  import FooterVue from './components/Footer.vue';
  import Header from './components/Header.vue';

</script>

<template>
  <div class="bg-black min-h-[100vh] text-white ">
  <div class="max-w-[1500px] mx-auto w-full">
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
  </div>
</template>

<style scoped>
  
</style>
