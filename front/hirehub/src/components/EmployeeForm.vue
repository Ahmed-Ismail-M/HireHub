<template>
  <form @submit.prevent="submitForm">
    <div class="mb-3">
      <label>Email</label>
      <input v-model="employee.email" type="email" class="form-control" required />
    </div>
    <div class="mb-3">
      <label>Password</label>
      <input v-model="employee.password" type="password" class="form-control" required />
    </div>
    <div class="mb-3">
      <label>First Name</label>
      <input v-model="employee.first_name" type="text" class="form-control" required />
    </div>
    <div class="mb-3">
      <label>Last Name</label>
      <input v-model="employee.last_name" type="text" class="form-control" required />
    </div>
    <div class="mb-3">
      <label>Company</label>
      <select v-model="employee.company" class="form-control" required>
        <option v-for="comp in companies" :key="comp.id" :value="comp.id">
          {{ comp.name }}
        </option>
      </select>
    </div>
    <div class="mb-3">
      <label>Department</label>
      <select v-model="employee.department" class="form-control" required>
        <option v-for="dept in filteredDepartments" :key="dept.id" :value="dept.id">
          {{ dept.name }}
        </option>
      </select>
    </div>
    <div class="mb-3">
      <label>Mobile Number</label>
      <input v-model="employee.mobile_number" type="text" class="form-control" required />
    </div>
    <div class="mb-3">
      <label>Address</label>
      <textarea v-model="employee.address" class="form-control" required></textarea>
    </div>
    <div class="mb-3">
      <label>Designation</label>
      <input v-model="employee.designation" type="text" class="form-control" required />
    </div>
    <div class="mb-3">
      <label>Hired On</label>
      <div class="input-group">
        <input
          v-model="employee.hired_on"
          type="date"
          class="form-control"
          required
          :max="todayDate"
        />
      </div>
    </div>
    <div class="mb-3">
      <label>Status</label>
      <select v-model="employee.status" class="form-control" required>
        <option value="active">Active</option>
        <option value="inactive">Inactive</option>
        <option value="terminated">Terminated</option>
        <option value="on_leave">On Leave</option>
      </select>
    </div>
    <button type="submit" class="btn btn-primary">Register</button>
  </form>
</template>

<script setup lang="ts">
import { onMounted, ref, computed, watch } from 'vue'
import { useEmployeeStore } from '../stores/employee'
import { useCompanyStore } from '../stores/company'
import { useDepartmentStore } from '../stores/department'
import { storeToRefs } from 'pinia'

const employeeStore = useEmployeeStore()
const companyStore = useCompanyStore()
const departmentStore = useDepartmentStore()
const todayDate = new Date().toISOString().split('T')[0]
const employee = ref({
  email: '',
  password: '',
  first_name: '',
  last_name: '',
  company: { id: 0, name: '' },
  department: { id: 0, name: '', company: { id: 0, name: '' } },
  mobile_number: '',
  address: '',
  designation: '',
  hired_on: todayDate,
  status: 'active' as const,
})

const companies = storeToRefs(companyStore).companies
const departments = storeToRefs(departmentStore).departments

const submitForm = async () => {
  await employeeStore.addEmployee(employee.value)
  employee.value = {
    email: '',
    password: '',
    first_name: '',
    last_name: '',
    company: { id: 0, name: '' },
    department: { id: 0, name: '', company: { id: 0, name: '' } },
    mobile_number: '',
    address: '',
    designation: '',
    hired_on: todayDate,
    status: 'active' as const,
  }
}
const filteredDepartments = computed(() => {
  if (!employee.value.company) {
    return []
  }
  return departments.value.filter((dept) => dept.company === employee.value.company)
})

watch(
  () => employee.value.company,
  () => {
    employee.value.department = { id: 0, name: '', company: { id: 0, name: '' } }
  },
)

onMounted(async () => {
  await companyStore.fetchCompanies()
  await departmentStore.fetchDepartments()
})
</script>
