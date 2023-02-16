import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import Main from "@/views/Main.vue";
import SearchTemplate from "@/views/SearchTemplate.vue";


const routes = [
    {path: '', component: Main},
    {path: '/search/', component: SearchTemplate},
]

export const router = createRouter(
    {history: createWebHistory(), routes,}
)