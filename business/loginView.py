# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

import logging
import sys

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

if not cli_setup():
    project_root = sys.path[1].replace("\\", "/")
    auto_setup(__file__, logdir=True, devices=["Android:///", ], project_root=project_root)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class LoginView():
    def login_as_guest(self):
        """
        访客登陆
        :return:
        """
        wait(Template(r"../imgs/login/continue_as_guest.png", record_pos=(0.002, 0.196), resolution=(1280, 800)), timeout=120,
             interval=3)
        touch(Template(r"../imgs/login/continue_as_guest.png", record_pos=(0.005, 0.193), resolution=(1280, 800)))


# if __name__ == '__main__':
#     l = LoginView()
#     l.login_as_guest()
