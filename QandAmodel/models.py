from django.db import models
from django.contrib.auth import authenticate, get_user_model
from authentication.models import User
from datetime import datetime
# from django.conf import settings
from django.db.models import DateTimeField
# from django.contrib.postgres.fields import ArrayField
User = get_user_model()
# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=list, null=True)
    # tags = ArrayField(models.CharField(max_length=200, unique=False, blank=True), unique=False, blank=True, default=list)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    
    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.title


#Creating the answer model

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'