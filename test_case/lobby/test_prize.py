from base_view.base_unit import *
from test_view.lobby_view.prize_view.prize_view import PrizeView


class TestPrize(StartEnd):
    def test_draw_prize(self):
        if self.logined:
            n = 0
            while n < 1:
                p = PrizeView()
                before_collected_cash = p.get_cash()
                reward_cash = p.draw_span()
                if reward_cash == "RING":
                    self.assertEqual("RING", reward_cash)
                else:
                    after_colleted_cash = p.get_cash()
                    # print("领取前的筹码数", before_collected_cash)
                    # print("领取后的筹码数", after_colleted_cash)
                    collected_cash = int(after_colleted_cash) - int(before_collected_cash)
                    # print("奖励的筹码数为", reward_cash)
                    # print("领取的筹码数为", collected_cash)
                    # print(n)
                    self.assertEqual(reward_cash, collected_cash, "奖励下发不对")
                n += 1
        else:
            # print("登陆未成功")
            pass