# 导入包
import re
import requests
import os

import urllib3.exceptions

fill_path = "./视频"
# 首先在当前目录下创建文件夹
try:
    if os.path.exists(fill_path):
        print("视频文件夹已存在")
    else:
        os.mkdir('./' + '视频')
except urllib3.exceptions.NewConnectionError as e:
    print("以存在无法写入文件")
# 获得链接地址(从ts文件)
# fangao.stboda.com/concat/20220309/a51097bc349c44c9adb995c580d8e6b7/cloudv-transfer/5555555502sp828o5556s2654n0o03p1_71a8b076384f4161b5d9282b446c4c7b_0_3
url = 'http://imeiju.pro/ckplayerx/m3u8.php'
data = {
    #       https://fangao.stboda.com/concat/20220309/58d9d100dc4444dfbf044e566ca95d25/cloudv-transfer/555555550p97sso55556s26580no03p1_7979344d40ca496aba0f7281d0a8625f_0_3.m3u8
    'url': 'https://fangao.stboda.com/concat/20220309/58d9d100dc4444dfbf044e566ca95d25/cloudv-transfer/555555550p97sso55556s26580no03p1_7979344d40ca496aba0f7281d0a8625f_0_3.m3u8',
    'f': 'ck_m3u8'
}
# 伪装Python脚本
head = {
    'Host': 'imeiju.pro',
    'Referer': 'http://imeiju.pro/js/player/rrm3u8.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

# 得到播放链接的主页面的文本文件
m3u8_html = requests.get(url=url, params=data, headers=head)

# 使用正则表达式来筛选
m3u8_link = re.findall("url: '(.*?)'", m3u8_html.text)[0]

# 爬取子页面的数据
m3u8_sub = requests.get(url=m3u8_link)

# 获得视频链接的片段
ts_text = re.sub('#E.*', '', m3u8_sub.text).split()

# 拿取所有片段视频
for ts_link in ts_text:
    ts_all_link = 'https://fangao.stboda.com/concat/20220309/58d9d100dc4444dfbf044e566ca95d25/cloudv-transfer/' + ts_link
    content_ts = requests.get(url=ts_all_link).content
    with open('./' + '视频/{1}.mp4', 'ab') as fill:
        fill.write(content_ts)
    print('正在爬取片段' + ts_link)
print('爬取视频完成！')
