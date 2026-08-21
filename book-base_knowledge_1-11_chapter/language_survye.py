# 写一个需要测试的类

# import sys
# from pathlib import Path


from survey import AnonymousSurvey

"""定义一个问题，并创建一个表示调查的AnonymouseSurvey对象"""
question = "what language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# 显示问题并存储答案：
language_survey.show_question()
"""显示问题，或问卷"""
print("enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()