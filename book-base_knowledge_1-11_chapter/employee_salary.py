class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_salary=""):
        if raise_salary=="":
            self.annual_salary += 5000
        else:
            self.annual_salary+=int(raise_salary)
        return self.annual_salary

e=Employee('kaka','joseph',10000)
print(e.give_raise())
#调用一次，结果是15000.这个结果以及存入self.annual_salary属性中。
print(e.give_raise(2000))
#再次调用，结果从15000+2000=17000，然后再次存入了self.annual_salary属性中。
#调用几次，叠加几次。