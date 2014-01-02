from numpy import zeros
from common import dataLoading

__author__ = 'Chris'

import unittest

from logisticRegression import logisticRegressionTools


class MyTestCase(unittest.TestCase):
    def test_sigmoid_function(self):
        sigmoidAnswer1 = logisticRegressionTools.sigmoid(100)
        sigmoidAnswer0 = logisticRegressionTools.sigmoid(0)
        self.assertAlmostEqual(sigmoidAnswer1,1,places=5)
        self.assertEqual(sigmoidAnswer0,0.5)

    def test_logistical_regression_with_dataSet1(self):
        X,y=dataLoading.load("../data/ex2data1.txt")

        logReg=logisticRegressionTools.computeCost(X,y,showGraph=True)

        logReg.predict_proba([45,85])





if __name__ == '__main__':
    unittest.main()
