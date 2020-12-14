import unittest

import pytest

from api.app_activity_api import Activity


class TestActivity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app_activity = Activity()

    def test_activity_type_list(self):
        self.app_activity.activity_type_list()
        self.app_activity.get_assert("success", 200)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestActivity("test4_Write_off_query"))
    unittest.TextTestRunner(verbosity=2).run(suite)