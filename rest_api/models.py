from django.db import models

# Create your models here.

class Employee(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique= True, db_index= True)
    department = models.TextField()
    name = models.TextField()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural =  'Employees'
    
    def __str__(self):
        return f'{self.name} works in {self.department}'