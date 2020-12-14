import json
import os

import requests

from api import phone_num, code
from tools.log_file import GetLogin

log = GetLogin.get_logger()


class BaseApp(object):
    def __init__(self):
        self.base_url = "http://test-api.bhmc.com.cn"
        self.base_bhmc_url = "http://test-api.bhmc.com.cn"
        self.app_headers = {"Content-Type": "application/x-www-form-urlencoded", "token": None}
        self.token = None
        self.user_hid = None

    def requests_get(self, url, get_data=None, token=None, content=None):
        # get方法
        self.get_url = self.base_url + url
        if content == "json":
            self.app_headers["Content-Type"] = "application/json"
        # else:
        #     self.app_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if get_data is None:
            self.rp = requests.get(url=self.get_url, headers=self.app_headers, verify=False)
        else:
            self.rp = requests.get(url=self.get_url, params=get_data, headers=self.app_headers, verify=False)

    def requests_post(self, url, post_data=None, content=None):
        # post方法
        self.post_url = self.base_url + url
        if content == "json":
            self.app_headers["Content-Type"] = "application/json"
            post_data = json.dumps(post_data)
        # else:
        #     self.app_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if post_data is None:
            self.rp = requests.post(url=self.post_url, headers=self.app_headers, verify=False)
        else:
            self.rp = requests.post(url=self.post_url, data=post_data, headers=self.app_headers, verify=False)

    def requests_delete(self, url, post_data=None, content=None):
        # delete方法
        self.post_url = self.base_url + url
        if content == "json":
            self.app_headers["Content-Type"] = "application/json"
            post_data = json.dumps(post_data)
        # else:
        #     self.app_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if post_data is None:
            self.rp = requests.post(url=self.post_url, headers=self.app_headers, verify=False)
        else:
            self.rp = requests.delete(url=self.post_url, params=post_data, headers=self.app_headers, verify=False)

    def send_message(self, phone):
        # 获取验证码
        phone_data = phone
        if phone is None:
            phone_data = phone_num
        url = "/v1/app/white/sms2"
        data = {"phone": phone_data}
        self.requests_post(url, data)
        return self.get_json()

    def by_login(self, phone=None):
        # 验证码登录
        phone_data = phone
        if phone is None:
            phone_data = phone_num
        self.send_message(phone_data)
        self.app_headers["App-Version"] = "7.3.0"
        self.app_headers["device"] = "android"
        self.app_headers["Origin-Id"] = "011e0b33ad5bf235"
        data_login = {"phone": phone_data, "code": code}
        url = "/v1/app/account/users/info"
        self.requests_post(url, data_login)
        self.app_headers["token"] = self.token = self.get_json().get("data").get("token")
        self.user_hid = self.get_json().get("data").get("hid")
        return self.get_json()

    def get_json(self):
        # 获取json数据
        # if self.rp.status_code
        return self.rp.json()

    def get_assert(self, message, status_code, data=None):
        # 获取断言
        try:
            # 断言响应信息
            assert message == self.rp.json().get("msg")
            # 断言状态码
            assert status_code == self.rp.status_code
            # 断言data数据
            # if data is None:
            #     pass
            # else:
            #     assert data == self.rp.json().get("data")
        except Exception as e:
            # 日志
            log.error(f"断言错误了！{e},{message}!={self.rp.json().get('msg')},{status_code}!={self.rp.status_code}")
            # 抛出异常
            raise e

    def read_txt(self):
        # 读取txt文件
        pass


if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath("bhmc")))
    print(os.path.abspath(__file__))
