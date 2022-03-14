# -* coding=gbk  *-
# -* coding:utf-8 *-
# @Author: Sammie
# @SoftWare: PyCharm


import requests
import json

word = input("请输入要翻译的文字:")  # 输入函数，返回str类型
url = 'https://fanyi.baidu.com/sug'  # 封装网页链接
Form_data = {'kw': word}  # 设置一个字典来保存输入的文字

# header = {'User-agent': 'Googlebot'}  # 浏览器头部的信息

# post方式请求网站
response = requests.post(url=url, data=Form_data)  # 使用requests的post方法，里面的参数第一个为网页的链接，第二个为输入的文字的字典，第三个为网页头部的信息
# 以 JSON 格式返回的，因此需要引入内置库 json 来解析
content = json.loads(response.text)  # 解析json文件，结果保存在content这个变量里面,对应的是dumps，这个是把Python对象编码成JSON格式的字符串

result = content['data']  # 获取翻译结果
# print(result)

for item in result:
    print(item["k"], item["v"])
