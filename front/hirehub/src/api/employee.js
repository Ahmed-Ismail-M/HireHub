import api from './index'

export const registerEmployee = (data) => api.post('/register/', data)
export const loginEmployee = (data) => api.post('/login/', data)
export const getEmployees = () => api.get('/employees/')
export const getEmployee = (id) => api.get(`/employees/${id}/`)
export const updateEmployee = (id, data) => api.put(`/employees/${id}/`, data)
export const deleteEmployee = (id) => api.delete(`/employees/${id}/`)
