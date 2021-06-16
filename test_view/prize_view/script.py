# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/926QADV3227V4?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])
wait(Template(r"collect_btn.png", record_pos=(-0.003, 0.098), resolution=(2232, 1080)))

    
    

    
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

wait(Template(r"continue_as_guest.png", record_pos=(0.002, 0.168), resolution=(2232, 1080)))
wait(Template(r"close_tag_icon.png", record_pos=(0.278, -0.162), resolution=(2232, 1080)))
wait(Template(r"cash_icon.png", record_pos=(-0.365, -0.23), resolution=(2232, 1080)))
wait(Template(r"play_now_btn.png", record_pos=(-0.002, 0.214), resolution=(2232, 1080)))


