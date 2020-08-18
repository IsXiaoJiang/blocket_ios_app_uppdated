#!/usr/bin/env python3
import sys

path='/Users/xiajia/Documents/Tester/Blocket/blocket_ios_app_uppdated/AutoTest_project/driver'
sys.path.append(path)

path='/Users/xiajia/Documents/Tester/Blocket/blocket_ios_app_uppdated/AutoTest_project/Website/test_case/page_object'
sys.path.append(path)

path='/Users/xiajia/Documents/Tester/Blocket//blocket_ios_app_uppdated/AutoTest_project/Website/test_case/model'
sys.path.append(path)

path='/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/'
sys.path.append(path)

import unittest

from HTMLTestRunner import HTMLTestRunner
import time

from function import *

#report_dir='./test_report/'
#test_dir='./test_case/'

report_dir='/Users/xiajia/Documents/Tester/Blocket/blocket_ios_app_uppdated/AutoTest_project/Website/test_report/'
test_dir='/Users/xiajia/Documents/Tester/Blocket/blocket_ios_app_uppdated/AutoTest_project/Website/test_case/'


print("start to run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

now=time.strftime("%Y-%m-%d %H-%M-%S")
report_name=report_dir+'/'+now+'result.html'

print("Start to write report..")

with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title="Test Report",description="Blocket app test")
    runner.run(discover)
    f.close()

print("find latest report")
latest_report=latest_report(report_dir)

print("send email report..")
send_mail(latest_report)

print("test finished")
