import re
import time
import urllib.request

from bs4 import BeautifulSoup

x = re.compile(r'<a href="(.*?)"<em>')
y = re.compile(r"<span>(.*?)<em>")


def ask(url):
    head = {
        "User-Agent": r"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36"
    }
    req = urllib.request.Request(url, headers=head)
    h = urllib.request.urlopen(req)
    return h


def jiexi():
    url = "https://s.weibo.com/top/summary"
    html = ask(url)
    soup = BeautifulSoup(html, "html.parser")
    for i in soup.find_all("ul", class_="list_a"):
        data = []
        i = str(i)
        y1 = re.findall(y, i)
        data.append(y1)
        fp = open("/Users/beauty/Desktop/微博热搜.txt", "w", encoding="utf8")
        t = time.strftime("%Y.%m.%d  %H：%M：%S", time.localtime())
        fp.write(t + "\n")
    for i in range(len(data[0])):
        s1 = str(data[0][i])
        fp = open("/Users/beauty/Desktop/微博热搜.txt", "a", encoding="utf8")
        fp.write(str(i + 1) + "=>")
        fp.write(s1 + "\n")


if __name__ == '__main__':
    jiexi()
