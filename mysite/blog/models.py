#coding = utf-8
from django.db import models
from django.contrib import admin
 
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
    class Meta:
        ordering = ('-timestamp',)
 
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'timestamp')
    

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
