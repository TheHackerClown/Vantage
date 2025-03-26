from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_person = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField()

class Branch(models.Model):
    company_ref = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.TextField()
    pf_no = models.BigIntegerField()#check length
    pf_group_code = models.BigIntegerField()#check length
    pf_office = models.TextField()
    esic_no = models.BigIntegerField()#check length
    esic_group_code = models.BigIntegerField()#check length
    esic_office = models.TextField()


class Designation(models.Model):
    name = models.CharField(max_length=20)

class Department(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    company_ref = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_ref = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
    principle_employer = models.CharField(max_length=50)
    contractor_name = models.CharField(max_length=50)
    contractor_address = models.TextField()
    
    sub_contractor_name = models.CharField(max_length=50)
    sub_contractor_address = models.TextField()
    
    main_contractor_name = models.CharField(max_length=50)
    main_contractor_address = models.TextField()
    
    esic_no = models.BigIntegerField()#check length
    esic_group_code = models.BigIntegerField()#check length
    esic_office = models.TextField()


class Employee(models.Model):
    cust_id = models.TextField()
    
    name = models.CharField(max_length=50)
    father_husband_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    designation = models.ForeignKey(Designation,on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    company_ref = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    regular = models.BooleanField(default=True)
    
    salary_type = models.CharField(max_length=50)#check types
    
    epf = models.BooleanField(default=True)
    pension = models.BooleanField(default=True)
    edli = models.BooleanField()
    esi = models.BooleanField(default=True)
    
    epf_non_regular = models.BooleanField(default=False)
    esi_non_regular = models.BooleanField(default=False)
    
    pf_limit_employee = models.IntegerField(default=6500)
    pf_limit_employer = models.IntegerField(default=6500)
    
    esi_limit_employee = models.IntegerField(default=7500)
    esi_limit_employer = models.IntegerField(default=7500)

    pf_number = models.TextField() #check
    
    nssn = models.TextField() #check

    esi_number = models.TextField() #check

    dispensary = models.TextField()

    reason_of_quit = models.CharField(max_length=50) # check types

    marital_status = models.CharField(max_length=20) # check types

    sex = models.CharField(max_length=10) # check types

    #dates
    date_of_birth = models.DateField()
    date_of_left = models.DateField()
    date_of_joining = models.DateField()
    date_of_retire = models.DateField()
    date_of_pf = models.DateField()
    date_of_esic = models.DateField()
    age = models.IntegerField()
    inc_month = models.IntegerField()


    def __str__(self):
        return f"{self.name} working at {self.company_ref.name} with post {self.designation}"
    



class Payment(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    company_ref = models.ForeignKey(Company,on_delete=models.CASCADE)  