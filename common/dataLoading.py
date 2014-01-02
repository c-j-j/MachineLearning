__author__ = 'Chris'
import numpy as np

def load(filename):
    data = np.loadtxt(filename, delimiter=",")
    numberOfColumns = data.shape[1]
    X = data[:, :numberOfColumns-1]
    y = data[:, numberOfColumns-1]
    return X, y