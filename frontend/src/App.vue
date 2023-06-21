<script setup>
import Login from './components/Login.vue'
</script>

<template>
  <div>
      <img src="./assets/qrcode.png" class="logo vue" alt="Vue logo" />  
  </div>
  <Login msg="Vite + Vue" />
</template>

<style scoped>
.logo {
  height: 8em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #f37006aa);
}
</style>