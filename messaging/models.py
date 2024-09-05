from django.db import models
from django.conf import settings
from listings.models import Listing
 

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='sent_messages', 
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='received_messages', 
        on_delete=models.CASCADE
    )
    listing = models.ForeignKey(
        Listing, 
        related_name='messages', 
        on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Message from {self.sender} to {self.receiver} about {self.listing}"