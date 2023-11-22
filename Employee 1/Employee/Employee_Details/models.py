from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    emp_id = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField()
    gender = models.CharField(max_length=25, blank=False, null=False)
    department = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.first_name
