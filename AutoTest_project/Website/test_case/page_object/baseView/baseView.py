import traceback
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class BaseView(object):
    def __init__(self,driver):
        self.driver=driver


    def find_element(self,*loc):
       return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_element(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipeup(self):
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        print("-------------------swipeup-------------------------")
        self.driver.execute_script("mobile: dragFromToForDuration",
                                   {"element": None, "fromX": (width / 4), "fromY": (height/ 2),
                                    "toX": (width / 4), "toY": 0,
                                    "duration": 1})
    def swipeUpLess(self):

        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        print("-------------------swipeup-------------------------")
        self.driver.execute_script("mobile: dragFromToForDuration",
                                   {"element": None, "fromX": (width / 2), "fromY": (height/ 3),
                                    "toX": (width / 2), "toY": 0,
                                    "duration": 1})

    def swipeDown(self):
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        print("-------------------swipeup-------------------------")
        self.driver.execute_script("mobile: dragFromToForDuration",
                                   {"element": None, "fromX": (width / 4), "fromY": 0,
                                    "toX": (width / 4), "toY": height/2,
                                    "duration": 1})

    def swiperight(self):
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        print("-------------------swipe right-------------------------")
        self.driver.execute_script("mobile: dragFromToForDuration",
                                   {"element": None, "fromX": 0, "fromY": (height / 2),
                                    "toX": (width / 2), "toY": (height / 2),
                                    "duration": 1})

    def is_element_exist(self, element):
        source = self.driver.page_source
        print(source)
        if element in source:
            return True
        else:
            return False

    def assert_if_element_exist(self,element):
        print("---------assert if element : "+element+"exists---------------------")
        try:
            self.driver.find_element_by_ios_predicate(element) or self.driver.find_element_by_accessibility_id(element)
        except NoSuchElementException:
            traceback.print_exc()
            print ('traceback.format_exc():\n%s' % traceback.format_exc())

    def klar_button(self):
        print("--------------------Click on Klar---------------------------------")
        Klar = self.driver.find_element_by_accessibility_id("Klar")
        actions = TouchAction(self.driver)
        actions.tap(Klar)
        actions.perform()

    def execute_tap(self,element):
        actions = TouchAction(self.driver)
        actions.tap(element)
        actions.perform()

    def telephone_action(self):
            actions = TouchAction(self.driver)
            keyboard0 = self.driver.find_element_by_accessibility_id("0")
            actions.tap(keyboard0)
            keyboard7 = self.driver.find_element_by_accessibility_id("7")
            actions.tap(keyboard7)
            actions.perform()
            keyboard0 = self.driver.find_element_by_accessibility_id("0")
            actions.tap(keyboard0)
            actions.perform()
            keyboard5 = self.driver.find_element_by_accessibility_id("5")
            actions.tap(keyboard5)
            actions.perform()
            keyboard7 = self.driver.find_element_by_accessibility_id("7")
            actions.tap(keyboard7)
            actions.perform()
            keyboard6 = self.driver.find_element_by_accessibility_id("6")
            actions.tap(keyboard6)
            actions.perform()
            keyboard0 = self.driver.find_element_by_accessibility_id("0")
            actions.tap(keyboard0)
            actions.perform()
            keyboard9 = self.driver.find_element_by_accessibility_id("9")
            actions.tap(keyboard9)
            actions.perform()
            keyboard2 = self.driver.find_element_by_accessibility_id("2")
            actions.tap(keyboard2)
            actions.perform()
            keyboard7 = self.driver.find_element_by_accessibility_id("7")
            actions.tap(keyboard7)
            actions.perform()
            Klar = self.driver.find_element_by_accessibility_id("Klar")
            actions.tap(Klar)
            actions.perform()