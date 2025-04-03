from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 问题文本
    pub_date = models.DateTimeField('date published')  # 发布时间

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 关联到问题
    choice_text = models.CharField(max_length=200)  # 选项文本
    votes = models.IntegerField(default=0)  # 票数

    def __str__(self):
        return self.choice_text