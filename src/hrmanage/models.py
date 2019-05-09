from django.db import models

# Create your models here.

class Staff(models.Model):
    #Emp_ID = models.CharField(unique=True,max_length=255,blank=False)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    NIC = models.CharField(max_length=15)
    Email = models.CharField(unique=True,max_length=255)
    Phone_Number = models.IntegerField()
    Admission_date = models.DateField(auto_now=True)
    Job_title = models.CharField(max_length=255)
    Job_level = models.CharField(max_length=255)




    def __str__(self):
        return 'First_Name:{1}  Last_Name:{2} Email:{3} Phone_Number:{4} Admission_date:{5} Job_title:{6}  Job_level:{7} '.format(
            self.First_Name, self.Last_Name, self. Email, self.Phone_Number,self. Admission_date,self.Job_title,self. Job_level)

# Create your models here.
