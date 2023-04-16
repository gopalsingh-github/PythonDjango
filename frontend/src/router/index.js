import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/Login.vue'
import InstituteSignup from '../views/InstituteSignup.vue'
// import StudentSignup from '../views/StudentSignup.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/institute-signup',
      name: 'institute-signup',
      component: InstituteSignup
    },

    {
      path:'/student-signup',
      name:'student-signup',
      component:()=> import('../views/StudentSignup.vue')

    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
