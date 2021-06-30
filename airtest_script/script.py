# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/926QADV3227V4?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])
 

wait(Template(r"tpl1624937238741.png", threshold=0.9000000000000001, record_pos=(0.279, -0.221), resolution=(2232, 1080)))
wait(Template(r"golden_token.png", record_pos=(0.13, 0.043), resolution=(2232, 1080)))
wait(Template(r"collect_btn.png", record_pos=(-0.003, 0.1), resolution=(2232, 1080)))




    
    
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



