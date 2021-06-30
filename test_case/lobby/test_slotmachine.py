from base_view.base_unit import *
from base_view.base_view import *
from test_view.lobby_view.slot_machine_view.slot_machine_view import *


class TestSlotMachine(StartEnd):
    """
    老虎机业务
    """
    def test_slot_machine(self):
        """
        点击老虎机spin按钮抽奖
        """
        logger.info("*******抽取老虎机******")
        n = 0
        while n < 1:
            sm = SlotMachineView()
            sm.click_slot_machine_icon()
            sleep(2)
            sm.click_spin_btn()
            sleep(5)
            bv.click_close_btn()
            n += 1

