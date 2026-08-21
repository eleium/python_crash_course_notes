# python中函数与方法的异同点：

# 比较维度	               函数（Function）	                 方法（Method）
# 定义位置	          在模块（.py 文件）中独立定义	     在类（class） 内部定义
# 调用方式	          直接通过函数名调用：func()	     通过实例或类调用：obj.method() 或 Class.method(obj)
# 第一个参数	      没有特殊要求，按需定义	         通常有 self（指向实例本身），由 Python 自动传入
# 所有权	          不属于任何对象，属于模块	         属于某个类或实例

# ✅ 用代码看清楚
# 1. 函数（独立定义）
# 定义在模块顶层，不属于任何类
def greet(name):
    return f"Hello, {name}"


# 直接调用
print(greet("Alice"))  # Hello, Alice


# 2. 方法（定义在类内部）
class Person:
    def __init__(self, name):
        self.name = name

    # 这是一个实例方法（method）
    def say_hello(self):
        return f"Hello, {self.name}"


# 调用方法：必须先创建实例，通过实例调用
p = Person("Bob")
print(p.say_hello())  # Hello, Bob


# 3. 方法本质上也是函数，只是被绑定到了对象


class Person:
    def say_hello(self):
        return "Hello"


# 通过类调用，手动传入 self
print(Person.say_hello(None))  # Hello（但通常不这样用）

# 通过实例调用，self 自动传入
p = Person()
print(p.say_hello())  # Hello


#  两者相同的地方
# 都是可调用对象：它们都可以用 () 来调用。

# 都可以接受参数：都可以定义参数，支持位置参数、关键字参数、默认值等。

# 都可以返回值：都可以用 return 返回结果。

# 都可以被装饰：函数和方法都可以用 @decorator 装饰。

# 📌 一个重要的判断方法
# 你可以用 type() 来区分：


def my_func():
    pass


class MyClass:
    def my_method(self):
        pass


obj = MyClass()

print(type(my_func))  # <class 'function'>
print(type(obj.my_method))  # <class 'method'>


#  一句话总结
# 函数是独立的代码块，不属于任何对象；
# 方法是定义在类内部的函数，属于类或实例，并且会自动接收 self 作为第一个参数。
# 它们本质上都是“可调用对象”，只是绑定关系不同。


# 它们的使用形式都是 ： 方法是对象名.方法名(),比如： name.upper()方法，list_name.pop()方法，
# 而函数是把对象放到后面的print(name)、sorted(car_list)，函数名在前面。

# ✅ 你的总结完全正确
# 类型	             调用形式	          示例
# 方法	            对象.方法名()	      name.upper()
# list_name.pop()
# scores.get('math')
# 函数	             函数名(对象)	      print(name)
# sorted(car_list)
# len(my_list)

# 为什么会有这种区别？
# 方法是“属于”某个对象的，它必须知道自己是属于哪个具体实例的（所以要有 self），因此调用时是 对象.方法()，对象在前面。

# 函数是“独立”的，它不隶属于任何对象，它接收什么数据由参数决定，因此调用时是 函数(对象)，对象作为参数传进去。

# 🧪 对照示例

# 方法：对象在前，方法在后
name = "hello"
print(name.upper())  # HELLO

my_list = [1, 2, 3]
my_list.append(4)  # 方法：列表对象.append(元素)
print(my_list)  # [1, 2, 3, 4]

# 函数：函数名在前，对象作为参数
print(len(my_list))  # 函数：len(对象)
print(sorted(my_list))  # 函数：sorted(对象)


# 📌 一个特例：type()
# type() 是一个内置函数，但你可能会写成：
print(type(123))  # <class 'int'> → 函数在前，对象作为参数
# 它符合你总结的规律。

# 📌 一句话总结
# 你的总结完全正确：调用形式是“方法：对象.方法名()”，而“函数：函数名(对象)”。这是区分方法和函数最直观的方式。


# 前面还涉及到了语句，del name[0],  del与 name之间没有.,
# 这个del语句的结构是：‘ 删除’ ‘对象’那个的‘属性’，
# 其他语句也如此吗？

# 你观察得非常敏锐，而且理解完全正确！

# del 是 Python 的语句（statement），它和函数或方法有本质区别。

# 🎯 核心区别
# 语法单元	        调用形式	                                      示例
# 函数	           函数名(对象)	                                  print(name)、len(list)
# 方法	           对象.方法名()	                             list.pop()、str.upper()
# 语句	          关键字 + 目标，没有括号，没有点号	             del name[0]、if、for、import
# 你的发现完全正确：del 与 name 之间没有 .，也没有 ()，这是语句的典型特征。

# 📝 常见语句（也是 Python 核心语法）
# 语句类型	示例
# 赋值语句	x = 10
# 删除语句	del name[0]、del person.age
# 条件语句	if x > 0: ...
# 循环语句	for i in range(10): ...
# 导入语句	import math
# 返回语句	return result
# 异常处理	try: ... except: ...


# 🧪 对比验证

# 1. 语句（statement）—— 没有括号，没有点号
name = ["a", "b", "c"]
del name[0]  # ✅ 删除语句
print(name)  # ['b', 'c']

# 2. 方法（method）—— 有点号，有括号
name.remove("b")  # ✅ 方法调用
print(name)  # ['c']

# 3. 函数（function）—— 没有点号，有括号
print(len(name))  # ✅ 函数调用


# 📌 一个易混淆点：del 与 pop() 的区别
# 操作	类型	能否获取被删除的值
# del name[0]	语句	❌ 不能，直接删除，无返回值
# name.pop(0)	方法	✅ 能，返回被删除的元素


# 📌 一句话总结
# 你的观察完全正确：del 是语句，没有 . 也没有 ()，它直接作用于目标对象。
# Python 中还有 if、for、import、return 等语句，它们的结构都是“关键字 + 目标”，不依赖点号或括号

# del 是 Python 中的删除语句，它不局限于列表，也不局限于方法调用，所以它的语法是 del + 目标，
# 目标可以是变量、属性、列表元素、字典键等。

# 📌 一句话总结
# del 是语句，不是方法，所以它不需要 () 来传参，而是直接跟要删除的目标。
# name_list[0] 是“索引操作”（语法），del 作用于这个目标，所以写成 del name_list[0]。

# pop() 是方法，需要在对象上调用，所以写成 name_list.pop(0)。
# 两者本质不同：一个是“删除”，一个是“调用方法删除并返回”。

# del name_list[2]中，name_list[2]是一个整体。被del 删除。


# 返回新对象的是函数，不是方法。这是两者的区别吗？
# ✅ 你的理解大部分是对的
# “原地修改的方法，大多返回 None”：你猜得完全正确。
# 比如 list.sort()、list.append()、list.reverse()，它们都是直接修改列表，然后返回 None。

# “返回新对象的是函数，不是方法”：这个说法有例外，但总体规律是对的。

# 📌 1. 返回新对象的，不一定是“函数”
# 你观察到的 sorted() 是个函数，它返回新列表。但有一个重要的例子也是“返回新对象”，它却是方法：list.copy()。

cars = ["宝马", "奔驰", "奥迪"]
new_cars = cars.copy()  # 这是一个方法，但它返回新列表
# 所以，“返回新对象”不是函数的专利，方法也可以。

# 📌 2. 真正的区别：在于“会不会修改原对象”
# 这才是区分的关键，也是 Python 的一条设计准则：

# 类型	               会不会修改原对象	        返回值	          示例
# 原地修改方法	        ✅ 会	              None	            list.append()、list.sort()、list.reverse()
# 返回新对象的方法	    ❌ 不会	               新对象	         list.copy()、str.upper()
# 返回新对象的函数	    ❌ 不会	               新对象	         sorted()、reversed()
# 所以，sorted() 是函数，list.copy() 是方法，但它们的共同点是“不修改原对象，返回新对象”。

# 📌 3. 为什么会有这个规律？
# 这背后是 Python 的一个核心思想：“在修改对象和返回新对象之间做明确区分”。

# 如果你想修改对象，就用 list.sort()（返回 None）。
# 如果你想保留原对象、得到一个新版本，就用 sorted() 或 list.copy()。
# 这种设计让你一眼就能看出代码的行为：看到 list.sort()，你知道原列表会被改变；看到 sorted()，你知道原列表不会被改变。

# 📌 4. 那“函数”和“方法”到底区别在哪？
# 回到你最初的问题：“返回新对象的是函数，不是方法”——这个说法不完全对，因为 list.copy() 就是一个返回新对象的方法。
# 但它的核心规律是对的：函数是独立的，方法是属于对象的。

# 类型	        调用形式	        是否属于对象
# 函数	        sorted(cars)	   ❌ 不属于任何对象
# 方法	        cars.copy()	       ✅ 属于列表对象
# 📌 一句话总结
# “原地修改的方法返回 None”是正确的。
# 但“返回新对象的是函数”不准确，因为 list.copy() 也是一个返回新对象的方法。
# 真正的区别在于：方法属于对象，函数独立于对象；而是否修改原对象，取决于设计意图，而不是它是函数还是方法。**
