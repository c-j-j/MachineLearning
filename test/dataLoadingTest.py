from common import dataLoading

__author__ = 'Chris'

import unittest


class MyTestCase(unittest.TestCase):
    def test_data_loading(self):
        X,y=dataLoading.load('../data/ex1data2.txt')
        self.assertEqual(X.shape[1], 2)



if __name__ == '__main__':
    unittest.main()
