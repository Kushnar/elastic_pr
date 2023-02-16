<template>
  <div class="form-wrapper">
    <form action="" @submit.prevent="onSubmit">
      <label for="search">Введіть ваш запит для пошуку:</label>
      <input id="search" v-model="searchValue" placeholder="search">
      <button type="submit">Шукати</button>
    </form>
  </div>

  <div v-if="items.length > 0" class="container">
    <table>
      <thead>
      <tr>
        <th colspan="1" v-for="k in itemsKeys">
          <span v-on:click="sortTable(k)" :class="{active: currentSortItem===k}">{{ k }}</span>
        </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="itm in items">
        <td v-for="i in itm._source">
          <span>{{ i }}</span>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
  <div v-if="isEmptyResult" class="container">За заданим запитом нічого не знайдено</div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchTemplate",
  data() {
    return {
      searchValue: null,
      itemsKeys: [],
      items: [],
      isEmptyResult: false,
    }
  },
  methods: {
    async onSubmit() {
      this.items = await axios.post(
          `${this.$store.getters.getBackendUrl}/search`,
          {'value': this.searchValue}
      ).then(response => {
        if (response.data.data.length > 0){
          this.isEmptyResult = false
          this.itemsKeys = Object.keys(response.data.data[0]._source)
          return response.data.data
        } else {
          this.isEmptyResult = true
          return []
        }
      })
    }
  }
}
</script>

<style scoped>
.form-wrapper {
  display: flex;
  padding: 10px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: start;
  font-size: 23px;
}

button {
  padding: 10px;
  border-radius: 10px;
  border: solid 1px hsla(160, 100%, 37%, 1);
  background-color: transparent;
  color: #f2f2f2;
  cursor: pointer;
}

button:hover {
  background-color: hsla(160, 100%, 37%, 1);
  color: #181818;
}

form input {
  margin: 5px 0;
  padding: 10px 4px;
  font-size: 20px;
  width: 100%;
  border-radius: 10px;

}

.container {
  display: block;
  max-width: 1280px;
  overflow: scroll;

}

table, td, th {
  border: solid 1px hsla(160, 100%, 37%, 1);
  border-collapse: collapse;
}

th {
  background-color: #2c3e50;
}

th, td {
  text-align: center;
}

th span, td span {
  padding: 5px;
  cursor: pointer;
}

.active {
  background-color: lightgreen;
  color: #181818;
}
</style>