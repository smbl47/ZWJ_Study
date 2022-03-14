import requests
import re
from lxml import etree
import os

# 得到当前文件的位置
dir_path = os.getcwd()
# 创建保存图片的文件夹
final_dir_path = os.path.join(dir_path, '壁纸')
# 判断文件夹是否生成
if not os.path.exists(final_dir_path):
    os.makedirs(final_dir_path)
else:
    print("保存的文件夹已经存在，将继续在此文件夹写入！！")

for page in range(1, 197):
    # 请求网站
    url = f'https://wallhaven.cc/toplist?page={page}'
    # 伪装
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    # 封装一个子链接的列表地址
    sub_url_list = []

    html_data = requests.get(url=url, headers=head)

    # 解析数据，使用xpath表达式
    sub_html_data = etree.HTML(html_data.text)

    result = sub_html_data.xpath('///div[@id="thumbs"]/section[@class="thumb-listing-page"]//li')

    for sub_data in result:
        sub_src = sub_data.xpath('./figure/a/@href')[0]
        sub_url_list.append(sub_src)

    # 获得子页面图片的源地址
    for sub_link in sub_url_list:
        # 访问子链接
        response = requests.get(sub_link, headers=head)
        small_data = response.text
        # 再次使用xpath解析
        small_data_x = etree.HTML(small_data)
        sub_result = small_data_x.xpath('///div[@class="scrollbox"]/img/@src')
        # 双层循环
        for po in sub_result:
            po_name = po.split('/')[-1]
            # 保存数据
            if os.path.exists(f'壁纸/{po_name}'):
                print("文件已经存在，自动跳过保存！！")
            else:
                html_img = requests.get(po).content
                with open(f'壁纸/{po_name}', mode='ab+') as f:
                    f.write(html_img)
                print("正在爬取：", po_name)
