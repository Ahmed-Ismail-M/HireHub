<template>
  <div class="col-md-6">
    <div class="card p-3 shadow">
      <h3 class="text-center">Create Department</h3>
      <form @submit.prevent="handleSubmit">
        <div class="mb-3">
          <label class="form-label">Department Name</label>
          <input v-model="department.name" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label>Company</label>
          <select v-model="department.company" class="form-control" required>
            <option v-for="comp in companies" :key="comp.id" :value="comp.id">
              {{ comp.name }}
            </option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary w-100">Add Department</button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useDepartmentStore } from '../stores/department'
import { storeToRefs } from 'pinia'
import { useCompanyStore } from '@/stores/company'

const department = ref({ name: '', company: { name: '' } })
const departmentStore = useDepartmentStore()
const companyStore = useCompanyStore()
const companies = storeToRefs(companyStore).companies

const handleSubmit = async () => {
  departmentStore.addDepartment(department.value)
  department.value = { name: '', company: { name: '' } }
}
onMounted(async () => {
  await companyStore.fetchCompanies()
})
</script>
