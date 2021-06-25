import unittest

from test_view.login_view.login_view import LoginView


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.login = LoginView()
        self.login.login_as_guest()
        self.login.close_tap()
        self.logined = self.login.check_logined()

    def tearDown(self):
        self.login.logout()
