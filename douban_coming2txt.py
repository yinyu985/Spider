"""
需求：抓取豆瓣电影即将上映的电影
1.http://movie.douban.com/coming
2.构建请求头（伪装成浏览器，发送请求）
3.利用request模块，发送网络请求，获取响应对象
4.从响应对象中，利用lxml提取html中的电影数据
5.Xpath 语法
6.将数据写入到CSV文件
"""

import time

# 构建一个爬虫类
import requests
from lxml import etree


class DoubanSpider(object):

    def __init__(self):  # 构建请求头
        self.url = "http://movie.douban.com/coming"
        self.headers = {  # User-Agent:用户标识
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
                          "Referer: https://movie.douban.com/"
            # Referer: 标识是从哪个网页跳转过来的
        }

    @property
    def send_request(self):  # 发送请求
        time.sleep(2)  # 睡眠两秒钟防止IP被封
        response = requests.get(url=self.url, headers=self.headers)
        return response

    def parser_response(self, response):  # 解析请求对象
        html = response.content.decode()
        # print(html)
        # 打印测试
        eroot = etree.HTML(html)
        tr_list = eroot.xpath('//div[@class="article"]//tr')[1:]
        # 遍历提取
        for tr in tr_list:
            # 上映时间
            # strip()去掉字符串前后空格
            time = tr.xpath('./td[1]/text()')[0].strip()

            # 电影名称
            name = tr.xpath('./td[2]/a/text()')[0].strip()

            # 电影类型
            type = tr.xpath('./td[3]/text()')[0].strip()

            # 播放地区
            area = tr.xpath('./td[4]/text()')[0].strip()

            # 期待人数
            number = tr.xpath('./td[5]/text()')[0].strip()

            # 将每一部电影装到字典中

            text = ("{:<10}""{:^30}""{:^20}""{:^20}""{:>30}".format(time, name, type, area, number))
            fp = open("/Users/beauty/Desktop/豆瓣电影.txt", "a", encoding="utf8")
            fp.write(text+"\n")

    def run(self):
        response = self.send_request
        self.parser_response(response)


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
