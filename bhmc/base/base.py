import json

import requests


class BaseApp(object):
    def __init__(self):
        self.base_url = "http://test-api.bhmc.com.cn"
        self.app_headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # self.get_url = None

    def requests_get(self, url, get_data=None, token=None, content=None):
        # get方法
        self.get_url = self.base_url + url
        if content == "json":
            self.app_headers["Content-Type"] = "application/json"
        # else:
        #     self.app_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if get_data is None:
            self.rp = requests.get(url=self.get_url, headers=self.app_headers)
        else:
            self.rp = requests.get(url=self.get_url, params=get_data, headers=self.app_headers)

    def requests_post(self, url, post_data=None, token=None, content=None):
        # post方法
        self.post_url = self.base_url + url
        if content == "json":
            self.app_headers["Content-Type"] = "application/json"
            post_data = json.dumps(post_data)
        # else:
        #     self.app_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if post_data is None:
            self.rp = requests.post(url=self.post_url, headers=self.app_headers)
        else:
            self.rp = requests.post(url=self.post_url, data=post_data, headers=self.app_headers)

    def requests_delete(self, url, post_data=None, token=None, content=None):
        # delete方法
        self.post_url = self.base_url + url
        if content == "json":
            self.app_headers["Content-Type"] = "application/json"
            post_data = json.dumps(post_data)
        # else:
        #     self.app_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if post_data is None:
            self.rp = requests.post(url=self.post_url, headers=self.app_headers)
        else:
            self.rp = requests.delete(url=self.post_url, params=post_data, headers=self.app_headers)
        pass

    def get_json(self):
        # 获取json数据
        # if self.rp.status_code
        return self.rp.json()

    def get_assert(self):
        # 获取断言
        pass

    def read_txt(self):
        # 读取txt文件
        pass
