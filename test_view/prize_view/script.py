# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/926QADV3227V4?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])
    
wait(Template(r"tpl1623405306786.png", record_pos=(0.0, 0.052), resolution=(2232, 1080)))



# script content
wait(Template(r"spin_icon.png", record_pos=(0.173, -0.209), resolution=(2232, 1080)))
wait(Template(r"spin_btn.png", record_pos=(0.001, -0.006), resolution=(2232, 1080)))

wait(Template(r"collect_btn.png", target_pos=1, record_pos=(-0.004, 0.093), resolution=(2232, 1080)))







# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)