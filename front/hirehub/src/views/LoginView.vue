<template>
  <div class="container mt-4">
    <h1>Login</h1>
    <div v-if="isLoggedIn" class="alert alert-info">
      You are already logged in as {{ user.email }}.
      <button @click="logout" class="btn btn-secondary ms-2">Logout</button>
    </div>
    <form v-else @submit.prevent="login">
      <div class="mb-3">
        <label>Username</label>
        <input v-model="form.username" type="text" class="form-control" required />
      </div>
      <div class="mb-3">
        <label>Password</label>
        <input v-model="form.password" type="password" class="form-control" required />
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { loginEmployee } from '@/api/employee'
import { useToastStore } from '@/stores/toast'
import handleError from '@/services/error_service'
import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const toastStore = useToastStore()
const authStore = useAuthStore()

const form = ref({
  username: '',
  password: '',
})
const isLoggedIn = storeToRefs(authStore).token
const user = storeToRefs(authStore).user

const login = async () => {
  try {
    const response = await loginEmployee(form.value)
    authStore.login(response.data.token, response.data.user)
    toastStore.addToast('success', 'Logged in successfully')
    router.push('/')
  } catch (error) {
    const errorMessages = handleError(error, 'Login failed')
    toastStore.addToast('error', errorMessages)
  }
}

const logout = () => {
  authStore.logout()
  toastStore.addToast('success', 'Logged out successfully')
  router.push('/login')
}
</script>
