from django.db import models

# Create your models here.
class BankDetails(models.Model):
    Trans_ID = models.CharField(max_length=255,blank=False)
    Trans_Date = models.DateField()
    Bank_Name = models.CharField(max_length=255)
    Bank_Branch = models.CharField(max_length=255)
    Amount = models.FloatField()
    Withdraw_or_Deposit= (
        ('W', 'Withdraw'),
        ('D', 'Deposite'),
    )
    Withdraw_or_Deposit= models.CharField(max_length=100, choices=Withdraw_or_Deposit, blank=False)
    Trans_Type =(
        ('Online','Online'),
        ('Cheque','Cheque'),
        ('At Bank','At Bank'),

    )
    Trans_Type = models.CharField(max_length=100, choices=Trans_Type, blank=False)

    Transfer_Details = models.CharField(max_length=255)





    def __str__(self):
        return ' Trans_ID: {0} : Trans_Date {1}    '.format(self.Trans_ID, self. Trans_Date )

