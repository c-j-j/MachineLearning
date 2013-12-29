__author__ = 'Chris'

import unittest

from linearRegression import compute_cost, simpleGraph


class MyTestCase(unittest.TestCase):
    def test_dataLoading(self):
        x, y = compute_cost.load('../data/ex1data1.txt')
        self.assertEqual(len(x), 97)
        self.assertEqual(len(y), 97)
        simpleGraph.generate_scatter_graph(x, y, 'graphPlot.png')

        theta = (0, 0)
        J = compute_cost.compute_cost(x, y, theta)

        self.assertEqual(round(J,2), 32.07)


if __name__ == '__main__':
    unittest.main()
