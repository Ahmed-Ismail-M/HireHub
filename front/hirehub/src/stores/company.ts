import { defineStore , storeToRefs } from 'pinia'
import { ref } from 'vue'
import type { Company } from '../types'
import { getCompanies, createCompany, deleteCompany } from '../api/company'
import { useToastStore } from './toast'
import handleError from '@/services/error_service'

export const useCompanyStore = defineStore('company', () => {
  const companies = ref<Company[]>([])
  const toast = useToastStore()

  const fetchCompanies = async () => {
    try {
      const response = await getCompanies()
      companies.value = response.data
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to fetch companies')
      toast.addToast('error', errorMessage)
    }
  }

  const addCompany = async (data: Partial<Company>) => {
    try {
      const response = await createCompany(data)
      companies.value.push(response.data)
      toast.addToast('success', 'Company registered successfully')
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to add company')
      toast.addToast('error', errorMessage)
      throw error
    }
  }

  const removeCompany = async (id: number) => {
    try {
      await deleteCompany(id)
      companies.value = companies.value.filter((emp) => emp.id !== id)
      toast.addToast('success', 'Company deleted successfully')
    } catch (error) {
      const errorMessage = handleError(error, 'Failed to delete company')
      toast.addToast('error', errorMessage)
    }
  }

  return { companies, fetchCompanies, addCompany, removeCompany }
})
