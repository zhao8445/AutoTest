__author__ = "zhaobl01"

from base_view.base_view import *


IMGS_PATH = PROJECT_ROOT_PATH + '/test_view/lobby_view/slot_machine_view/imgs/'


class SlotMachineView:
    """
    老虎机业务
    """

    def __init__(self):
        self.project_path = params["project_root_path"]

    def click_slot_machine_icon(self):
        """
        点击老虎机icon
        """
        try:
            position = wait(
                Template(IMGS_PATH + r"slot_machine_icon.png", record_pos=(0.348, -0.22), resolution=(2232, 1080))
            )
            touch(position)
            # logger.info("点击老虎机ICON")
        except TargetNotFoundError:
            logger.error("未找到老虎机ICON")

    def click_add_btn(self):
        """
        点击"+"筹码按钮
        """
        try:
            position = wait(
                Template(IMGS_PATH + r"add_btn.png", record_pos=(0.082, 0.131), resolution=(2232, 1080))
            )
            touch(position)
            # logger.info("点击'+'筹码按钮")
        except TargetNotFoundError:
            logger.error("未找到老虎机'+'按钮")

    def click_sub_btn(self):
        """
        点击"-"筹码按钮
        """
        try:
            position = wait(
                Template(IMGS_PATH + r"sub_btn.png", record_pos=(-0.083, 0.128), resolution=(2232, 1080))
            )
            touch(position)
            # logger.info("点击'-'筹码按钮")
        except TargetNotFoundError:
            logger.error("未找到老虎机'-'按钮")

    def click_spin_btn(self):
        """
        点击"spin"按钮
        """
        try:
            position = wait(
                Template(
                    IMGS_PATH + r"spin_btn.png", record_pos=(0.002, 0.125), resolution=(2232, 1080),
                    threshold=0.7
                )
            )
            touch(position)
            # logger.info("点击SPIN按钮")
        except TargetNotFoundError:
            logger.error("未找到老虎机SPIN按钮")

    def find_slot_chips_box_position(self):
        """
        获取老虎机投注金币框坐标
        """
        try:
            start_position = wait(
                Template(
                    IMGS_PATH + r"slot_chips_box.png", target_pos=1, record_pos=(0.017, 0.078), resolution=(2244, 1080)
                )
            )
            end_position = wait(
                Template(
                    IMGS_PATH + r"slot_chips_box.png", target_pos=9, record_pos=(0.017, 0.078), resolution=(2244, 1080)
                )
            )
            return start_position, end_position
        except TargetNotFoundError:
            logger.error('未找到老虎机投注金币框')

    def find_your_chips_box_position(self):
        """
        获取YOUR CHIPS框坐标
        """
        try:
            start_position = wait(
                Template(
                    IMGS_PATH + r"your_chips_box.png", target_pos=1, record_pos=(0.017, 0.078), resolution=(2244, 1080),
                    threshold=0.5
                )
            )
            end_position = wait(
                Template(
                    IMGS_PATH + r"your_chips_box.png", target_pos=9, record_pos=(0.017, 0.078), resolution=(2244, 1080),
                    threshold=0.5
                )
            )
            return start_position, end_position
        except TargetNotFoundError:
            logger.error('未找到YOUR CHIPS框')

    def is_free_spin(self):
        """
        判断是否是"FREE SPIN"按钮
        :return:
        """
        try:
            wait(
                Template(
                    IMGS_PATH + r"free_spin_btn.png", threshold=0.8, record_pos=(0.018, 0.127), resolution=(2244, 1080)
                ), timeout=5, interval=1
            )
            return 1
        except TargetNotFoundError:
            return 0


sm = SlotMachineView()
