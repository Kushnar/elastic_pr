<template>
  <div class="form-wrapper">
    <form action="" @submit.prevent="onSearchSubmit">
      <label for="search">Введіть ваш запит для пошуку:</label>
      <input id="search" v-model="searchValue" placeholder="Введіть дані для пошуку" required>
      <button type="submit">Шукати</button>
      <button type="button" v-on:click="onResetTable">До повної таблиці</button>
    </form>
    <div v-if="isEmptyResult">
      <p class="warning">За заданим запитом нічого не знайдено</p>
    </div>
  </div>
  <div class="container">
    <table v-if="isTableData">
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
</template>

<script>
import axios from "axios";

export default {
  name: "Main",
  data() {
    return {
      searchValue: null,
      itemsKeys: [],
      items: [],
      isEmptyResult: false,
      currentSortItem: null,
      sortOrdering: true,
    }
  },
  computed: {
    isTableData() {
      console.log('catch')
      if (this.items.length <= 0){
        this.loadItems()
      }
      console.log(this.items)
      return this.items
    },
  },
  methods: {
    async loadItems() {
      await axios.get(
          `${this.$store.getters.getBackendUrl}/get-table-data/`,
          {
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
              "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
            }
          }).then(response => {
        this.currentSortItem = null
        if (response.data.code === 200) {
          this.itemsKeys = Object.keys(response.data.data[0]._source)
          this.items = [...response.data.data]
          return this.items;
        } else {
          axios.get(`${this.$store.getters.getBackendUrl}/create-index`).then(
              response => {
                this.items = [...response.data.data]
                console.log(this.items, 400)
                return this.items
              }
          )
        }
      })

    },
    async sortTable(target) {
      if (this.currentSortItem === target) {
        this.sortOrdering = !this.sortOrdering
      } else {
        this.sortOrdering = true
        this.currentSortItem = target
      }
      this.items = await axios.post(
          `${this.$store.getters.getBackendUrl}/sort-table/`,
          {'target': target, 'direction': this.sortOrdering},
          {
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
              "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
            }
          }
      ).then(response => {
        console.log(response.data.data, this.currentSortItem, this.sortOrdering)
        if (response.data.data.length > 0){
          this.isEmptyResult = false
          this.itemsKeys = Object.keys(response.data.data[0]._source)
          return response.data.data
        } else {
          this.isEmptyResult = true
          return []
        }
      })
    },
    async onSearchSubmit() {
      this.currentSortItem = null
      this.items = await axios.post(
          `${this.$store.getters.getBackendUrl}/search`,
          {'value': this.searchValue}
      ).then(response => {
        if (response.data.data.length > 0) {
          this.isEmptyResult = false
          this.itemsKeys = Object.keys(response.data.data[0]._source)
          return response.data.data
        } else {
          this.isEmptyResult = true
          return []
        }
      })
    },
    onResetTable(){
      this.searchValue = ''
      this.isEmptyResult = false
      this.loadItems()
    }
  },
}
</script>

<style scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;
  padding: 10px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: start;
  font-size: 17px;
  margin: 0 0 5px 0;
}
form input{
  border: 1px solid #181818;
}

button {
  padding: 10px;
  margin: 0 0 5px 0;
  border-radius: 10px;
  border: solid 1px #2c3e50;
  background-color: transparent;
  cursor: pointer;
}
button:hover{
  background-color: grey;
}
.warning{
  border: 1px solid coral;
  border-radius: 10px;
  padding: 10px;
}
form input {
  margin: 5px 0;
  padding: 10px 4px;
  width: 100%;
  border-radius: 10px;
}

.container {
  max-width: 1280px;
  overflow: scroll;
}

table, td, th {
  border: solid 1px #181818;
  border-collapse: collapse;
}

th, td {
  text-align: center;
}
th span{
  cursor: pointer;
}
th span, td span {
  padding: 5px;
}

.active {
  background-color: #2c3e50;
  color: #f2f2f2;
}
</style>