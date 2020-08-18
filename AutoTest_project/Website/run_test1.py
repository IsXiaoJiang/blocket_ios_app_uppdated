import unittest
from function import *
from HTMLTestRunner import HTMLTestRunner
import time

script='/Users/xiajia/Downloads/Python_script1'

report_dir='./test_report/'
test_dir='./test_case'

print("start to run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")


now=time.strftime("%Y-%m-%d %H-%M-%S")
report_name=report_dir+'/'+now+'result.html'

print("Start to write report..")
f=open(report_name,'wb')

k=1
while k<2:
    timing=time.strftime('%H_%M',time.localtime(time.time()))
    if timing=='07_30':
        runner=HTMLTestRunner(stream=f,title="Test Report",description="log in blocket jobb test")
        runner.run(discover)
        print('Finish running scrips')
        break
    else:
        time.sleep(3)
        print(timing)

f.close()

latest_report=latest_report(report_dir)

print("find latest report")
print("send email report..")
send_mail(latest_report)

print("test finished")