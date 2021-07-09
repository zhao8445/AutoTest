from base_view.base_unit import *
from test_view.lobby_view.daily_bonus_view.daily_bonus_view import *
from test_view.login_view.login_view import *


@ddt
class TestDailyBonus(StartEnd):
    """
    每日签到模块
    """
    @data(*user)
    def test_daily_bonus(self, user_info):
        """
        点击每日签到
        """
        # 登陆游戏
        account = user_info["account"]
        password = user_info["password"]
        lv.login_by_account(account, password)

        logger.info("***点击每日签到***")
        dbv.click_daily_bonus_icon()
        dbv.click_collect_btn()
        bv.click_close_btn()


if __name__ == "__main__":
    unittest.main()




