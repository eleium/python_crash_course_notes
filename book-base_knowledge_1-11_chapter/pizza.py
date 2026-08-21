
def make_pizza(size,*toppings):
    print(f"\nMaking a {size} -inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
if __name__=="__main__":

    make_pizza(12,'moshroom','cheese')

#把函数调用make_pizza()变成if 条件语句里面的代码块，不再是顶层代码。这样被调用的时候，这个调用不会被执行。
#这是明确这个文件，或者说这个程序，这个函数是被当作模块来写的，所以用 if __name__=="__main__"