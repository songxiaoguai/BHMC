from bhmc.base.base import BaseApp

from bhmc.base.base_app import BaseApp


class Activity(BaseApp):
    def __init__(self):
        super(Activity, self).__init__()

    def activity_type_list(self):
        # 【活动】分类列表
        url = "/bhmc/v1/white/activity/type_list"
        self.requests_get(url)
        return self.get_json()

    def activity_list(self):
        # 【活动】列表
        url = "/bhmc/v1/white/activity/list"
        data = {"page_no":"","page_size":"","type_hid":"","":""}
        self.requests_get(url)
        return self.get_json()
