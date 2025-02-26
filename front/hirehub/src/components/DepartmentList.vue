<template>
  <!-- List Section -->
  <div class="col-md-6 mt-4 mt-md-0">
    <div class="card p-3 shadow">
      <h3 class="text-center">Department List</h3>
      <ul class="list-group">
        <li
          v-for="depart in departments"
          :key="depart.id"
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          <div>
            <strong>{{ depart.name }}</strong
            ><br />
            <small>Employees: {{ depart.employee_count }}</small>
          </div>
          <div v-if="isLoggedIn">
            <button @click="deleteDepartment(depart.id)" class="btn btn-danger btn-sm">
              Delete
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">

import { useAuthStore } from '@/stores/auth'
import { useDepartmentStore } from '../stores/department'
import { storeToRefs } from 'pinia'

const isLoggedIn = storeToRefs(useAuthStore()).token
const departmentStore = useDepartmentStore()
const departments = storeToRefs(departmentStore).departments

const deleteDepartment = (id?: number) => {
  if (id) departmentStore.removeDepartment(id)
}
</script>
