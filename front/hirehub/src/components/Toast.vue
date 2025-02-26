<template>
  <div class="toast-ccontainer">
    <div v-for="toast in toasts" :key="toast.id" :class="['toast-message', `toast-${toast.type}`]">
      {{ toast.message }}
      <button @click="toastStore.removeToast(toast.id)" class="btn-cclose">×</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useToastStore } from '../stores/toast'
import { storeToRefs } from 'pinia'

const toastStore = useToastStore()
const toasts = storeToRefs(toastStore).toasts
</script>

<style scoped>
.toast-ccontainer {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1000;
}

.toast-message {
  padding: 10px 20px;
  border-radius: 4px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-width: 200px;
  margin-bottom: 5px;


}

.toast-success {
  background-color: #28a745;
}

.toast-error {
  background-color: #dc3545;
}

.btn-cclose {
  background: none;
  border: none;
  color: white;
  font-size: 16px;
  cursor: pointer;
}
</style>
