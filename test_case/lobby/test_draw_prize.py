from base_view.base_unit import *
from test_view.lobby_view.prize_view.prize_view import *


class TestDrawPrize(StartEnd):
    """
    转盘抽奖模块
    """
    def test_draw_prize(self):
        """
        转盘抽奖
        """
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


