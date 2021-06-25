from base_view.base_unit import *
from test_view.login_view.login_view import LoginView
import unittest


class TestLogin(StartEnd):
    def test_login_as_guest(self):
        """
        访客登陆测试用例
        """
        l = LoginView()
        l.login_as_guest()

