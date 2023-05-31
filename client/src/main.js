import { createApp } from "vue";

import App from './App.vue'
import VueCookies from 'vue3-cookies'
import router from './router/index'
// import store from "./store/index";

import './axios'

const app = createApp(App);
app.use(router);
// app.use(store);
app.use(VueCookies)
app.mount('#app')

// createApp(App).use(router).use(store).mount('#app')