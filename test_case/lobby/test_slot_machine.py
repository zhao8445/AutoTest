from base_view.base_unit import *
from test_view.lobby_view.slot_machine_view.slot_machine_view import *


class TestSlotMachine(StartEnd):
    """
    老虎机业务
    """
    def test_slot_machine(self):
        """
        点击老虎机spin按钮抽奖
        """
        if self.logined:
            sm = SlotMachineView()
            sm.click_slot_machine_icon()
            sleep(2)
            sm.click_spin_btn()
            sleep(5)
            click_close_btn()
            simple_report(
                __file__,
                logpath=True,
                output=PROJECT_ROOT_PATH + "/reports/test_slot_machine_report.html"
            )
        else:
            print("登陆未成功")
            pass

