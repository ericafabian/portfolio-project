from django.db import models

# Create blog model
class Blog(models.Model):
    title = models.CharField(max_length=25)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image  = models.ImageField(upload_to='images/')
    

# Add the the admin
