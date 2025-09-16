from django.db import models

class Transaction(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()
    account_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - ${self.amount}"
