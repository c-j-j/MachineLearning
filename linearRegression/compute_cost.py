__author__ = 'Chris'

import numpy


def load(filename):
    content = numpy.loadtxt(filename, delimiter=",")
    x = content[:, 0]
    y = content[:, 1]

    return x, y


def compute_cost(x, y, theta):
    m = len(y)
    xData= attachOnesToColumn(x)

    hypothesis = numpy.dot(xData,theta)
    loss = hypothesis - y
    cost = numpy.sum(loss ** 2) / (2*m)

    return cost

def attachOnesToColumn(x):
    ones = numpy.ones((len(x),2))

    for i in range(0,len(x)):
        ones[i,1]=x[i]
    return ones
