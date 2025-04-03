from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice

class Command(BaseCommand):
    help = '创建示例投票数据'

    def handle(self, *args, **kwargs):
        # 创建第一个投票
        q1 = Question.objects.create(
            question_text="你最喜欢的编程语言是什么？",
            pub_date=timezone.now()
        )
        q1.choice_set.create(choice_text="Python", votes=0)
        q1.choice_set.create(choice_text="Java", votes=0)
        q1.choice_set.create(choice_text="JavaScript", votes=0)
        q1.choice_set.create(choice_text="C++", votes=0)

        # 创建第二个投票
        q2 = Question.objects.create(
            question_text="你平时使用什么操作系统？",
            pub_date=timezone.now()
        )
        q2.choice_set.create(choice_text="Windows", votes=0)
        q2.choice_set.create(choice_text="macOS", votes=0)
        q2.choice_set.create(choice_text="Linux", votes=0)

        # 创建第三个投票
        q3 = Question.objects.create(
            question_text="你最常用的代码编辑器是？",
            pub_date=timezone.now()
        )
        q3.choice_set.create(choice_text="Visual Studio Code", votes=0)
        q3.choice_set.create(choice_text="PyCharm", votes=0)
        q3.choice_set.create(choice_text="Sublime Text", votes=0)
        q3.choice_set.create(choice_text="Vim", votes=0)

        self.stdout.write(self.style.SUCCESS('示例投票创建成功！')) 