from base_view.base_unit import *
from test_view.lobby_view.slot_machine_view.slot_machine_view import *

from ddt import ddt, data, unpack, file_data

from data.user import user


@ddt
class TestSlotMachine(StartEnd):
    """
    老虎机
    """

    @data(*user)
    def test_slot_machine(self, value):
        """
        老虎机模块
        """
        print(value)
        # logger.info("***抽取老虎机***")
        # n = 0
        # while n < 1:
        #     sm = SlotMachineView()
        #     sm.click_slot_machine_icon()
        #     sleep(2)
        #     sm.click_spin_btn()
        #     sleep(5)
        #     bv.click_close_btn()
        #     n += 1


if __name__ == '__main__':
    unittest.main()
