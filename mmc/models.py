from django.db import models
from users.models import CustomUser

# Define the choices for the fitness group dropdown
FITNESS_GROUP_CHOICES = (
    ('Group A', 'Group A'),
    ('Group B', 'Group B'),
    ('Group C', 'Group C'),
    # Add more fitness group choices as needed
)

class Notification(models.Model):
    fitness_group = models.CharField(max_length=20, choices=FITNESS_GROUP_CHOICES)
    message = models.TextField()
    sent_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notifications')
    recipients = models.ManyToManyField(CustomUser, related_name='received_notifications')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.fitness_group}"

    class Meta:
        ordering = ['-timestamp']