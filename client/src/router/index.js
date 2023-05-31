import { createRouter, createWebHistory } from "vue-router";

import MainPage from '../pages/MainPage'



const routes =  [ {path : '/',name:'start', component : MainPage },
]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router