<template>
      <div class="col-md-6">
        <div class="card p-3 shadow">
          <h3 class="text-center">Create Company</h3>
          <form @submit.prevent="handleSubmit">
            <div class="mb-3">
              <label class="form-label">Company Name</label>
              <input v-model="company.name" type="text" class="form-control" required />
            </div>
            <button type="submit" class="btn btn-primary w-100">Add Company</button>
          </form>
        </div>
      </div>

</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useCompanyStore } from '../stores/company'
import { storeToRefs } from 'pinia'

const company = ref({ name: '' })
const companyStore = useCompanyStore()

const companies = storeToRefs(companyStore).companies

const handleSubmit = async () => {
  companyStore.addCompany(company.value)
  company.value = { name: '' }
}
onMounted(async () => {
  await companyStore.fetchCompanies()
})
</script>
