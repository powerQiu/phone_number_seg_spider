# https://www.ip138.com/sj/
import requests
from bs4 import BeautifulSoup


class Ip138:
    
    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        
    def search(self, number_seg):
        url = f"https://www.ip138.com/mobile.asp?mobile={number_seg}&action=mobile"
        resp = self.sess.get(url)
        resp.encoding = "utf-8"
        return resp.text
    
    def get_info(self, number_seg):
        result = self.search(number_seg)
        soup = BeautifulSoup(result, "html.parser")
        trs = soup.find_all("tr")
        info = number_seg
        for tr in trs[3:-1]:
            info += "\t" + tr.find_all("td")[1].find("span").text.replace("\xa0", " ")
        return info


if __name__ == '__main__':
    ip138 = Ip138()
    print(ip138.get_info("1337400"))
