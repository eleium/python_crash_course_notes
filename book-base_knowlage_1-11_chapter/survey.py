# 写一个需要测试的类


class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    # survey:调查问卷

    def __init__(self, question):
        """存储一个问题，并未存储答案做准备"""
        self.question = question
        self.responses = []
        # response:回答，回复

    def show_question(self):
        """显示调查问卷,也就是要问的问题"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答案"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results: ")
        for response in self.response:
            print(f" - {response}")

