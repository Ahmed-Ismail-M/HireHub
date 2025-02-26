<template>
  <div class="container mt-4">
    <h1>Dashboard</h1>
    <div class="container mt-4">
      <div class="row">
        <company-list />
        <department-list />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useDepartmentStore } from '@/stores/department'
import CompanyList from '../components/CompanyList.vue'
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
