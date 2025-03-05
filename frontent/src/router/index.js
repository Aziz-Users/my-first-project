import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../Views/HomeView.vue'
import NoPage from '../Views/NoPage.vue'



const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/:pathMath(.*)*',
            name: 'NoPage',
            component: NoPage,
        }
    ]

})


export default router