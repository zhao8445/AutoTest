from base_view.base_unit import *
from base_view.base_view import *
from test_view.lobby_view.daily_bonus_view.daily_bonus_view import *


class TestDailyBonus(StartEnd):
    """
    每日签到业务
    """
    def test_daily_bonus(self):
        """
        点击每日签到
        """
        logger.info("******点击每日签到******")
        dbv.click_daily_bonus_icon()
        dbv.click_collect_btn()
        bv.click_close_btn()



