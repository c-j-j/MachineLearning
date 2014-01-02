from common import dataLoading
from linearRegression.compute_cost import attachOnesToColumn

__author__ = 'Chris'

import unittest

from linearRegression import compute_cost


class LinearRegressionTestCase(unittest.TestCase):
    def test_gradient_descent(self):
        x, y = dataLoading.load('../data/ex1data1.txt')
        xData = attachOnesToColumn(x)
        theta = (0, 0)
        alpha = 0.005
        iterations = 1500
        j_history, theta = compute_cost.gradient_descent(xData, y, theta, alpha, iterations)
        self.assertLess(j_history[1], j_history[0])
        print theta

    def test_gradient_descent_with_scikit(self):
        x, y = dataLoading.load('../data/ex1data1.txt')
        param, intecept = compute_cost.gradient_descent_with_scikit(x, y)
        print param
        print intecept

    def test_normal_equation(self):
        x, y = dataLoading.load('../data/ex1data1.txt')
        xData = attachOnesToColumn(x)
        theta = compute_cost.normal_equation(xData, y)
        print theta

        #todo write multiple features test

    if __name__ == '__main__':
        unittest.main()
