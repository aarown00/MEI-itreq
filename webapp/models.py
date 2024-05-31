from django.db import models
from django.contrib.auth.models import User


class IT_Request(models.Model):
    # Helper function to generate choices
    def generate_choices(*args):
        return [(arg, arg.capitalize()) for arg in args]

    # Constants for choices
    EQ_TYPE_CHOICES = generate_choices('Desktop', 'Laptop', 'Others')
    ISSUE_CHOICES = generate_choices('Software', 'Hardware', 'Network')
    STATUS_CHOICES = generate_choices('Requested', 'Ongoing', 'Completed')

    # Model fields
    eq_name = models.CharField(max_length=100)
    eq_type = models.CharField(max_length=10, choices=EQ_TYPE_CHOICES, default='Desktop')
    department = models.CharField(max_length=100)
    requested_at = models.DateTimeField(auto_now_add=True)
    issue = models.CharField(max_length=10, choices=ISSUE_CHOICES, default='Software')
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Requested')
    #Foreign Model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} - {self.user.last_name} - {self.issue} - {self.status} "