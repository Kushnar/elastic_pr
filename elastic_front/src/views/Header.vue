<template>
  <header>
    <Nav/>
  </header>
</template>

<script>
import Nav from "@/components/Nav.vue";

export default {
  name: "Header",
  components: {Nav}
}
</script>

<style scoped>
header {
  display: flex;
  width: 100%;
  padding: 1rem 2rem;
  margin: 0 0 1rem 0;
  /*border: solid 1px #181818;*/
  border-top: none;
  border-radius: 0 0 1rem 1rem;
}
</style>