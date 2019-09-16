import datetime
from django.db import models
from django.utils import timezone

class UsersAnswers(models.Model):
    question_id = models.IntegerField()
    account_id = models.IntegerField()
    created_date= models.DateTimeField()

    def __str__(self):
        return self.question_text

class UserAnswerList(models.Model):
    UsersAnswers = models.ForeignKey(UsersAnswers, on_delete=models.CASCADE)
    answer_id = models.IntegerField()
    created_date= models.DateTimeField()
    
    def __str__(self):
        return self.choice_text
