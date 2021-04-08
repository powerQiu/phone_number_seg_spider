# 无忧代理IP
import requests


class XiaoX:

    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret
        self.sess = requests.Session()
        self.sess.headers["Host"] = "api.xiaoxiangdaili.com"

    def get_ip(self):
        url = f"https://api.xiaoxiangdaili.com/ip/get?appKey={self.app_key}&appSecret={self.app_secret}&cnt=20&wt=json"
        resp = self.sess.get(url)
        result = resp.json()
        if result.get("code") == "200":
            return f'{result["data"].get("ip")}:{result["data"].get("port")}'
        return ""
