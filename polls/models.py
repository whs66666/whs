from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 问题文本
    pub_date = models.DateTimeField('date published')  # 发布时间

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 关联到问题
    choice_text = models.CharField(max_length=200)  # 选项文本
    votes = models.IntegerField(default=0)  # 票数

    def __str__(self):
        return self.choice_text