from test_case.page_object.AiBilarTest import AiBilarTest
from myunit import StartEnd
import unittest
import logging



class TestAi(StartEnd):
    def test_ai(self):
        logging.info('------------Ai test--------------')
        main=AiBilarTest(self.driver)
        main.aiBilar_action()



if __name__=='__main__':
    unittest.main()

