import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/user/LoginPage.vue')
    },
    {
      path: '/',
      name: '/',
      component: () => import('@/views/user/TestPage.vue')
    }
  ],
})

export default router
