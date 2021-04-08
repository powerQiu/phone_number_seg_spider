# https://haoma.baidu.com/phoneSearch
import requests


class BaiDuHaoMa:

    def __init__(self):
        self.sess = requests.Session()

    def index(self):
        self.sess.get(url="https://haoma.baidu.com/phoneSearch")

    def info(self):
        self.sess.get(url="https://haoma.baidu.com/api/v1/user/info")

    def abdr(self):
        payload = "eyJkYXRhIjoiYTBhZDUyZjQwZWQ4OWZjYjI1NmQ0MDg2ZDJlMjhiNTg5OTkyNzZhZTk4YWU4ODM5YmZkOGVkNDU3MGI2YjJjOWY5YTM0N2Y5OGUxMWU4OGM4YTk2MDFlOWVlNzRkMTM0NmIzNTYzYzk2MmNmNzU0MTBlYjdmNWIxNjlhOGEwODlhYTgzOGEwYzY4M2I4NDM0OGVjMGFjNzA1N2Y5YjI0MDcwN2I0MDIwOTk3MDM2M2U2MzI5ZGE0Y2QxMjQ3ODU3ZjBjMjg3NTNiOGUzZTA0YTdlMGYyZGY5ZGZhNGM2NzI4MTM1MzkyN2FlMjMwZDA2MTBhZjljNDFlYmEwNzNiOTdkYWVkODVlNDkwMjQwMzRhNGY0OGUzMzcyZmMzY2ViMzlmNDQyNzc0MmM3NjA0ODgwN2E0MWQ1ODg4YzBhNTdiMWRjNGRkYzA1ZmIwYWEzZGUzOWRlNjRhYzMwNzRhNTdhNzRjMTRhZDc0ZDM3ZmVhOWFhZTQxOWMzYzZjM2JkZGRiMTYwOTQwMmU3ZmYxMjRhYTY5Y2VkYzRlN2IwMGI1MTEwNzA2MjJlOTBjZjRkN2Q3NjljY2E4YTM4ZTYyMzFkOTk1N2YzMWU5ODE4NGE4Mjg2NTA2Njk1MmYxYjg5YzYxMmJlNzNmNDRjOGY4MGViNDM4YTljMzc2YWJhNzNkOWQwNDc0YTIzMDFlZWM2ZmQ0MmY4NTIyYzZlM2YxZWM5YjAxMTczZjRkNjUwMTIwNDNmOWQ0OTRhZGYyYmJkYjY1YzgwMzhlNTJjZGY4MWMzZGVhYTY2YTM3ZmFhMmNhODE3Nzc1YWE5ZDAwZDllMjgyYmVhMTE1MzFjMGVjYzJkOTNiZmEzOTkyNDhlYjExYmI1NDM5NDk3ODg2NTFkNGQ1Mjg3MDZkYWFkYzE2MmU3MjExMDI1Y2RjZDg3MDA3NmYxYWNmZjk5ZjBjZmQ3N2NjMDY1ZDA5N2FjOWNlZmJiMGE0ODY1OWU3MmQ1YzhjYTY5MjBmNDhiN2EwMGQyNjYyZmQxMDhlM2FiNjcxOTU5NjAzMDhhZGIxNGFhY2IzODhiZGQ2OTIwZWZiZjhmYjk2Y2I2YWY0MGFkOTViZDM4Mzk0ODBjNGMxYTNiNDJhNDhkNzUwNGM0YmRjZmU4ZTVhMGYwNDYxODNkODM5YmViZmYxMTc0Y2Q1MzZlMTg5ZTczODkzZDk3Zjk3YWY1NWU5MDUyYmZlZmNkMzZkMzc5OWRiZGE2M2QxZDZiNTM3OTAyOWNhMzJiYjA4MDc4NzI0NTQ0YjA1Y2EzZWQ3MjVhYzkxYWEwNmFlYTFiYTAzYWFmZTg4MjE4ZjZjN2UwYjllYWEwZTVhNmVjM2JkYjMwZDMzMDNhMzI3OTg1MWFhZGQ0Y2E1NDIxZWFhY2QyYzVhMmY3OGM0OGEwOGI2M2NiY2VkNGY1MGExMGMwYTc3OTg4YmFhMjZhNWM2YjY1YTdhNmM0ZWEzODJkNWI3NTE2Mjg1YzE3ZjQ0ZTI0ZWY4YzI4NzMyMDAzZTc1NzQyZTY1ZWE1ODMyYzg3ZmEwMWRhZjdiN2RhM2RjMjVmOWFlNTFlNTllYzE2YTgxMDMxZWQzZGMyMDkzYmM5NzcwYzI3YWVlYWM2ZGZjNTBiMWYwOWFjY2I5YzZkZjA4NGZhZGUzOTJjZGIyODY1MGRhN2M0MjE3NmQ0N2EyZjcwZmIwYmNkNjczOTRlYTYzMzNkYjUzMzI4ODRjYThiMGU2MGQ3ODM0OTZmMmZlZDYwODgxYWQxNzljY2JhYTk1NDFmMTFjYzU3ZTdkYmYyN2RiODM0ZDlkNjExZjczNDJjOGM1YWJkNzZhZjY4MWVhYzJhOWIyNzgwNGE5ZDNiODEwODNmMTkzMjhhY2I1NGFmYTE3M2JlZTQ3MjhiMjVmZTFjZDZhYzZmNGU3OWNlMmY0ZGY3NDFiOTc5MjczNzc4ZjU2Y2VjM2ZlOTFlZDU3NzM4YTBmMDcwNzI4OGVkYjgwNjRjNWJjOThiMjU5YjY3OTUxYzQxOTcxZDRjNjFlYTJjMDRmYWIxNDA1NDJhOTE0NGI2NzJmZjM3YmJhYTcxMjFjNzIzMGRhNWRjOTY5NzJkYTZiNDMxZjhlOTk4N2Y2ODQ1M2UwOWEzOWFhZDRhYWM4MjY2OWVjOTE3OTI1NTNlMTgxNDYzMTc3NmY3MDIwY2Q2YzIxODJlNzkxNDQ4YWU5YjQ5M2M2NTAyYjU2ZjRjZGMwZDBjMjQ4OTAxZmE5ZGIwYTBiNGQ2YjVmMzlmN2YwZTEwYmY2OWE4NWVjMzRjNzRkY2Y5ZDE4YzNhOTJmNDM2YmM1NmQ5ZTYwYmUwNGFiNTQ3NjBmNTQ2NTYxODUwYzRhNzZlZWY3OGRjMjhlNDIyY2MzOGIwMGI4NjliNjgzMTAwZTM4MjBkNzM5MTY0Y2ZlMTVlZThjMWJjM2M4MzkzOWMyNDgzY2Y1ODkyYjgyNmIyYThmMWMyNTUxNTIwMWI2MDQ2NjA0OWMyY2ViYjMzZjIzOTVkMTBkYWYyMTVkNWQ5ZTg5MDA0ZDA0MDZhNTI4ZTdhODhkNDg1MmI1NDA5NTljYzViMTc3YzVhYzZiM2Y3MjQ2NjkwZWZkMWIwOGRmOGJiY2QwMWJhYWNiMDIyZGIyNmJkYTMxYjZlYjlmYjk3OTQ4M2RkNjliM2JiZGFmNTgyZjg3OWM0ZDg1MmFkM2I0YzdmNjRjZTFkZmM4YzRkNzNiNzg0NjQzYzdhNDhiMTk4ZDAxNmMyZjI2YjRkYjFmY2JiNTgxMjQwMjI1NTdhMDc4ZTIxMzViODdhZTljYjVkZDdhNjA0ZTA1NDUxMGRkNTJhODJiOTgzNDg0NDg1N2U3MmFkMzYwOTY4NjFmMTZhYjJkM2M4M2RmNzkzY2YxNTVlYWUyMGY0Y2ZhZGJmNTllNDA3OWExZDgyMWVhZDAwOGQzNmZmODE5MTY3M2EwZjJkYTVjZjZlNTBlMGY2MGJmYmRiMmUyZmFhOTgzZjU1NWU1ODJiZmE0MDVlMjkxMmU4NDY2NGU2OGE5NWFhZDkxYmNmNDhjZGUyOTQwMDk1ZTExOGMxNzBmMWZjNTUxNzQxZDRiMmYyNzM5OTYxZjlkZWRlMDk5YmRmZjQyZjM1MzJmOTcyYTZlOWE2OWRjZjBlZjZiYjY3Zjg2OTE2MmQ4NzljZDNhY2VkN2U1MWI1ZjNhNWUyNmZjOWNmZWVlNWJkOTAzODY1MWMyZDlkZTFkMTVjNDM4MDdlZDBkZDA0MDY1N2UwNGE5NzQyZDEwZjUwMzRjZGYyMjc2YzRmY2Q4M2FiOWU4ZjFjMGZjNjRmYzRjMmYxYmQzMWM2ZThlODNhODU2ZjM4NjRkMTlmM2M3MWQxMjI2MzIyNGU1NDZlM2I0NDU0N2E3ZWMyZmViOTJmMDY2ODg3NTE4MzgwMDA1ODJhMmI2ZDQ1N2MxODg5ODc0ZGE3MzFkNzcxYTQ5MWMyNjJiZWYzOWYiLCJrZXlfaWQiOjQ3fQ=="
        self.sess.headers = {
            "Host": "miao.baidu.com",
            "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            "DNT": "1",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://haoma.baidu.com",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://haoma.baidu.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7,ja;q=0.6",
        }
        resp = self.sess.post(url="https://miao.baidu.com/abdr", data=payload)
        if not resp.text:
            return {}
        return resp.json()

    def search(self, phone_number):
        j = self.abdr()
        if not j:
            return
        self.sess.headers.update(**{
            "Host": "haoma.baidu.com",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://haoma.baidu.com",
            "Referer": "https://haoma.baidu.com/phoneSearch",
        })
        data = {
            "data": j.get("data"),
            "key_id": j.get("key_id"),
            "sign": j.get("sign"),
            "page": 1,
            "size": 10,
            "search": phone_number
        }
        resp = self.sess.post("https://haoma.baidu.com/api/v1/search", json=data)
        return resp.json()


if __name__ == '__main__':
    bdhm = BaiDuHaoMa()
    print(bdhm.search("13088888888"))
