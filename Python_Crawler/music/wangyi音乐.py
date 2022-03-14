import re
import execjs
import requests


'''解析界面，不参加代码运行'''
o_url = 'https://music.163.com/#/song?id={id}'

n_url = 'https://music.163.com/song/media/outer/url?id={id}'

'''-----------------'''

url = 'https://music.163.com/discover/toplist'
response = requests.get(url)
# print(response.text)
# re解析数据
song_list = re.compile('<li><a href="/song\?id=(?P<id>.*?)">(?P<name>.*?)</a></li><li>', re.S)
# 找到所有返回结果当中的所有字符
result_song = song_list.finditer(response.text)
# 拿到属于name组的字符和id组的字符
for song in result_song:
    # print(song.group("name"))
    print(song.group("id"))

# jiami = open('网页JS加密文件.js', 'r', encoding='utf-8').read()
# jiemimusic = execjs.compile(jiami)
# for song in song_list:
#     fin_reu = jiemimusic.call('start', song[0])
#     print(fin_reu)
