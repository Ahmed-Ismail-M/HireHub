from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from datetime import date


class User(AbstractUser):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    role = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @property
    def department_count(self):
        return self.departments.count()

    @property
    def employee_count(self):
        return self.employees.count()


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('company', 'name')

    def __str__(self):
        return f"{self.name} ({self.company.name})"

    @property
    def employee_count(self):
        return self.employees.count()


class Employee(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated'),
        ('on_leave', 'On Leave')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    mobile_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^[0-9]+$', message="Mobile number must contain only digits.")]
    )
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True)

    def clean(self):
        if self.department and self.company and self.department.company != self.company:
            raise ValidationError("The selected department does not belong to the selected company.")

    def days_employed(self):
        if self.hired_on:
            return (date.today() - self.hired_on).days
        return None
    
    @property
    def full_name(self):
        return self.user.get_full_name()
    
    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.designation}"

    def save(self, *args, **kwargs):

        self.full_clean() 
        super().save(*args, **kwargs)