<script setup>
import Header from "@/views/Header.vue";
import Main from "@/views/Main.vue";
</script>

<template>
  <Header/>
  <div class="wrapper">
    <main>
    <router-view></router-view>
    </main>
  </div>
</template>

<style scoped>

</style>
