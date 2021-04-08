# https://www.chahaoba.com/
import ssl
import time

import requests
from bs4 import BeautifulSoup
from urllib3 import poolmanager

from xiaoxiang import XiaoX


class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)


class ChaChaBa:
    
    def __init__(self, app_key="", app_secret=""):
        self.sess = requests.Session()
        self.sess.mount('https://', TLSAdapter())
        self.sess.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                                          "Chrome/89.0.4389.90 Safari/537.36"
        self.timeout = 20
        self.xx = XiaoX(app_key, app_secret)
        self.timestamp = 0

    def get(self, url):
        if int(time.time()) - self.timestamp > 10:
            self.ip = self.xx.get_ip()
            self.timestamp = int(time.time())
        proxies = {
            "http": f"http://{self.ip}",
            "https": f"http://{self.ip}",
        }
        return self.sess.get(url=url, timeout=self.timeout, proxies=proxies)

    def index(self):
        self.get(url="https://www.chahaoba.com/")

    def get_number_seg(self, number):
        resp = self.get(url=f"https://www.chahaoba.com/{number}")
        soup = BeautifulSoup(resp.text, "html.parser")
        return [td.text.strip().replace("\n", "") for td in soup.find_all("td") if "页面不存在" not in td.find("a")["title"]]

    def search(self, number_seg):
        resp = self.get(url=f"https://www.chahaoba.com/{number_seg}")
        soup = BeautifulSoup(resp.text, "html.parser")
        info = soup.find("div", attrs={"class": "right"})
        if not info:
            return []
        return [li.text.split("：")[1].strip() for li in info.find_all("li")[:3]]

    def get_info(self, number):
        self.index()
        infos = []
        for number in self.get_number_seg(number):
            for n in range(100):
                info = self.search(f'{number}{str(n).zfill(2)}')
                if info:
                    infos.append(info)
        return infos
