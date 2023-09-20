from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100,null=False)
    usn = models.CharField(max_length=100,blank=False)
    age = models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    