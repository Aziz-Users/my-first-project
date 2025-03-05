from django.db import models
from django.contrib.auth.models import User


class Transactions(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    uuid = models.CharField(max_length=1000, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(f'{self.uuid} - {self.user}')
    def update_status(self, new_status):

        if new_status in dict(self.STATUS_CHOICES).keys():
            self.status = new_status
            self.save()
        else:
            raise ValueError("Invalid status")