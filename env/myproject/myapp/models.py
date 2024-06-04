from django.db import models

class contact(models.Model):
    pname=models.CharField(max_length=200)
    mail=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    def __str__(self):
        return self.pname