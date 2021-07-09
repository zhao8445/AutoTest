import unittest
from ddt import ddt, data, unpack, file_data

from airtest.core.api import *
from airtest.report.report import simple_report

from test_view.login_view.login_view import *
from data.user import user

PACKAGE_NAME = params["package_name"]
PROJECT_ROOT_PATH = params["project_root_path"]
USER_DATA_PATH = PROJECT_ROOT_PATH + "/data/user2.json"


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logger.info("-------------------------------")

    @classmethod
    def tearDownClass(self):
        simple_report(__file__, logpath=True)
        logger.info("-------------------------------")

    def setUp(self):
        clear_app(PACKAGE_NAME)
        start_app(PACKAGE_NAME)

    def tearDown(self):
        sleep(5)
        lv.logout()
