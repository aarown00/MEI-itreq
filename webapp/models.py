from django.db import models
from django.contrib.auth.models import User


class IT_Request(models.Model):
    # Constants for choices
    PC_TYPE_CHOICES = [
        ('desktop', 'Desktop'),
        ('laptop', 'Laptop'),
        ('tablet', 'Tablet'),
    ]

    ISSUE_CHOICES = [
        ('software', 'Software'),
        ('hardware', 'Hardware'),
        ('network', 'Network'),
    ]

    # Model fields
    PIC = models.CharField(max_length=100)  # Person In Charge
    PC_name = models.CharField(max_length=100)
    pc_type = models.CharField(max_length=10, choices=PC_TYPE_CHOICES, default='desktop')
    department = models.CharField(max_length=100)
    requested_at = models.DateTimeField(auto_now_add=True)
    issue = models.CharField(max_length=10, choices=ISSUE_CHOICES, default='software')
    description = models.TextField()


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.issue} - {self.user.first_name} - {self.user.last_name} - {self.user.username}"