from base_view.base_unit import *
from base_view.base_view import *
from test_view.prize_view.prize_view import PrizeView
import unittest


class TestPrize(StartEnd):
    def test_draw_prize(self):
        if self.logined:
            print("登陆成功")
            n = 0
            while n < 10:
                p = PrizeView()
                before_collected_cash = p.get_cash()
                reward_cash = p.draw_span()
                after_colleted_cash = p.get_cash()
                print("领取前的筹码数", before_collected_cash)
                print("领取后的筹码数", after_colleted_cash)
                print("奖励的筹码数为", reward_cash)
                collected_cash = int(after_colleted_cash) - int(before_collected_cash)
                print("领取的筹码数为", collected_cash)
                print(n)
                self.assertEqual(collected_cash, reward_cash, "奖励下发不对")
                n += 1
        else:
            print("登陆未成功")

        simple_report(
            __file__,
            logpath=True,
            output=PROJECT_ROOT_PATH + "/reports/test_prize_report.html"
        )

if __name__ == '__main__':
    unittest.main()
