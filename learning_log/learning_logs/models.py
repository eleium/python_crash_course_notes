from django.db import models

# Create your models here.


class Topic(models.Model):
    # 用户学习的主题
    # 创建名为 Topic 的类。它继承自 models.Model。
    # 在 Django 里，只要你继承 models.Model，这个类就会自动变成一个“数据库表”（表名通常叫 learning_logs_topic）。
    # Topic 代表一个“学习主题”（比如“Python 基础”、“Django 入门”）。
    text = models.CharField(max_length=200)
    # field: 字段 的意思。
    # models.CharField：这是一个短文本字段（相当于 Excel 表格里的一列文字）。
    # max_length=200：最多只能存 200 个字符（这保证了数据库不会无限膨胀）。
    date_added = models.DateTimeField(auto_now_add=True)
    # 定义另一个字段 date_add（记录这个主题创建的时间）。
    # models.DateTimeField：这是一个日期时间字段，用来存放日期和时间。
    # auto_now_add=True：这是一个“自动保存时间”的魔法参数。
    # 当你创建这个主题时，Django 会自动把这个时刻记下来，不需要你手动输入，而且以后更新它也不会改变

    def __str__(self):
        # 返回模型的字符串表示：
        # 这是一个魔法方法。
        # __str__ 告诉 Python：“当你用 print() 打印这个对象时，展示它的 text（主题名称）。”
        # 例如，你有一个叫“Python”的主题对象，打印它会直接显示 Python。
        # 这个魔法方法在 Django 后台管理界面里极其有用，能让管理员一眼看出这个条目代表什么。
        return self.text


# opic = 一个文件夹（主题）。
# Entry = 文件夹里的一张张具体笔记纸（条目）。
# 你可以为“Python”这个主题创建很多个 Entry，比如“今天学了函数”、“明天学了类”。
# opic 是“大分类”，Entry 是“大分类下面的一条具体笔记”。
# 如果你把 Entry 连接到你的 Topic（通过外键），你就能在 Django 里把这些具体的笔记按照你的学习主题整理得井井有条


class Entry(models.Model):
    # 学到的有关某个主题的具体知识：（models.Model)表示继承Django的基类Model的models类。
    # Entry： “条目”、“词条”、“记录”。也需要加入admin.py 去register一下才能起作用。
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # models.ForeignKey：告诉 Django，“我要在这张表里建立一个外键关系，把这两张表连起来。”
    # Topic：参数一，告诉 Django，“我要连接的目标是 Topic 这张表。”
    # on_delete=models.CASCADE：参数二，这是最关键的！它的意思是：“如果你删除了那个 Topic（主题），那么挂靠在它下面的所有 Entry（条目）也一并自动删除！”
    # CASCADE 是“级联删除”的意思。
    # 为什么这样设计？ 因为如果你删除了“Python”这个主题，那么里面的“列表推导式”、“函数”等笔记还有什么意义呢？它们都该一起消失。
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # Topic（主题） = 一个带标签的文件夹。
    # 文件夹上写着：text（名字）和 date_added（什么时候建的这个文件夹）。
    # Entry（条目） = 文件夹里的一张张笔记纸。
    # 每张笔记纸上写着：
    # text（具体内容）
    # date_added（这张纸是什么时候写下的）
    # auto_now_add:它永远只记录第一次创建的时间，不会随便变。多个Entry会有不同的时间戳。这个是自己的出生证明。
    # auto_add：以后每次修改内容时的时间，会变化。

    class Meta:
        # Meta 是英文单词 Metadata（元数据）的缩写。
        # 就是“关于数据的数据”。比如：这张表里的 text 是数据（内容），而表的名字、表里数据的排列方式、是否允许重复这些信息，就是“元数据”。
        # 当你在模型类里写一个 class Meta:，就等于告诉 Django：“我现在要开始设置关于这张表本身的属性了，而不是设置表里的具体字段。”
        verbose_name_plural = "entries"
        # verbose = 啰嗦的、详细的、冗长的。    verbose_name = “人性化、可读的名字”。
        # plural = 复数（语言学术语）。    verbose_name_plural = “复数的、人性化的名字”。
        #在后台菜单里，请用 entries 这个正确的英文复数来显示它，别用 Django 默认生成的 Entrys。

    def __str__(self):
        # 返回一个表示条目的简单字符串：
        return f"{self.text[:50]}..."
