
from baseView.baseView import BaseView
from model.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from time import sleep
import os, time

class Common(BaseView):



    def check_readMore(self):
        logging.info('------------------------check read more---------')
        try:
            readMore = self.driver.find_element_by_ios_predicate("type =='XCUIElementTypeButton' AND label='Läs mer'")
        except NoSuchElementException:
            print('no readmore')
        else:
            self.execute_tap(readMore)
            sleep(5)
            stang=self.driver.find_element_by_ios_predicate("type =='XCUIElementTypeButton' AND label='Stäng'")
            self.execute_tap(stang)


    def check_okButton(self):
        logging.info('------------------------check ok button---------')
        try:
            okButton = self.driver.find_element_by_ios_predicate("type =='XCUIElementTypeButton' AND label='Okej!'")
        except NoSuchElementException:
            print('no okbutton')
        else:
            self.execute_tap(okButton)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M-%S")
        return self.now

    def getScreenShot(self,module):
        time= self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)


if __name__=='__main__':
    driver=appium_desired()
    com=Common(driver)
    sleep(3)
    com.check_readMore()
    com.check_okButton()

