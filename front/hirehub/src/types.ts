export interface Employee {
  id: number
  email: string
  full_name: string
  company: Company
  department: Department
  mobile_number: string
  address: string
  designation: string
  hired_on?: string
  days_employed?: number
  status: 'active' | 'inactive' | 'terminated' | 'on_leave'
}

export interface User {
  id?: number
  password?: string
  email: string
  first_name?: string
  last_name?: string
}
export type LoginUser = Pick<User, 'email'| 'id'>


export type RegisterUser = Pick<User, 'email'| 'password'>

export interface Company {
  id?: number
  name: string
  department_count?: number
  employee_count?: number
}

export interface Department {
  id?: number
  name: string
  company: Company
  employee_count?: number
}
