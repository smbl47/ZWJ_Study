import json
import urllib.request, urllib.error
import re


def main():
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    askURL(url)
    result = open('result.html', 'r', encoding='utf-8')
    # 正则表达式
    data = re.findall(r"\"engine_jds\":(.+?),\"jobid_count\"", str(result.readline()))
    print(data)


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"

    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()
