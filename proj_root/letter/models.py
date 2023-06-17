from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Letter(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    send_to = models.EmailField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    ending = models.CharField(max_length=50)
    date_to_send = models.DateField()
    submitted = models.DateField(auto_now_add=True)

    
    def get_absolute_url(self):
        return reverse_lazy('letter', kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ['submitted']
        
        
    def __str__(self):
        return f"""
            First Name={self.first_name};
        """
        
class LetterUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField("User Email",  unique=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    