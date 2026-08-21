#测试文件的名称一定以test开头。用pytest测试的时候，它将去查找test开头的文件。
#因此，这个单元格应该命名为： test_name_function.py

from name_function import get_formatted_name
#导入要被测试的函数


#写一个测试函数：
def test_first_last_name():
    """能够正确的处理 Janis joplin 这样的姓名吗？"""
    #测试函数必须以test开头。
    #测试函数应该比典型的函数名字更长，更具描述性，让测试人员清楚的知道测试的是哪些行为。
    
    formatted_name=get_formatted_name('janis','joplin')
    #调用被测试函数
    assert formatted_name== 'Janis.Joplin'
    #断言：声称满足特定的条件： 生成formatted_name的值是'Janis Joplin'.

#用pytest测试这个文件（包含测试函数）,在终端输入命令：pytest,它会自动搜寻以test开头的文件，然后测试以test开头的函数：