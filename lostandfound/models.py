from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    date_reported = models.DateTimeField(auto_now_add=True)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    image = models.CharField(max_length=255)
    additional_information = models.TextField(blank=True)
    is_resolved = models.BooleanField(default=False)

    
