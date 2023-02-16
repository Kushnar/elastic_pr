import {createStore} from 'vuex'

const store = createStore({
    state: {
        backendUrl: "http://localhost:8000",
        config: {
            headers: {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
            }
        }
    },
    mutations: {},
    actions:{},
    modules:{},
    getters: {
        getBackendUrl: (state) => {return state.backendUrl},
        getConfig: (state) => {return state.config},
    },
})

export default store