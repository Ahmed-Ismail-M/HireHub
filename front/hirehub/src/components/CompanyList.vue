<template>
  <!-- List Section -->
  <div class="col-md-6 mt-4 mt-md-0">
    <div class="card p-3 shadow">
      <h3 class="text-center">Company List</h3>
      <ul class="list-group">
        <li
          v-for="comp in companies"
          :key="comp.id"
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          <div>
            <strong>{{ comp.name }}</strong
            ><br />
            <small
              >Departments: {{ comp.department_count }} | Employees:
              {{ comp.employee_count }}</small
            >
          </div>
          <div v-if="isLoggedIn">
            <button @click="deleteCompany(comp.id)" class="btn btn-danger btn-sm">Delete</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { useCompanyStore } from '../stores/company'
import { storeToRefs } from 'pinia'

const isLoggedIn = storeToRefs(useAuthStore()).token
const companyStore = useCompanyStore()
const companies = storeToRefs(companyStore).companies

const deleteCompany = (id?: number) => {
  if (id) {
    companyStore.removeCompany(id)
  }
}
</script>
