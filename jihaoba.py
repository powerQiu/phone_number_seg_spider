# https://m.jihaoba.com/haoduan
import time

import requests
from bs4 import BeautifulSoup


class JiHaoBa:

    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) " \
                                          "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 " \
                                          "Safari/604.1 "
    
    def get(self, url):
        return self.sess.get(url, timeout=20)

    def index(self):
        self.get("https://m.jihaoba.com/tools/haoduan/")

    def get_url(self, number):
        resp = self.get(url=f"https://m.jihaoba.com/haoduan/{number}/")
        soup = BeautifulSoup(resp.text, "html.parser")
        uls = soup.find_all("ul", attrs={"class": "city_lst"})
        return [f'https://m.jihaoba.com{li.find("a")["href"]}' for ul in uls for li in ul.find_all("li")]

    def search(self, url):
        resp = self.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        print(resp.text)
        uls = soup.find_all("ul", attrs={"class": "city-hd city-hd-nei"})
        return [[li.text for li in ul.find_all("li")][:3] for ul in uls]

    def get_info(self, number):
        self.index()
        urls = self.get_url(number)
        infos = []
        print(urls)
        for url in urls:
            infos.extend(self.search(url))
            time.sleep(1)
        return infos


if __name__ == '__main__':
    jhb = JiHaoBa()
    jhb.index()
    print(jhb.get_url(190))
    print(jhb.search("https://m.jihaoba.com/haoduan/190/anshan.htm"))
