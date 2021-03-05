from django.db import models
from django.urls import reverse
# Create your models here.

#MASTER TABLE
class courses_master(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    duration=models.CharField(max_length=20)
    fees=models.IntegerField()
    op=(
        ('Active','Active'),
        ('Inactive','Inactive')
    )
    status=models.CharField(max_length=50,choices=op)


    def get_absolute_url(self):
        return reverse('courses_list')

    def __str__(self):
        return   f"Couse Name:{self.name}"

class student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    father_firstname=models.CharField(max_length=50)
    father_secondname=models.CharField(max_length=50)
    father_lastname=models.CharField(max_length=50)
    Building_name=models.CharField(max_length=50)
    state_name=models.CharField(max_length=50)
    area_name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    ph_number=models.CharField(max_length=11)
    ph_number_house=models.CharField(max_length=11)
    birthdate=models.DateField()
    choice=(
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(max_length=10,choices=choice)
    Schoolname=models.CharField(max_length=50)
    education=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='Profile Pic')
    email=models.EmailField()
    inquiry_id=models.CharField(max_length=50)

    def __str__(self):
        return f"First name:{self.first_name}"
class timetable(models.Model):
    start_time=models.TimeField()
    end_time=models.TimeField()
    date=models.DateField()
    choice=(
        ('Active','Active'),
        ('Inactive','Inactive')
    )
    remarks=models.CharField(max_length=10,choices=choice,default='Active')

    def __str__(self):
        return f"Date:{self.date}"


class addmission(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE,related_name='addmission')
    course=models.ForeignKey(courses_master,on_delete=models.CASCADE,related_name='addmission')
    time_table=models.ForeignKey(timetable,on_delete=models.CASCADE,related_name='time_table',default=1)
    #payment=models.ForeignKey(payment,on_delete=models.CASCADE,related_name='addmission',default=3)


    def __str__(self):
        return f"addmission:{self.student.first_name}"



class payment(models.Model):
    receipt_id=models.CharField(max_length=50)
    receipt_date=models.DateField()
    amount=models.IntegerField()
    choice=(
        ('Cash','Cash'),
        ('Check','Check'),
        ('Card','Card')
    )
    type=models.CharField(max_length=20,choices=choice)
    ch_no=models.IntegerField(blank=True)
    bank_name=models.CharField(max_length=100,blank=True)
    branch_name=models.CharField(max_length=100,blank=True)
    payment_date=models.DateField()
    admission=models.ForeignKey(addmission,on_delete=models.CASCADE,related_name='adm',default=1)

    def __str__(self):
        return f"Receipt_ID:{self.receipt_id}"

class attendance(models.Model):
    date=models.DateField()
    time=models.TimeField()
    Choices=(
        ('Yes','Present'),
        ('No','Absent')
        )
    presence=models.CharField(max_length=50,choices=Choices)
    remarks=models.CharField(max_length=50,blank=True)
    time=models.TimeField()
    admission=models.ForeignKey(addmission,on_delete=models.CASCADE,related_name='attendance')
