from api.base_app import BaseApp


class Activity(BaseApp):
    def __init__(self):
        super(Activity, self).__init__()
        self.by_login()

    def activity_type_list(self):
        # 【活动】分类列表
        url = "/bhmc/v1/white/activity/type_list"
        self.requests_get(url)
        return self.get_json()

    def activity_list(self):
        # 【活动】列表
        url = "/bhmc/v1/white/activity/list"
        data = {"page_no":"","page_size":"","type_hid":"","keyword":""}
        self.requests_get(url,data)
        return self.get_json()

    def activity_register_info(self):
        # 【活动】报名活动-详情
        url = "/bhmc/v1/white/activity/register_info"
        data = {"hid":""}
        self.requests_get(url,data)
        return self.get_json()


