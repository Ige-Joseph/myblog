from django.db import models
from datetime import datetime
# Create your models here.

class myBlogDdDefined(models.Model):
      PostName = models.CharField(max_length= 100)
      PostContent = models.CharField(max_length = 10000000)
      TimeCreated = models.DateTimeField(default=datetime.now, blank=True)
      
      
      


