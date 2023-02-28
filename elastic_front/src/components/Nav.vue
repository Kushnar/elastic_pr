<template>
  <ul>
    <li>
      <router-link to="/">Головна</router-link>
    </li>
    <li>
      <router-link to="search/">Пошук</router-link>
    </li>
  </ul>


</template>

<script>
export default {
  name: "Nav",
}
</script>

<style scoped>
ul{
  display: inline-flex;
  justify-content: center;
  padding: 0;
}
li{
  list-style: none;
}
a{
  padding: 1rem;
}
</style>