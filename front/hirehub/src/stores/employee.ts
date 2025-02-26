import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Employee } from '../types'
import { getEmployees, registerEmployee, deleteEmployee } from '../api/employee'
import { useToastStore } from './toast'
import handleError from '@/services/error_service'

export const useEmployeeStore = defineStore('employee', () => {
  const employees = ref<Employee[]>([])
  const toast = useToastStore()
  const fetchEmployees = async () => {
    try {
      const response = await getEmployees()
      employees.value = response.data
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to fetch employees')
      toast.addToast('error', errorMessage)
    }
  }

  const addEmployee = async (data: Partial<Employee>) => {
    try {
      await registerEmployee(data)
      fetchEmployees()
      toast.addToast('success', 'Employee registered successfully')
    } catch (error) {
    const errorMessage = handleError(error, 'Failed to add employees')
    toast.addToast('error', errorMessage);
    throw error;
    }
  }

  const removeEmployee = async (id: number) => {
    try {
      await deleteEmployee(id)
      employees.value = employees.value.filter((emp) => emp.id !== id)
      toast.addToast('success', 'Employee deleted successfully')
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to delete employees')
      toast.addToast('error', errorMessage)
      throw error
    }
  }

  return { employees, fetchEmployees, addEmployee, removeEmployee }
})
