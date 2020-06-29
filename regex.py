"""
    regex.py
    re模块 功能函数演示
"""
import re


# 目标字符串
str01 = "Alex:1994,Sunny:1996"
# 正则表达式
pattern = r"(\w+):(\d+)"

# re 模块直接调用findall
list01 = re.findall(pattern,str01)
print(list01)

# complie 对象调用findall
regex = re.compile(pattern)
list02 = regex.findall(str01,0,12)
print(list02)

# 按照正则表达式匹配内容切割字符串
list03 = re.split(r"[:,]",str01)
print(list03)

# 替换目标字符串
str02 = re.sub(r":","-",str01,1)
print(str02)

# 替换目标字符串
str03 = re.subn(r":","-",str01)
print(str03)  # 显示替换了几个地方