<template>
  <table class="table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Company</th>
        <th>Department</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="employee in employees" :key="employee.id">
        <td>{{ employee.id }}</td>
        <td>{{ employee.full_name }}</td>
        <td>{{ employee.email }}</td>
        <td>{{ employee.company }}</td>
        <td>{{ employee.department }}</td>
        <td>
          <button @click="deleteEmployee(employee.id)" class="btn btn-danger btn-sm">Delete</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { useEmployeeStore } from '../stores/employee'
import { storeToRefs } from 'pinia'
const employeeStore = useEmployeeStore()
const employees = storeToRefs(employeeStore).employees

const deleteEmployee = (id: number) => employeeStore.removeEmployee(id)
</script>
