from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    
    def full_name(self):
        return f"{self.last_name[0].capitalize()}. {self.first_name}"    
    
    def __str__(self):
        return self.full_name()