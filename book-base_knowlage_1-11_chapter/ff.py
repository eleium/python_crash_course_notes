from pathlib import Path


path = Path("alice.txt")
contents = path.read_text(encoding='utf-8')
# contents 是一个全文的字符串
lines = contents.split()
# split(),默认以空格分割字符串，得到的是一个列表。也可以用任意的字符 'a','.'等。
# splitlines()默认以\n, \r\n、\r等转义符分割字符串，得到的也是一个列表。

# number = lines.count("the")
# print(number)


count_word = 0
for i in lines:
    if i == "the":
        count_word += 1
print(count_word)
