from test_case.page_object.SparadeTest import SparadeTest
from myunit import StartEnd
import unittest
import logging



class TestSparade(StartEnd):
    def test_sparade(self):
        logging.info('------------Sparade test--------------')
        #main=SparadeTest(self.driver)
        #main.sparade_action()



if __name__=='__main__':
    unittest.main()

