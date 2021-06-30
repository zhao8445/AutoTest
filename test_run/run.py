import unittest
from site_packages.BSTestRunner import BSTestRunner
import time
import sys

path = sys.path[1].replace('\\', "/")
test_dir = path + '/test_case/lobby'
report_dir = path + '/reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + ' test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(
        stream=f, title='AuguPoker Report', description='AuguPoker App Test Report'
    )
    runner.run(discover)

