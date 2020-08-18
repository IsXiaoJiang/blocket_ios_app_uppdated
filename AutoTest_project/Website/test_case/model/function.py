#coding=utf-8
from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header



def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    print(func_path)

    base_dir=os.path.dirname(func_path)
    print(base_dir)

    base_dir=str(base_dir)

    base_dir=base_dir.replace('\\','/')

    print(base_dir)

    base=base_dir.split('Website')[0]

    print(base)

    filepath=base+'/Website/test_case/screenshot/'+filename

    driver.get_screenshot_as_file(filepath)


def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()
    smtpserver='smtp.163.com'

    user='jiangx0927@163.com'
    password='125803636jx'

    sender='jiangx0927@163.com'
    receives=['xiao.jiang@schibsted.com']

    subject='Web Selenium automation testning'

    msg=MIMEText(mail_content,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=sender
    msg['To']=','.join(receives)
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"


    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)


    print("Start sending email...")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("Send email end!")


def latest_report(report_dir):
    lists=os.listdir(report_dir)
    print(lists)
    #lists.sort(key=lambda fn:os.path.getatime(report_dir+fn))
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + fn))

    print("The lastest report is "+ lists[-1])

    file=os.path.join(report_dir,lists[-1])
    print(file)
    return file

if __name__=='__main__':

    driver=webdriver.Firefox()
    driver.get("https://jobb.blocket.se")
    insert_img(driver,'bloket jobbahhah.jpg')

    func_path = os.path.dirname(__file__)
    base_dir = os.path.dirname(func_path)
    base_dir=str(base_dir)

    base_dir=base_dir.replace('\\','/')
    base = base_dir.split('Website')[0]
    dir2 = base + 'Website/test_report/'
    print(dir2)
    latest_report(dir2)
    latest_report = latest_report(dir2)
    send_mail(latest_report)

    driver.quit()