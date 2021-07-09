# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/926QADV3227V4?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])
    

    
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


wait(Template(r"your_chips.png", record_pos=(0.016, -0.167), resolution=(2244, 1080)))
