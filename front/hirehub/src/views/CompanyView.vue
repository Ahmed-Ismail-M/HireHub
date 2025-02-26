<template>
  <div class="container mt-4">
    <h1>Companies</h1>
    <div class="container mt-4">
      <div class="row">

        <company-form />
        <company-list />
      </div></div>
  </div>
</template>

<script setup lang="ts">
import CompanyForm from '../components/CompanyForm.vue'
import CompanyList from '../components/CompanyList.vue'
import { useCompanyStore } from '../stores/company'
import { onMounted } from 'vue'

const companyStore = useCompanyStore()
onMounted(async () => {
  await companyStore.fetchCompanies()
})
</script>
