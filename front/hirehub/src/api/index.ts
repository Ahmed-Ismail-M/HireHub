import { useAuthStore } from '@/stores/auth'
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/hirehub/api/v1', 
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.request.use((config) => {
  const token = useAuthStore().getToken()
  if (token) {
    config.headers.Authorization = `Token ${token}`
  }
  return config
})

export default api
