from django.db import models

# Create your models here.
class Letter(models.Model):
    send_to = models.EmailField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    ending = models.CharField(max_length=50)
    submitted = models.DateField(auto_now_add=True)

    
    class Meta:
        ordering = ['-title']
        
    def __str__(self):
        return self.title