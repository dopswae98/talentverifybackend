from django.db import models
from datetime import date

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    date_of_registration = models.DateField()
    company_registration_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    departments = models.TextField()
    # num_employees = models.IntegerField()
    num_employees = models.IntegerField()
    contact_phone = models.CharField(max_length=15)
    email = models.EmailField()
    # Add more fields as needed

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=255)
    employee_id_number = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    date_started = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    duties = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.name
    

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    marks = models.PositiveIntegerField(default=0)
    roll_number = models.PositiveIntegerField(default=0)
    section = models.CharField(max_length=50)
    # name = models.CharField(max_length=255, default='a')
    # date_of_registration = models.DateField(default=date)
    # company_registration_number = models.CharField(max_length=255, default='reg number')
    # address = models.CharField(max_length=255, default='address')
    # contact_person = models.CharField(max_length=255, default='person')
    # departments = models.TextField(default='a')
    # # num_employees = models.IntegerField()
    # num_employees = models.IntegerField(default=0)
    # contact_phone = models.CharField(max_length=15, default=0)
    # email = models.EmailField(default='a')

    def __str__(self):
        return self.first_name
    
# class Kompanies(models.Model):
#     # first_name = models.CharField(max_length=50)
#     # last_name = models.CharField(max_length=50)
#     # marks = models.PositiveIntegerField(default=0)
#     # roll_number = models.PositiveIntegerField(default=0)
#     # section = models.CharField(max_length=50)
#     name = models.CharField(max_length=255, default='a')
#     date_of_registration = models.DateField(default=date)
#     company_registration_number = models.CharField(max_length=255, default='reg number')
#     address = models.CharField(max_length=255, default='address')
#     contact_person = models.CharField(max_length=255, default='person')
#     departments = models.TextField(default='a')
#     # num_employees = models.IntegerField()
#     num_employees = models.IntegerField(default=0)
#     contact_phone = models.CharField(max_length=15, default=0)
#     email = models.EmailField(default='a')

#     def __str__(self):
#         return self.name