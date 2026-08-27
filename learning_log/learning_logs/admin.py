from django.contrib import admin

# Register your models here.

# 注册你的模型
from .models import Topic,Entry

# models.py前面的. 表示在同一级目录里面寻找models.py文件
admin.site.register(Topic)

admin.site.register(Entry)

