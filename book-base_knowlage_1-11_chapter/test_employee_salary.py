# from employee_salary import Employee

# def test_give_default_raise():
#     employee_01 = Employee("mike", "bordon", 10000)
#     # employee_01.give_raise()
#     #不要调用，一调用，结果就变成了 self.annual_salary +=5000=15000
#     assert employee_01.give_raise() == 15000
#     #断言又一次调用，就又加一次： self.annual_salary=15000+5000=2000


# from employee_salary import Employee

# def test_give_coustom_raise():

#     employee_02 = Employee("hhh", "jtjhh", 10000)
#     # employee_02.give_raise(2000)
#     assert employee_02.give_raise(2000) == 12000

# 两个问题：
# 1，实例对象创建在测试函数外，如果传入测试函数当参数，将被pytest视为夹具：
# #pytest 会“抢走”你定义的变量，并试图把它当成一个“夹具（fixture）”来加载。
# 在 pytest 中，测试函数的参数名（如 employee_01）会被自动解释为一个“夹具（fixture）”的名称。
# pytest 会去查找一个同名的 @pytest.fixture 函数，找不到就会报 fixture not found。
# 所以，你定义的全局变量 employee_01 被 pytest 无视了，因为它只认夹具（fixture）。

# 2,不要多次调用类方法：employee_01.give_raise(),因为原类规定了，每次调用都返回类属性：self.annual_salary.
# 多次调用，就多次叠加


from employee_salary import Employee
import pytest

@pytest.fixture
def employee():
    """创建一个 Employee 实例供测试使用"""
    return Employee('sofeiya', 'luolan', 10000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 15000


def test_give_custom_raise(employee):
    employee.give_raise(2000)
    assert employee.annual_salary == 12000