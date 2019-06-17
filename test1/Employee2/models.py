from django.db import models

# Create your models here.
class emp(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=50)
