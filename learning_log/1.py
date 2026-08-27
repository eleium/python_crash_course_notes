# Django是个啥？


# **Django** 是一个非常强大、非常受欢迎的 **Python Web 框架（Web Framework）**。
# 通俗地说：**如果你用纯 Python 写一个网站，你需要自己处理很多繁琐的事（比如处理网址、数据库、用户登录等）。
# 而 Django 就是一套帮你把这些事**全部做好的**“超级工具箱”**。

# 我帮你用最直白的方式把它拆解清楚：
# ### 1. 到底什么是“框架”？

# 比喻：你想盖一栋房子。
# 如果你什么工具都没有，你需要自己搬砖、和水泥、做窗户……累死累活。
# 如果你用 **Django**，就像租了一个**“豪华建筑队”**。
# 地皮、砖头、水泥、蓝图都给你准备好了，你只需要喊“我要盖个三室一厅”，他们就能帮你搞定大部分工作，你只需要做一些个性化的装修。

#  2. Django 能帮你做什么？（它的四大绝招）

# | 绝招                         | 具体功能                                               | 你手动做有多痛苦 |

# | **1. 路由（URL）**           | 管理你网站的网址（比如 `yoursite.com/posts/`）         | 你要自己写一堆 `if...else` 判断用户访问了哪个网址 |
# | **2. 数据库**                | 管理用户数据（比如博客文章、用户账号）                 | 你要自己写复杂的 SQL 语句去存储和查找数据 |
# | **3. 后台管理**              | 自带一个超级好用的“网站管理员后台”                     | 你要花几天时间自己写一个 |
# | **4. 用户认证**              | 处理登录、注册、密码加密、权限管理                     | 涉及安全，极其复杂，容错率低 |

#  3. 为什么全世界那么多人都爱用它？

# *   **极其高效**：你想做一个博客、论坛、电商网站，用 Django 可能只需要几小时，而纯手写可能需要几个月。
# *   **极其安全**：它是久经考验的，比如防止黑客攻击（SQL 注入、跨站脚本攻击）的防护措施都已经内置好了。
# *   **“大而全”**：它自带超多功能，所以你不需要到处找第三方插件，所有工具都有（这比另一个流行的 Flask 框架要“重”，但也更省事）。

#  4. 结合你正在学的《Python编程：从入门到实践》第 18 章

# 你即将进入的第 18 章，就是 **“Web 应用程序（Django）”**。在那一章里，你会：
# 1. 用 Django 创建第一个项目。
# 2. 写一个简单的“学习笔记”网站（用户可以写笔记、查看笔记、登录、管理）。
# 3. 接触 Django 的 **Model（模型）**、**View（视图）**、**Template（模板）** 等核心概念。

# ### 📝 总结一句话：

# > **Django 就是你用 Python 建网站时，那个能帮你搞定 90% 杂活的“超级万能工具箱”。** 它让你从一个“只会写代码的人”变成一个“能发布网站的人”。

# **你准备好开始搭这个工具箱了吗？** 如果准备好了，我们就开始解决第 18 章的“环境创建”问题，你离学会做自己的第一个网站只差一步了！🚀


# manage.py 到底是什么？

# manage.py 是 Django 创建项目时自动生成的一个“总指挥文件”。
# 它存放了你项目所在的文件夹路径。
# 它里面写着一条极其关键的命令：DJANGO_SETTINGS_MODULE 环境变量（告诉 Django 你的项目配置文件在哪）。
# 它就像一个“门户”，只有通过它，你才能和你的 Django 项目对话。

# 为什么不能用 import 来使用它？
# 因为 import 是用来导入“库/模块（Module）”的，但 manage.py 是一个“脚本（Script）”。
# 我们打一个非常直观的比喻：
# 你想写一个 Python 函数（库/模块）来：比如你写的 alien_invasion.py，它是一个纯代码文件，你可以写 import alien_invasion，然后用里面的类。
# 你想“执行一个动作”：比如跑一个 python manage.py migrate，这就好比你在命令行里“下命令”，让 Django 这个系统去“执行数据库迁移”。
# 这个“执行动作”的权限，只掌握在 manage.py 这个“总指挥”手里。

# 总结：
# import 用于导入“模块（写得像工具箱一样的东西）”，而 python manage.py 命令 用于“执行（下命令）”。
# manage.py 是一个“总指挥”脚本，它在你用 python manage.py 时，才会被唤醒。
# import 去导入它的话，只会得到一个毫无意义的空壳。
# 以后看到 python xxx.py 命令 这种格式，你记住：这是 Python 脚本在执行“命令”，而不是在“导入”工具！

# migrate: 迁徙的意思
# **`migrate`** 翻译成中文是：**“迁移”**（动词 / 名词）。

# 在 Django（和很多 Web 框架）里，`migrate` 是一个极其核心的技术术语，但它**完全不是你想的“把代码从这里搬到那里”的意思**。

# ### 1. 什么是“数据库迁移（Database Migration）”？—— 最通俗的解释
# 想象一下：
# *   你刚搭好网站的**数据库**，它是一张**空表格**（比如“学习笔记表”）。
# *   你后来修改了代码，想在表格里**加一个“日期”列**，或者**删掉一个“分类”列**。
# *   如果你手动去数据库软件（比如 SQLite 或 MySQL）里改表格，那会很麻烦，而且容易出错。

# **Django 的 `migrate` 就是帮你“自动修改表格”的工具！**

# **它的作用是：把你在 Python 代码里写好的“数据模型（Model）”，同步到真实的数据库表格中。**
# *   如果你在代码里定义了一个“用户”模型，`migrate` 就会在数据库里真正创建一张叫“用户”的表格。
# *   如果你在代码里给“用户”加了一个字段（比如“电话”），`migrate` 就会在表格里加上“电话”这一列。

#  2. 为什么叫“迁移（Migration）”？—— 术语背后的秘密

# 因为数据库的结构**“从旧状态变成了新状态”**，这就像是发生了一次“结构上的迁移”：
# *   旧的表格结构（比如只有名字和密码） ➡️ **迁移** ➡️ 新的表格结构（加了头像、电话等）。
# *   Django 会为每一次这种“结构改变”**生成一个编号的迁移文件**（存放在 `migrations` 文件夹里），就像一个“结构变更记录表”。
# 执行 `migrate`，就是把这些“变更记录”真正应用到数据库上。

#  3. 与 `manage.py` 一起理解
# 当你执行 `python manage.py migrate` 时：
# 1. **`manage.py`**（总指挥）：告诉 Django ，“我要开始执行命令了”。
# 2. **`migrate`**（命令）：我命令你，把数据库的表格结构更新成代码里写好的样子。

# ### 4. 你即将要做的事（预习一下）

# 在第 18 章里，你会经历：

# python manage.py makemigrations learning_logs   # 第1步：根据你的代码，生成“变更记录文件”
# python manage.py migrate                         # 第2步：执行所有“变更记录”，真正修改数据库

# *   **`makemigrations`**：只做“计划”，在纸面上写下“我要怎么改表格”。
# *   **`migrate`**：真正施工！把纸面上的计划应用到真正的数据库里。

# ### 📝 总结一句话：
# > **`migrate` = “自动修改数据库结构”，让你不需要手写复杂的 SQL 语句。只要改变你的 Python 代码，它就会帮你把数据库更新到最新状态。**
# **以后看到 `migrate`，你的脑子里就要浮现出四个字：“同步数据表”**。你马上就会亲手体验这个魔法了！🚀

# 与 git 及其相似。

# 第一次运行 python manage.py migrate,初始化数据库：
# 那你自己定义的数据表，什么时候建？
# 你不用担心！第一次 migrate 只是打造地基。等到你接下来：
# 写代码：定义你的专属模型（比如 Topic，代表学习笔记的一个主题）。
# python manage.py makemigrations：把你的代码变化写成“计划书”。
# 再次 python manage.py migrate：把计划书应用到数据库，此时你的专属表格（比如 learning_logs_topic）才真正被建立。

# 建立web框架，创建一个project项目的步骤：

# 1，建立一个文件夹，也就是一个项目的根目录。这里叫learning_log文件夹。
# 2，进入该文件夹，然后创建虚拟环境：python -m venv project_venv
# 3,激活虚拟环境： project_venv/Scripts/activate
# 4,激活虚拟环境之后，要先安装python的web框架： pip install django
# 5,创建项目：django-admin startproject project .
# 产生 manage.py文件 和project文件夹，project文件夹下，有： __init__.py  asgi.py   settings.py    urls.py   wsgi .py  文件。
# 关于 asgi.py 和 wsgi.py（你只列了文件名，没提区别）

# wsgi.py：同步服务器入口（传统部署，如 Nginx + uWSGI）
# asgi.py：异步服务器入口（支持 WebSocket、长连接）

# （这个“点”（.）非常非常重要！它代表“在当前文件夹里直接创建项目”，这样你的项目结构会非常干净，所有文件都平铺在同一个文件夹里。
# 如果你不加这个点，Django 会额外创建一个子文件夹，导致项目嵌套太深，后续管理会非常麻烦。）

# 6,初始化数据库（新建数据库）python manage.py migrate 生成数据库：db.sqlite3
# db ：data base : 是“数据库”的简称，sqlite3 是它用的文件格式。这个文件就是你把表格、数据、密码等所有东西“存进去”的地方。
# sqlite3:是一个轻量化的数据库。
# 7,初次运行服务器： python manage.py runserver
# 以上是搭建web框架，并创建一个project项目的必要步骤，后续就可以在这个框架内，添加、丰富内容了。

# 典型的django项目文件夹内容：
"""
learning_log/                    <-- 项目根目录（你的“家”）
│
├── manage.py                    <-- ✅ 总控制台（在这里跑命令）
│
├── ll_project/                  <-- ✅ 存放配置（只有 settings.py, urls.py 等）
│
├── learning_logs/               <-- （看你刚刚创建了什么）应用文件夹
│
├── ll_venv/                     <-- ✅ 虚拟环境
│
├── db.sqlite3                   <-- ✅ 数据库（由 migrate 生成）
│
└── 1.py                         <-- 你的练习文件
"""

"""
# 1. 创建应用
python manage.py startapp learning_logs  创建一个叫learning_logs的app,一个应用

# 2. 编写模型：打开 learning_logs/models.py，定义类 Topic
# （包括 text 和 date_add 字段）

# 3. 登记应用：打开根目录下的 settings.py，在 INSTALLED_APPS 里添加 'learning_logs'

# 4. 生成迁移计划：
python manage.py makemigrations learning_logs
# 完成后，会生成一个 0001_initial.py 文件（这就是数据库结构的“图纸”）

# 5. 执行迁移：
python manage.py migrate
# 这个动作会把图纸上的结构，真正同步到数据库表里
"""


# Django管理网站：
# 1，创建超级用户
# cd learning_log  -->python manage.py createsuperuser 填写管理员名字和密码。这里用ll_admin当作管理员的名字

# 向管理网站注册模型
# 创建pyton manage.py startapp learning_logs时，在models.py模块的目录中，还创建了一个admin.py的文件。
# 顾名思义，admin.py 是有关管理员的内容

# 要保证runserver 在运行，才能访问django的网页。如果没有，在虚拟环境中，重新python manage.py runserver

# 用刚才的admin注册名： ll_admin 和密码登录

# 添加主题
# 向管理网站注册Topic后，可以添加第一个主题了。
# Topic 是一个“类”，Topic 类 = 一张空白的 Excel 表格模板。
# 但它的本质是“一张数据库表格的设计图纸，在写下text和date_add时，Topic会自动变成数据库learning_logs_topic的表的两个列：
# text：这一列用来存你的学习主题（比如：“Python”、“Django 入门”）。
# date_add：这一列自动记录你是什么时候创建这个主题的。

# 用网站的Topic下的add，添加两个主题：Chess_国际象棋 和 Rock Climb_攀岩

# 定义模型Entry
# 把Entry 的模型，放入models.py中
# 每次修改完Entry,就可以 ： (1),创建可迁徙文件： python manage.py makemigrations    (2),迁徙文件： python manage.py migrate

# 新的子文件entry创建好了之后，就可以在管理网站中添加这个子文件Entry的text了。 text框内这次没有文字限制了。max_lenght=200.

# 完成上面的添加Entry之后，可以进入django的shell:
# python manage.py shell 进入一个交互环境：from learning_logs.models import Topic先从learning_logs app中导入Topic,
# Topic.objects.all() 显示这个Topic文件袋里面的所有内容，即 查询集。这个查询集可以像列表一样被遍历。

# topics=Topic.objects.all()
# for topic in topics:
#     print(topic.id,topic)
#--->1 pythn
#    2 Chess_国际象棋
#    3 Rock_Climbing_攀岩

#得到各个entry 的topic(主题对象) 的id.

# #你的目的	推荐写法	优点
# 只想看名单（有几个人，叫什么）	                 print(topics)	                            速度快，直接看全局
# 想深入分析或查看属性（比如每个人的 text）        	for topic in topics: print(topic)	        能把每一个人分开来检查

#用列表推导式来获取属性：
# topics = Topic.objects.all()
# # 方式一：使用列表推导式（最优雅）
# print([topic.text for topic in topics])

# # 方式二：甚至可以直接用 .values_list()
# print(topics.values_list('text', flat=True))
#“变扁（Flat）”： 把原本的“二维（嵌套的）”结构，压成了“一维（平铺的）”结构。



#用Topic.objects.get()方法获取该对象，并查看其属性：

#先把Topic.objects.get()赋值给一个变量： t=Topic.objects.get(id=2)
#仅限 shell 调试，生产环境慎用，因为如果id=2不存在，就会崩溃。
#调用属性： t.text    t.date_add

#查看与主题相关联的条目。
#前面给模型Entry 定义了一个属性：topic,是一个外键ForeignKey,用来将条目和主题关联起来。


#获取与特定主题相关联的所有条目：
#还是在shell 下：
#t.entry_set.all()
#将显示：<QuerySet [<Entry: The opening is the first part of the game,roughly ...>, <Entry: In the opening phase of the game,it's important to...>]>
#这是关于Chess_国际象棋的两个entry的text.指向了同一个主题：Chess_国际象棋
#Django的用法，一个描述符。用models.py 中的Entry类（一个主题）的小写加下划线加set.all()的形式，获得与同一个主题相关联的条目。

#entry_set 的本质不是 Django 的“特殊语法”，而是 Python 的“描述符协议”在 ORM 中的落地。
# 等复习高阶时，我会用 Django 的 ForeignKey 反推描述符的实现原理