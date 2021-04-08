# 购号网： http://xx.gouhaowang.cn/m/shoujihaoduan/search
import re
import time

import requests
from bs4 import BeautifulSoup


class GouHaoWang:

    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                                          "Chrome/89.0.4389.90 Safari/537.36"

    def index(self):
        """
        获取cookie
        :return:
        """
        self.sess.get("http://xx.gouhaowang.cn/m/shoujihaoduan")

    def get_page_count(self, number_seg):
        resp = self.search(number_seg, 1)
        ref = re.findall("个号段 1/(\d+) 页", resp)
        return ref[0] if ref else 1

    def search(self, number_seg, page_number):
        url = f"http://xx.gouhaowang.cn/m/shoujihaoduan/search/so/{number_seg}/type/0/p/{page_number}.html"
        resp = self.sess.get(url=url)
        return resp.text

    def get_info(self, number_seg):
        self.index()
        infos = []
        for page_number in range(2, int(self.get_page_count(number_seg)) + 1):
            resp = self.search(number_seg, page_number)
            soup = BeautifulSoup(resp, "html.parser")
            infos.extend([[td.text for td in tr.find_all("td")[1:4]] for tr in soup.find_all('tr')][1:])
            time.sleep(1)
        return infos
