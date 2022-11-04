from unittest.util import _MAX_LENGTH
from django.db import models
 

class Blog(models.Model):
    title = models.fields.CharField(max_length=100) 
    description = models.fields.TextField(max_length = 1000)  
    
    def __str__(self) -> str:
        return self.title     
