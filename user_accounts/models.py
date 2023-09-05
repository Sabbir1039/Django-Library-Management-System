from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    USER_TYPE_CHOICE = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Staff', 'Staff'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICE, verbose_name='User Type')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    
    def __str__(self) -> str:
        return f"{self.user}"