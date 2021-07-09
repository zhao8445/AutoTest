from base_view.base_unit import *
from test_view.lobby_view.prize_view.prize_view import *



@ddt
class TestDrawPrize(StartEnd):
    """
    转盘抽奖模块
    """
    @data(*user)
    def test_draw_prize(self, user_info):
        """
        转盘抽奖
        """
        # 登陆游戏
        account = user_info["account"]
        password = user_info["password"]
        lv.login_by_account(account, password)

        logger.info("***转盘抽奖***")
        n = 0
        while n < 1:
            p = PrizeView()
            before_collected_cash = p.get_cash()
            reward_cash = p.draw_span()
            if reward_cash == "RING":
                self.assertEqual("RING", reward_cash)
            else:
                after_colleted_cash = p.get_cash()
                logger.debug("领取前的筹码数: %s" % before_collected_cash)
                logger.debug("领取后的筹码数: %s" % after_colleted_cash)
                collected_cash = int(after_colleted_cash) - int(before_collected_cash)
                logger.debug("奖励的筹码数: %s" % reward_cash)
                logger.debug("领取的筹码数: %d" % collected_cash)
                self.assertEqual(reward_cash, collected_cash, "奖励下发不对")
            n += 1


if __name__ == "__main__":
    unittest.main()