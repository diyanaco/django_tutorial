from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    favorite_quote = models.CharField(max_length=500)
    date_created = models.DateTimeField('date created', default=datetime.now())

    def __str__(self):
        return f'User id : %d; name : %s; favorite_quote : %s;' % (self.id, self.name , self.favorite_quote)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)