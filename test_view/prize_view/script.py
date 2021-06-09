# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/926QADV3227V4?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


# script content
assert_exists(Template(r"tpl1623225731820.png", record_pos=(-0.001, 0.205), resolution=(2232, 1080)), "请填写测试点")







# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)