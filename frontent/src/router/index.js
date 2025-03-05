import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../Views/HomeView.vue'
import NoPage from '../Views/NoPage.vue'
import Support from '../Views/SupportView.vue'
import Plans from '../Views/PlansView.vue'
import Partners from '../Views/PartnersView.vue'
import Creators from '../Views/CreatorsView.vue'
import Faq from '../Views/FaqView.vue'
import Login from '../Views/LoginView.vue'
import Reg from '../Views/RegView.vue'



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
        },
        {
            path: '/support',
            name: 'Support',
            component: Support,
        },
        {
            path: '/plans',
            name: 'Plans',
            component: Plans,
        },
        {
            path: '/partners',
            name: 'Partners',
            component: Partners,
        },
        {
            path: '/creators',
            name: 'Creators',
            component: Creators,
        },
        {
            path: '/faq',
            name: 'Faq',
            component: Faq,
        },
        {
            path: '/login',
            name: 'Login',
            component: Login,
        },
        {
            path: '/register',
            name: 'Register',
            component: Reg,
        }
    ]

})


export default router