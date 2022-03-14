import requests  # 第三方模块
import parsel
import os

# 得到当前位置的文件目录
dir_path1 = os.getcwd()
# 创建保存图片的文件夹
final_dir_path = os.path.join(dir_path1, '图片')
if not os.path.exists(final_dir_path):
    os.makedirs(final_dir_path)
else:
    print("保存的文件夹已经存在，将继续在此文件夹写入！！")


for ye in range(1, 112):
    # 得到目标网址
    url = f'https://www.kanxiaojiejie.com/page/{ye}'
    # 请求的方法
    response = requests.get(url)
    # 返回的结果，获取数据
    html_data = response.text
    # 解析数据，照片的详情页
    selector = parsel.Selector(html_data)

    link_url = selector.css('.entry-title a::attr(href)').getall()  # 获取所有子链接信息

    # 循环便利列表中的数据
    for link in link_url:
        resp = requests.get(link)
        sub_html = resp.text
        # 获取子页面的数据
        selector_1 = parsel.Selector(sub_html)
        # 获取图片链接
        img_list = selector_1.css('.entry.themeform p img::attr(src)').getall()
        print(img_list)
        # 向图片链接发送请求
        for img in img_list:
            # 图片名字
            img_name = img.split('/')[-1]
            # 保存数据
            if os.path.exists(f'图片/{img_name}'):
                print("文件已经存在，自动跳过保存！！")
            else:
                html_img = requests.get(img).content
                with open(f'图片/{img_name}', mode='ab+') as f:
                    f.write(html_img)
                print("正在爬取：", img_name)
