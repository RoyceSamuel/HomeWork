import datetime
from django.db import models
from django.utils import timezone

class UsersAnswers(models.Model):
    question_id = models.IntegerField()
    question_text = models.CharField(max_length=200)
    account_id = models.IntegerField()
    answered_date= models.DateTimeField()
    def __str__(self):
        return self.question_text

class UserAnswerList(models.Model):
    UsersAnswers = models.ForeignKey(UsersAnswers, on_delete=models.CASCADE)
    question_id = models.IntegerField()
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

