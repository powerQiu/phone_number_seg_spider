# https://shouji.xpcha.com/
import requests
from bs4 import BeautifulSoup


class Xpcha:

    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) " \
                                          "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 " \
                                          "Safari/604.1 "

    def search(self, number_seg):
        url = f"https://shouji.xpcha.com/{number_seg}.html"
        resp = self.sess.get(url)
        return resp.text

    def get_info(self, number_seg):
        result = self.search(number_seg)
        soup = BeautifulSoup(result, "html.parser")
        dl = soup.find("dl", attrs={"class": "liebiao_1"})
        return '\t'.join([number_seg, ] + [dd.text.split("：")[1] for dd in dl.find_all("dd")][:-1])


if __name__ == '__main__':
    xpcha = Xpcha()
    print(xpcha.get_info("1353914"))
