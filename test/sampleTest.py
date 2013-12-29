__author__ = 'Chris'

import unittest

from linearRegression import loadData,simpleGraph


class MyTestCase(unittest.TestCase):
    def test_dataLoading(self):
        x,Y = loadData.load('../data/ex1data1.txt')
        self.assertEqual(len(x), 97)
        self.assertEqual(len(Y), 97)
        simpleGraph.create_graph(x,Y,'graphPlot.png')


if __name__ == '__main__':
    unittest.main()
