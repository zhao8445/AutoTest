import unittest

from test_view.login_view.login_view import LoginView
from base_view.base_view import *


class StartEnd(unittest.TestCase):

    def setUp(self):
        self.login = LoginView()
        self.login.login_as_guest()
        logined = self.login.check_logined()
        self.assertEqual(logined, 1, "登陆未成功")
        self.login.close_tap()

    def tearDown(self):
        self.login.logout()
