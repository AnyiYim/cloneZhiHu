from __future__ import unicode_literals
# Create your models here.


from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=50)
    head = models.FileField(upload_to='./upload/')
    objects = models.Manager()

    def __unicode__(self):
        return self.name


# debug TypeError: __init__() missing 1 required positional argument: 'on_delete'
# 在 ForeignKey 方法添加 on_delete=models.CASCADE
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    content = models.TextField()
    release_date = models.DateField()

    def __unicode__(self):
        return self.title


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,)
    content = models.TextField()
    release_date = models.DateField()

    def __unicode__(self):
        return self.content


class Collections(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE,)
    collectionname = models.CharField(max_length=50)
    release_date = models.DateField()

    def __unicode__(self):
        return self.collectionname
