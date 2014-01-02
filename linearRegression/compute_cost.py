__author__ = 'Chris'

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def compute_cost(x, y, theta):
    m = len(y)
    xData = attachOnesToColumn(x)

    hypothesis = np.dot(xData, theta)
    loss = hypothesis - y
    cost = np.sum(loss ** 2) / (2 * m)
    return cost


def attachOnesToColumn(x):
    ones = np.ones((len(x), 2))

    for i in range(0, len(x)):
        ones[i, 1] = x[i]
    return ones


def gradient_descent(x, y, theta, alpha, iterations):
    xTrans = x.transpose()
    m = len(y)

    j_history = np.zeros(shape=(iterations, 1))
    for i in range(0, iterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        #works out sum of (h@(xi) - y(i)x(i))
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
        j_history[i] = cost

    newX, newY = generateGraphDataFromTheta(theta, len(x))

    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(1, 1, 1) # one row, one column, first plot
    ax.scatter(x[:, 1], y, color="red", marker="^")
    ax.plot(newX, newY, color="green")

    fig.savefig("superimposedLineOfBestFit.png")

    return j_history, theta


def generateGraphDataFromTheta(theta, lengthOfX):
    x = range(0, lengthOfX / 3)
    y = np.ones(lengthOfX / 3)
    y = (x * theta[1]) + theta[0]
    return x, y


def gradient_descent_with_scikit(x, y):
# Load the diabetes dataset

    regr = linear_model.LinearRegression()

    xT = x.reshape(len(x), 1)
    yT = y.reshape(len(y), 1)

    regr.fit(xT, yT)
    print('Coefficients regr: \n', regr.coef_)
    print('Intecept regr: \n', regr.intercept_)

    return regr.coef_,regr.intercept_

#Normal Equation is (X'X)^-1 * X'y
def normal_equation(xData, y):
    xTransposed = np.transpose(xData)
    xTransposeTimesX = np.dot(xTransposed,xData)
    xInv = np.linalg.inv(xTransposeTimesX)
    yMultipledByXTransposed = np.dot(xTransposed, y)
    answer=np.dot(xInv,yMultipledByXTransposed)
    return answer