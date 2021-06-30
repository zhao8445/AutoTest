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
            logger.info("点击老虎机icon")
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
            logger.info("点击'+'筹码按钮")
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
            logger.info("点击'-'筹码按钮")
        except TargetNotFoundError:
            logger.error("未找到老虎机'-'按钮")

    def click_spin_btn(self):
        """
        点击"spin"按钮
        """
        try:
            position = wait(
                Template(IMGS_PATH + r"spin_btn.png", record_pos=(0.002, 0.125), resolution=(2232, 1080))
            )
            touch(position)
            logger.info("点击'spin'按钮")
        except TargetNotFoundError:
            logger.error("未找到老虎机'SPIN'按钮")
