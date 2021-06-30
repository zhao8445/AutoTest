__author__ = "zhaobl01"


from base_view.base_view import *

from utils import baidu_ocr


PACKAGE_NAME = params["package_name"]
REWARD_CHIP_IMG_PATH = params["reward_chip_img_path"]
IMGS_PATH = PROJECT_ROOT_PATH + '/test_view/lobby_view/prize_view/imgs/'


class PrizeView:
    """
    转盘抽奖业务
    """

    def __init__(self):
        self.project_path = params["project_root_path"]

    def get_cash(self):
        """
        获取现金数
        """
        cash_result = 0
        try:
            center = wait(
                Template(IMGS_PATH + r"cash_icon.png", threshold=0.6999999999999997, target_pos=1,
                         record_pos=(-0.349, -0.224), resolution=(2232, 1080), ), timeout=5, interval=1
            )
            x_start = center[0]
            y_start = center[1]

            img_path = bv.partial_screenshot(x_start+40, y_start, x_start+200, y_start+40, "get_cash.png")

            cash_result = baidu_ocr.img_ocr(img_path)
            cash_result = "".join(list(filter(str.isdigit, cash_result)))
        except TargetNotFoundError:
            logger.error("未找到现金icon")

        return cash_result

    def click_spin_icon(self):
        """
        点击SPIN图标
        """
        try:
            spin_icon_position = wait(
                Template(IMGS_PATH + r"spin_icon.png", record_pos=(0.173, -0.209), resolution=(2232, 1080)),
                 timeout=5, interval=1)
            touch(spin_icon_position)
        except TargetNotFoundError:
            logger.error("未找到'SPIN'图标icon")

    def click_spin_btn(self):
        """
        点击SPIN按钮
        """
        try:
            sleep(5)
            spin_btn_position = wait(
                Template(IMGS_PATH + r"spin_btn.png", record_pos=(0.001, -0.006), resolution=(2232, 1080)),
                 timeout=5, interval=1)
            touch(spin_btn_position)
        except TargetNotFoundError:
            logger.error("未找到'SPIN'按钮")

    def draw_span(self):
        """
        转盘抽奖
        """
        reward_chips = [
            "20", "40", "50", "100", "150", "200"
        ]
        reward_cash = 0

        self.click_spin_icon()
        self.click_spin_btn()
        try:
            collect_btn_postion = wait(
                Template(IMGS_PATH + r"collect_btn.png", target_pos=1, record_pos=(-0.004, 0.093),
                         resolution=(2232, 1080)), timeout=10, interval=1,
            )

            x_start = collect_btn_postion[0]
            y_start = collect_btn_postion[1]
            img_path = bv.partial_screenshot(x_start+30, y_start-70, x_start+350, y_start-30, "collected_chips.png")
            reward = baidu_ocr.img_ocr(img_path)
            if "RING" in reward:
                reward_cash = "RING"
                touch((x_start + 200, y_start + 40))
                bv.click_close_btn()
            else:
                for chip in reward_chips:
                    reward_chip_img = REWARD_CHIP_IMG_PATH + "/prize_view/imgs/reward_chips/" + chip + "k.png"
                    try:
                        position = wait(
                            Template(
                                reward_chip_img, record_pos=(0.004, 0.052), resolution=(2232, 1080),
                                threshold=0.99
                            ), timeout=1, interval=0.3,
                        )
                        if position:
                            reward_cash = int(chip) * 1000
                            touch((x_start + 200, y_start + 40))
                            bv.click_close_btn()
                            break
                    except:
                        pass
            return reward_cash
        except TargetNotFoundError:
            logger.error("未找到'COLLECT'按钮")
            bv.click_close_btn()
            return 0
