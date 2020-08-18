from test_case.page_object.StartpageTest import StartpageTest
from myunit import StartEnd
import unittest
import logging
from time import sleep



class TestStartPage(StartEnd):
    def test_startpage(self):
        logging.info('------------test start page--------------')
        main=StartpageTest(self.driver)
        main.search_action()
        sleep(1)
        main.filter_action()
        sleep(2)
        main.list_action()



if __name__=='__main__':
    unittest.main()

