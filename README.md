# Django 投票系统

这是一个使用 Django 框架开发的简单投票系统。

## 功能特点

- 创建投票问题
- 为每个问题添加多个选项
- 用户可以进行投票
- 查看投票结果
- 支持重新投票

## 安装说明

1. 克隆仓库：
```bash
git clone [你的仓库URL]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行数据库迁移：
```bash
python manage.py migrate
```

4. 创建示例数据：
```bash
python manage.py create_sample_polls
```

5. 启动开发服务器：
```bash
python manage.py runserver
```

6. 访问 http://127.0.0.1:8000/polls/ 开始使用

## 技术栈

- Python 3.x
- Django 5.0
- SQLite3 