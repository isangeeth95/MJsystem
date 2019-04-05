from django.db import models

# Create your models here.

class Staff(models.Model):
    Emp_ID = models.CharField(max_length=255,blank=False)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone_Number = models.IntegerField()
    Admission_date = models.DateField()
    Job_title = models.CharField(max_length=255)
    Job_level = models.CharField(max_length=255)




    def __str__(self):
        return 'Emp_ID : {0} First_Name : {1}   Last_Name : {2} '.format(self.Emp_ID, self.First_Name ,self.Last_Name)



# Create your models here.
