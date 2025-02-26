# HireHub Installation and API Documentation

## Installation and Setup

### Prerequisites
Ensure you have the following installed on your system:
- Python (>= 3.8)
- pip (Python package manager)
- virtualenv (optional but recommended)
- PostgreSQL or SQLite (default database)

### Step 1: Clone the Repository
```bash
$ git clone https://github.com/Ahmed-Ismail-M/HireHub.git
$ cd api/ems
```

### Step 2: Create and Activate a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
$ pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
$ python manage.py migrate
```

### Step 5: Create a Superuser
```bash
$ python manage.py createsuperuser
```
Provide the required details such as username, email, and password.

### Step 6: Run the Development Server
```bash
$ python manage.py runserver
```
The application will be accessible at `http://127.0.0.1:8000/`.

## API Documentation

### Base URL
```
http://127.0.0.1:8000/hirehub/api/v1/
```

### Authentication
This API uses Token-Based Authentication. Users must obtain a token and include it in the `Authorization` header with each request.

#### Obtain Token
```http
POST /hirehub/api/v1/login/
```
**Request Body (JSON):**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
**Response:**
```json
{
  "token": "your_auth_token"
}
```
Include the token in the header of subsequent requests:
```
Authorization: Token your_auth_token
```

### API Endpoints

#### 1. Companies
- **List all companies**
  ```http
  GET /hirehub/api/v1/companies/
  ```
- **Retrieve a company**
  ```http
  GET /hirehub/api/v1/companies/{id}/
  ```
- **Create a company**
  ```http
  POST /hirehub/api/v1/companies/
  ```
  **Request Body:**
  ```json
  {
    "name": "Company Name",
    "address": "Company Address"
  }
  ```

#### 2. Departments
- **List all departments**
  ```http
  GET /hirehub/api/v1/departments/
  ```
- **Retrieve a department**
  ```http
  GET /hirehub/api/v1/departments/{id}/
  ```
- **Create a department**
  ```http
  POST /hirehub/api/v1/departments/
  ```
  **Request Body:**
  ```json
  {
    "name": "Department Name",
    "company": 1
  }
  ```

#### 3. Employees
- **List all employees**
  ```http
  GET /hirehub/api/v1/employees/
  ```
- **Retrieve an employee**
  ```http
  GET /hirehub/api/v1/employees/{id}/
  ```
- **Create an employee**
  ```http
  POST /hirehub/api/v1/employees/
  ```
  **Request Body:**
  ```json
  {
    "name": "Employee Name",
    "department": 1
  }
  ```


This documentation provides all necessary steps to set up, run, and interact with the Django API using Token Authentication.

