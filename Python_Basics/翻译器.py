# -* coding=gbk  *-
# -* coding:utf-8 *-
# @Author: Sammie
# @SoftWare: PyCharm


import requests
import json

word = input("������Ҫ���������:")  # ���뺯��������str����
url = 'https://fanyi.baidu.com/sug'  # ��װ��ҳ����
Form_data = {'kw': word}  # ����һ���ֵ����������������

# header = {'User-agent': 'Googlebot'}  # �����ͷ������Ϣ

# post��ʽ������վ
response = requests.post(url=url, data=Form_data)  # ʹ��requests��post����������Ĳ�����һ��Ϊ��ҳ�����ӣ��ڶ���Ϊ��������ֵ��ֵ䣬������Ϊ��ҳͷ������Ϣ
# �� JSON ��ʽ���صģ������Ҫ�������ÿ� json ������
content = json.loads(response.text)  # ����json�ļ������������content�����������,��Ӧ����dumps������ǰ�Python��������JSON��ʽ���ַ���

result = content['data']  # ��ȡ������
# print(result)

for item in result:
    print(item["k"], item["v"])
