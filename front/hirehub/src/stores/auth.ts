import type { LoginUser } from '@/types'
import { defineStore } from 'pinia'
import { ref } from 'vue'
const TOKEN_KEY = 'token'
const USER = 'user'

export const useAuthStore = defineStore('auth', () => {
  const token = ref<string | null>(localStorage.getItem(TOKEN_KEY))
  const user = ref<LoginUser>(JSON.parse(localStorage.getItem(USER) || '{}'))
  const login = (newToken: string, newUser: LoginUser) => {
    token.value = newToken
    user.value = newUser
    localStorage.setItem(TOKEN_KEY, newToken)
    localStorage.setItem(USER, JSON.stringify(newUser))
    return newToken
  }
  const getUser = (): LoginUser => {
    return user.value
  }

  const logout = () => {
    token.value = null
    user.value = {} as LoginUser
    localStorage.removeItem(TOKEN_KEY)
    localStorage.removeItem(USER)
  }

  const getToken = (): string | null => {
    return token.value
  }

  const isAuthenticated = (): boolean => {
        return !!token.value
  }

  return { token, user, login, getUser, logout, getToken, isAuthenticated }
})
