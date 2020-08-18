from test_case.page_object.ViTest import Vi
from myunit import StartEnd
import unittest
import logging
from time import sleep



class TestVi(StartEnd):
    def test_vi(self):
        logging.info('------------test vi page--------------')
        main=Vi(self.driver)
        main.vi_action('760800543@qq.com','125803636jx')
        sleep(2)



if __name__=='__main__':
    unittest.main()

