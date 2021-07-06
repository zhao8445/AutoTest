from base_view.base_unit import *
from test_view.login_view.login_view import LoginView
from data.user import user


class TestLogin(StartEnd):

    @unittest.skip("跳过访客登陆用例")
    def test_login_as_guest(self):
        """
        访客登陆测试用例
        """
        lv = LoginView()
        lv.login_as_guest()

    def test_login_by_account(self):
        """
        按账号登陆
        :return:
        """
        for _, key in enumerate(user):
            lv = LoginView()
            account = user[key]["account"]
            password = user[key]["password"]
            lv.login_by_account(account, password)
            lv.logout()

