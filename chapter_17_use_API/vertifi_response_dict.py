import requests
import urllib3


urllib3.disable_warnings()
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers, verify=False)


print(f"Status code:{r.status_code}")

response_dict = r.json()
print(len(response_dict))
print(type(response_dict))


keys = []
for key in response_dict:
    keys.append(key)
print(keys[:10])

keys = list(response_dict)
# 原理： 当你对字典直接使用 list() 时，Python 会自动“遍历这个字典的键”，并把它们收集到一个列表里。你不需要写 for 循环，也不需要 append。
keys = list(response_dict.key())
# 字典自带一个 keys() 方法，它返回一个“视图对象”（一个类似集合的、含有所有键的东西）。你只需要用 list() 把它“固化”成实体列表即可。
print(keys[:10])
