import numpy as np

def lsq(X, y):
    """
    Least squares linear regression
    :param X: Input data matrix
    :param y: Target vector
    :return: Estimated coefficient vector for the linear regression
    """

    # add column of ones for the intercept
    ones = np.ones((len(X), 1))
    X = np.concatenate((ones, X), axis=1)

    # calculate the coefficients
    beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))

    return beta

def mean_squared_error(X, y, beta):
    """
    Calculate the mean squared error of the model
    :param X: Input data matrix
    :param y: Target vector
    : beta: Estimated coefficient vector for the linear regression
    :return: Mean squared error
    """
    ones = np.ones((len(X), 1))
    X = np.concatenate((ones, X), axis=1)

    mse= np.mean((y-X*np.transpose(beta))**2)

    return mse




