from django.urls import path
from . import views

app_name = 'polls'  # 添加应用命名空间

urlpatterns = [
    path('', views.index, name='index'),  # 这将处理 /polls/ 路径
    path('<int:question_id>/', views.detail, name='detail'),  # 处理问题详情
    path('<int:question_id>/results/', views.results, name='results'),  # 处理结果页面
    path('<int:question_id>/vote/', views.vote, name='vote'),  # 处理投票
]