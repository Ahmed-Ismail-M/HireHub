import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Department } from '../types'
import { getDepartments, createDepartment, deleteDepartment } from '../api/department'
import { useToastStore } from './toast'
import handleError from '@/services/error_service'

export const useDepartmentStore = defineStore('department', () => {
  const departments = ref<Department[]>([])
  const toast = useToastStore()

  const fetchDepartments = async () => {
    try {
      const response = await getDepartments()
      departments.value = response.data
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to fetch departments')
      toast.addToast('error', errorMessage)
    }
  }

  const addDepartment = async (data: Partial<Department>) => {
    try {
      const response = await createDepartment(data)
      departments.value.push(response.data)
      toast.addToast('success', 'Department registered successfully')
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to add department')

      toast.addToast('error', errorMessage)
      throw error
    }
  }

  const removeDepartment = async (id: number) => {
    try {
      await deleteDepartment(id)
      departments.value = departments.value.filter((emp) => emp.id !== id)
      toast.addToast('success', 'Department deleted successfully')
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to delete department')
      toast.addToast('error', errorMessage)
    }
  }

  return { departments, fetchDepartments, addDepartment, removeDepartment }
})
