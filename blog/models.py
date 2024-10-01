#Define data modles (objects) for use in this blog application

from django.db import models

# Create your models here.
class Article(models.Model):
    '''Encapulates the data for a blog an Article by some Author'''

    #data attributes:
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text =  models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    
