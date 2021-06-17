__author__ = "zhaobl01"

import re

from base_view.base_view import *
from test_view.login_view.login_view import LoginView

from utils import baidu_ocr


PACKAGE_NAME = params["package_name"]
IMGS_PATH = PROJECT_ROOT_PATH + '/test_view/prize_view/imgs/'
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

    func quickSort(nums [][]int, l int, r int) [][]int {
        /*递归边界：左右指针一旦相遇，结束递归。*/
        if l > r {
            return nums
        }
    
        //完成本次位置排序调整后l、r值不能改变，故使用变量m、n代替l、r完成本次排序所需的循环。
        m, n := l, r
        //先记录基准元素，基准元素左右侧完成本轮调整后还需要把基准元素归位，
        v := nums[m]
    
        for m < n {
            /*从右往左找出nums中左边界值比nums[m][0]小的第一个元素。*/
            for m < n && nums[n][0] >= v[0] {
                n--
            }
            /*确认真正找到比nums[m][0]小的元素，而非左右指针相遇，则移动找到元素至最左侧。*/
            if m < n {
                nums[m] = nums[n]
            }
            /*从左往右找出nums中左边界值比nums[m][0]大的第一个元素。*/
            for m < n && nums[m][0] <= v[0] {
                m++
            }
            /*确认真正找到比nums[m][0]大的元素，而非左右指针相遇，则移动找到元素至最右侧。*/
            if m < n {
                nums[n] = nums[m]
            }
        }
    
        /*基准元素v归位，递归对nums[m]两侧元素排序，最终保证nums中元素左边界递增。*/
        nums[m] = v
        nums = quickSort(nums, l, m - 1)
        nums = quickSort(nums, m + 1, r)
    
        return nums
    }
    
    
    func merge([][]int intervals) [][]int {
        merged = make([][]int, 0)
        
        for _, interval := range intervals {
            end := len(merged) - 1
            if merged == nil || merged[end][1] < interval[0] {
                merged = append(merged, interval)    
            } else {
                merged[end][1] = max(merged[end][1], interval[1])
            }
        }
    }
    
    func max(int x, int y) int {
        if x > y {
            return x
        } else {
            return y
        }
    }
        
"""


class PrizeView:
    """
    抽奖转盘领取奖励后，验证现金是否领取成功
    """
    def __init__(self):
        self.project_path = params["project_root_path"]

    def get_cash(self):
        """
        获取现金数
        """
        try:
            center = wait(
                Template(IMGS_PATH + r"cash_icon.png", threshold=0.6999999999999997, target_pos=1,
                         record_pos=(-0.349, -0.224), resolution=(2232, 1080), ), timeout=5, interval=1
            )
            x_start = center[0]
            y_start = center[1]

            img_path = partial_screenshot(x_start+40, y_start, x_start+200, y_start+40, "get_cash.png")

            cash_result = baidu_ocr.img_ocr(img_path)
            cash_result = "".join(list(filter(str.isdigit, cash_result)))
            # cash_result = int(cash_result.replace(",", "").replace(".", ""))
        except TargetNotFoundError:
            print("未找到现金icon")

        return cash_result

    def draw_span(self):
        """
        转盘抽奖
        :return:
        """
        try:
            spin_icon_position = wait(
                Template(IMGS_PATH + r"spin_icon.png", record_pos=(0.173, -0.209), resolution=(2232, 1080)),
                 timeout=5, interval=1)
            touch(spin_icon_position)
        except TargetNotFoundError:
            print("SPIN icon Not Found")
            pass
        try:
            sleep(5)
            spin_btn_position = wait(
                Template(IMGS_PATH + r"spin_btn.png", record_pos=(0.001, -0.006), resolution=(2232, 1080)),
                 timeout=5, interval=1)
            touch(spin_btn_position)
        except TargetNotFoundError:
            print("SPIN Button Not Found")
            pass
        try:
            collect_btn_postion = wait(
                Template(IMGS_PATH + r"collect_btn.png", target_pos=1, record_pos=(-0.004, 0.093),
                         resolution=(2232, 1080)), timeout=10, interval=1,
            )

            x_start = collect_btn_postion[0]
            y_start = collect_btn_postion[1]
            img_path = partial_screenshot(x_start, y_start-100, x_start + 400, y_start, "collected_chips.png")
            touch((x_start+200, y_start+40))
            cash = img_ocr(img_path)
            # reward_cash = int("".join(re.findall("(\d+)K", cash))) * 1000
            reward_cash = int("".join(list(filter(str.isdigit, cash)))) * 1000
            click_close_btn()
            return reward_cash
        except TargetNotFoundError:
            print("Collect Button Not Found")
            click_close_btn()
            return 0


if __name__ == '__main__':
    login = LoginView()
    login.login_as_guest()
    login.close_tap()
    logined = login.check_logined()

    if logined:
        print("登陆成功")
        p = PrizeView()
        before_collected_cash = p.get_cash()
        reward_cash = p.draw_span()
        after_colleted_cash = p.get_cash()
        collected_cash = int(after_colleted_cash) - int(before_collected_cash)
        print("领取前的筹码数", before_collected_cash)
        print("领取后的筹码数", after_colleted_cash)
        print("奖励的筹码数为", reward_cash)
        print("领取的筹码数为", collected_cash)
    else:
        print("登陆未成功")
    login.logout()
    from airtest.report.report import simple_report
    simple_report(__file__, logpath=True)