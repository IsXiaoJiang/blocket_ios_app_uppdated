import yaml
import logging
import logging.config
from appium import webdriver

CON_LOG='../log/log.conf'
logging=logging.getLogger()

def appium_desired():

    with open('/Users/xiajia/Documents/Tester/Blocket/blocket_ios_app_uppdated/AutoTest_project/Website/test_case/config/device.yaml', 'r', encoding='utf-8') as file:
        data=yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    # desired_caps['useNewWDA'] = data['useNewWDA']
    desired_caps['platformVersion'] = data['platformVersion']
    # base_dir=os.path.dirname(os.path.dirname(__file__))
    # app_path=os.path.join(base_dir,'app',data['appname'])
    # desired_caps['app'] = app_path
    desired_caps['bundleId'] = data['bundleId']
    desired_caps['xcodeOrgId'] = data['xcodeOrgId']
    desired_caps['xcodeSigningId'] = data['xcodeSigningId']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['noReset'] = data['noReset']
    desired_caps['fullReset'] = data['fullReset']
    desired_caps['autoGrantPermissions'] = data['autoGrantPermissions']
    desired_caps['udid'] = data['udid']
    desired_caps['newCommandTimeout'] = data['newCommandTimeout']
    desired_caps['automationName'] = data['automationName']
    desired_caps['newCommandTimeout'] = 6000
    logging.info('starta app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver

if __name__=='__main__':
    appium_desired()
