<template>
  <div class="container mt-4">
    <h1>Departments</h1>
    <div class="container mt-4">
      <div class="row">
        <department-form />
        <department-list />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import DepartmentForm from '@/components/DepartmentForm.vue'
import { useDepartmentStore } from '@/stores/department'
import DepartmentList from '../components/DepartmentList.vue'
import { useCompanyStore } from '../stores/company'
import { onMounted } from 'vue'

const companyStore = useCompanyStore()
const departmentStore = useDepartmentStore()

onMounted(async () => {
  await departmentStore.fetchDepartments()

  await companyStore.fetchCompanies()
})
</script>
