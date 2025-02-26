import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface ToastMessage {
  id: number
  type: 'success' | 'error'
  message: string
}

export const useToastStore = defineStore('toast', () => {
  const toasts = ref<ToastMessage[]>([])
  let idCounter = 0

  const addToast = (type: 'success' | 'error', message: string) => {
    const toast = { id: idCounter++, type, message }
    toasts.value.push(toast)
    setTimeout(() => removeToast(toast.id), 3000)
  }

  const removeToast = (id: number) => {
    toasts.value = toasts.value.filter((toast) => toast.id !== id)
  }

  return { toasts, addToast, removeToast }
})
