import { createRouter, createWebHistory } from 'vue-router'
import EmployeeView from '../views/EmployeeView.vue'
import LoginView from '../views/LoginView.vue'
import CompanyView from '@/views/CompanyView.vue'
import DepartmentView from '@/views/DepartmentView.vue'

import DashBoardView from '@/views/DashBoardView.vue'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: DashBoardView },
    { path: '/employees', component: EmployeeView, meta: { requiresAuth: true } },
    { path: '/companies', component: CompanyView, meta: { requiresAuth: true } },
    { path: '/departments', component: DepartmentView, meta: { requiresAuth: true } },
    { path: '/login', component: LoginView },
  ],
})
router.beforeEach((to, from, next) => {
  const isAuthenticated = useAuthStore().isAuthenticated()

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
