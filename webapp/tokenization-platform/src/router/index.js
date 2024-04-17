import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Tokenize.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Tokenize.vue')
    },
    {
      path: '/detokenize',
      name: 'detokenize',
      component: () => import('../views/Detokenize.vue')
    }
  ]
})

export default router
