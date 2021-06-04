# -*- encoding=utf8 -*-
__author__ = "zhaobl01"

from airtest.core.api import *

import unittest
import logging
from time import sleep
import sys


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp====')
        start_app("com.ccmt.augupoker")

    def tearDown(self):
        logging.info('====tearDown====')
        sleep(15)
        clear_app("com.ccmt.augupoker")
        stop_app("com.ccmt.augupoker")