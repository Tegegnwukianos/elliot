from django.db import models

# Create your models here.


class bottleform(models.Model):
    dorm = models.CharField(max_length=255)
    campus= models.CharField(max_length=255)
    bottleNumber = models.IntegerField()

