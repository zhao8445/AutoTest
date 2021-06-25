# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/926QADV3227V4?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])
 


wait(Template(r"slot_machine_icon.png", record_pos=(0.348, -0.22), resolution=(2232, 1080)))
wait(Template(r"spin_btn.png", record_pos=(0.002, 0.125), resolution=(2232, 1080)))
wait(Template(r"add_btn.png", record_pos=(0.082, 0.131), resolution=(2232, 1080)))
wait(Template(r"sub_btn.png", record_pos=(-0.083, 0.128), resolution=(2232, 1080)))

    


    
    
    
    
    
    
    
    

    
    
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



