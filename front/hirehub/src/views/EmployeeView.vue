<template>
  <div class="container mt-4">
    <h1>Employees</h1>
    <employee-form />
    <employee-list />
  </div>
</template>

<script setup lang="ts">
import EmployeeForm from '../components/EmployeeForm.vue'
import EmployeeList from '../components/EmployeeList.vue'
import { useEmployeeStore } from '../stores/employee'
import { onMounted } from 'vue'

const employeeStore = useEmployeeStore()

onMounted(async () => {
  await employeeStore.fetchEmployees()
})
</script>
