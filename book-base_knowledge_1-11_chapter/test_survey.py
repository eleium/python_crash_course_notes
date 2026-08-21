# 编写一个测试AnonymousSurvey类的程序：
# 验证如果用户在面对调查问题时，只提供一个答案，这个答案也能被存储。
# 这个程序的名字应该命名为： test_survey.py

from survey import AnonymousSurvey


# def test_store_single_response():
#     """测试单个答案会被妥善的存储"""
#     question = "what language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     # 创建实例

#     language_survey.store_response("english")
#     # 实例对象调用类中的存储方法，并传递参数：english-->new_response.新的回复回答

#     assert "english" in language_survey.responses


def test_store_three_response():
    """测试三个答案都会被存储"""
    question = "what language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)

    responses = ["english", "spanish", "mandarin"]
    # 这个列表是为了测试而写的，不是程序真正input的。
    # 只要从这个列表中验证成功，就可以说，类AnonymousSurvey的相关方法测试成功
    #这个列表的名字responses有迷惑性。跟实例对象的属性self.responses名字重合了。
    for response in responses:
        language_survey.store_response(response)
        #把得到的response答案都储存到self.responses,也就是这个实例的属性
    for response in responses:
        assert response in language_survey.responses
        #断言每一个response 都出现在实例的属性responses中。其实断言了三次


# 上面每次测试类的一个方法，都要创建一个实例对象和参数question.
# 重复的代码显得复杂，使用 夹具(fixture)，创造一个通用的测试环境
# 使用装饰器，创建一个夹具(fixture)，搭建测试环境，可以供多个测试使用。

import pytest
#使用了其中定义的一个装饰器，所以需要导入

@pytest.fixture
def language_survey():
    """一个可以供所有测试函数使用的AnonmousSurvey实例"""
    question='what language did you first learn to speak?'
    language_survey=AnonymousSurvey(question)
    return language_survey

def test_store_single_responses(language_survey):
    language_survey.store_response('english')
    assert 'english' in language_survey.responses

def test_store_three_responses(language_survey):
    responses=['english','spanish','mandarin']
    for response in responses:
        language_survey.store_response(response)
    for i in responses:
        assert i in language_survey.responses