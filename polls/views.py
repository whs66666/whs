from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Question, Choice

# 问题列表视图
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# 问题详情视图
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 获取指定问题，若不存在则返回404
    return render(request, 'polls/detail.html', {'question': question})

# 投票结果视图
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# 处理投票请求
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # 获取用户选择的选项
    except (KeyError, Choice.DoesNotExist):
        # 如果未选择选项，重新显示详情页面并提示错误
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "你没有选择任何选项。",
        })
    else:
        selected_choice.votes += 1  # 增加票数
        selected_choice.save()  # 保存到数据库
        # 重定向到结果页面
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))