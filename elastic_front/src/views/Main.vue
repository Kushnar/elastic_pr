<template>
  <div class="container">
    <button v-on:click="onWriteClick">Записати у таблицю</button>
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
</template>

<script>
import axios from "axios";

export default {
  name: "Main",
  data() {
    return {
      items: [],
      itemsKeys: [],
      currentSortItem: null,
      sortOrdering: true,
    }
  },
  created() {
    this.loadItems()
  },
  methods: {
    async onWriteClick(){
      await axios.get(`${this.$store.getters.getBackendUrl}/create-index`).then(()=>{
        this.loadItems()
      })
    },
    async loadItems() {
      this.items = await axios.get(
          `${this.$store.getters.getBackendUrl}/get-table-data/`,
          {
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
              "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
            }
          }).then(response => {
            this.itemsKeys = Object.keys(response.data.data[0]._source)
            return response.data.data
          }
      )
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
        return response.data.data
      })
    }
  },
}
</script>

<style scoped>
.container {
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
.active{
  background-color: lightgreen;
  color: #181818;
}
</style>