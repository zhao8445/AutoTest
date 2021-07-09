import traceback

from base_view.base_unit import *
from test_view.lobby_view.slot_machine_view.slot_machine_view import *
from test_view.login_view.login_view import *


@ddt
class TestSlotMachine(StartEnd):
    """
    老虎机
    """
    @data(*user)
    def test_slot_machine(self, user_info):
        """
        老虎机模块
        """

        # 登陆游戏
        account = user_info["account"]
        password = user_info["password"]
        lv.login_by_account(account, password)

        logger.info("***抽取老虎机***")
        n = 0
        while n < 1:
            # 默认老虎机奖励为0
            reward_chips = 0

            # 记录抽取老虎机之前的金币数
            before_cash = bv.get_cash()
            logger.debug('抽取老虎机之前的金额:'+before_cash)

            sm = SlotMachineView()
            sm.click_slot_machine_icon()
            sleep(2)

            # 获取老虎机投注金额坐标
            slot_chips_start, slot_chips_end = sm.find_slot_chips_box_position()
            # 获取老虎机GOOD LUCK坐标
            your_chips_start, your_chips_end = sm.find_your_chips_box_position()

            # 识别记录老虎机投注额
            res = bv.get_ocr_result(slot_chips_start, slot_chips_end, "slot_chips.png")[0]['words']
            bet_chips = int("".join(list(filter(str.isdigit, res)))) * 1000
            logger.debug('老虎机投注金额:' + str(bet_chips))

            if not sm.is_free_spin():
                logger.debug('不是FREE SPIN，扣除投注筹码')
                reward_chips -= bet_chips
            sm.click_spin_btn()
            sleep(5)

            # 识别记录老虎机抽取结果
            try:
                res = bv.get_ocr_result(your_chips_start, your_chips_end, "your_chips.png")[0]['words']
            except Exception as e:
                logger.error(traceback.format_exc())
            if res == 'GOOD LUCK':
                logger.debug('老虎机未中奖:GOOD LUCK')
                logger.debug('扣除投注筹码实际奖励:' + str(reward_chips))
            else:
                try:
                    c = int("".join(list(filter(str.isdigit, res)))) * 1000
                    logger.debug('老虎机奖励筹码：' + str(c))
                    reward_chips += c
                    logger.debug('扣除投注筹码后实际奖励:' + str(reward_chips))
                except Exception:
                    logger.debug('老虎机奖励金额:' + res)
                    logger.error(traceback.format_exc())

            sleep(2)
            bv.click_close_btn()

            # 记录抽取老虎机之后的金币数
            after_cash = bv.get_cash()
            logger.debug('抽取老虎机之后的金额:' + after_cash)

            collected_chips = str(int(after_cash) - int(before_cash))
            logger.debug('抽取老虎机获取的金额:' + collected_chips)

            self.assertEqual(int(reward_chips), int(collected_chips), '老虎机奖励下发不一致')

            n += 1


if __name__ == '__main__':
    unittest.main()
