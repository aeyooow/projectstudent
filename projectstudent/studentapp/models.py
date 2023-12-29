from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(BaseModel):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    student_id = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False, choices=GENDER)
    email = models.EmailField(max_length=100, null=False, blank=False)
    
