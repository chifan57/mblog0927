from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    body = models.TextField()#不限制欄位
    pub_date = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ('-pub_date', ) 
        
    def __str__(self) -> str:
        return self.title
    