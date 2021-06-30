__author__ = "zhaobl01"

from base_view.base_view import *


IMGS_PATH = PROJECT_ROOT_PATH + '/test_view/lobby_view/daily_bonus_view/imgs/'


class DailyBonusView:
    """
    每日签到业务
    """

    def __init__(self):
        self.project_path = params["project_root_path"]

    def click_daily_bonus_icon(self):
        """
        点击每日签到icon
        """
        try:
            position = wait(
                Template(IMGS_PATH + r"daily_bonus_icon.png", record_pos=(0.279, -0.221), resolution=(2232, 1080))
            )
            touch(position)
        except TargetNotFoundError:
            logger.error('未找到每日签到icon')

    def click_collect_btn(self):
        """
        点击'COLLECT'按钮
        """
        try:
            position = wait(
                Template(
                    IMGS_PATH + r"collect_btn.png", threshold=0.90, record_pos=(-0.003, 0.1), resolution=(2232, 1080)
                ), timeout=5, interval=1
            )
            touch(position)
            logger.info("点击签到")
            sleep(5)
            try:
                position = wait(
                    Template(
                        IMGS_PATH + r"collect_btn.png", threshold=0.90, record_pos=(-0.003, 0.1),
                        resolution=(2232, 1080)
                    ), timeout=5, interval=1
                )
                touch(position)
                logger.info("点击收集奖励")
            except TargetNotFoundError:
                logger.error('未找到领取奖励"COLLECT"按钮')
        except TargetNotFoundError:
            logger.error('未找到签到"COLLECT"按钮')


dbv = DailyBonusView()
