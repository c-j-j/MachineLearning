from math import e, log
import numpy as np
import pylab as pl
from numpy.ma import transpose
from sklearn import linear_model


def sigmoid(X):
    return 1 / (1 + e ** (-1.0 * X))


def computeCost(X, y, showGraph=True):
    logreg = linear_model.LogisticRegression(C=1e8)
    logreg.fit(X,y)

    h=0.2
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    pl.figure(1, figsize=(4, 3))
    pl.pcolormesh(xx, yy, Z, cmap=pl.cm.Paired)

    # Plot also the training points
    pl.scatter(X[:, 0], X[:,1], c=y, edgecolors='k', cmap=pl.cm.Paired)
    pl.xlabel('X1')
    pl.ylabel('X2')
    pl.xticks(())
    pl.yticks(())

    if showGraph:
        pl.show()

    # we create an instance of Neighbours Classifier and fit the data.
    return logreg
