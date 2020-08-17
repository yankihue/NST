from django.db import models
import datetime
from django.utils import timezone
from taggit.managers import TaggableManager
import uuid
from django.utils.timezone import now

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()  - datetime.timedelta(days=1)   

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=250)
    published = models.DateField(auto_now_add=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=100,default=uuid.uuid1)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',default='')
    name = models.CharField(max_length=80,default='')
    email = models.EmailField(default='')
    body = models.TextField(default='')
    created_on = models.DateTimeField(default=now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

