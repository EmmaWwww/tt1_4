from django.db import models

# Create your models here.
# fieldName & datatype

# Scheduled Transaction
class Transaction(models.Model):
    TransactionId = models.CharField(max_length=200)
    AccountID = models.CharField(max_length=200)
    ReceivingAccountID = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    TransactionAmount = models.CharField(max_length=200)
    Comment = models.CharField(max_length=200)

#https://docs.djangoproject.com/en/2.0/ref/models/fields/#model-field-types
