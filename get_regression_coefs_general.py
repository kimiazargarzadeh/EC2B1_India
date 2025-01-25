import numpy as np

def get_regression_coefs(Y, *args):
    """
    Compute coefficients for trend regressions.

    Given a vector `Y` and a collection of regressors `*args`, return vector of coefficients `coefs`.

    Parameters
    ----------
    Y : (T,) array that will be the dependent variable. In our example, either GDP per capita in
    level or in logs.
    
    *args : N arrays of dimension (T,) that are the regressors. For example, the first array will be
    a (T,) array with elements of ones. 
    
    Note: *args is a convenient Python command to flexibly allow
    for different number of inputs into a function. That is, `get_regression_coefs(Y, x1, x2)` will
    give us args = `(x1, x2)` while `get_regression_coefs(Y, x1, x2, x3)` will give us args = `(x1,
    x2, x3)`. This allows us to use the same function for all different specifications.

    Returns
    -------
    coefs: This returns the array of coefficients. If we input two regressors (i.e. `x1` and `x2`),
    then coefs = `(a, b)`. If we input three regressors (i.e. `x1`, `x2`, and `x3`), then coefs =
    `(a, b1, b2)`. Ordering `x1` as the vector of ones ensures that `a` is the intercept.
    """
    
    T = len(args[0]) # The first element of args is x1. Its length should correspond to the number of time periods T in the sample.
    N = len(args) # The number of elements specified in *args corresponds to the number of inputs (i.e. if run `get_regression_coefs(Y, x1, x2)', then N = 2)

    X = np.empty((T, N)) # initialise the X data

    # in a for loop iterate through our regressors *args and fill in the X data
    for ix in range(N):
        x = args[ix] # extract our input array, i.e. for ix = 0 this will be x1 and our vector of ones
        X[:, ix] = x # fill the X data with our input arrays

        # Note: for a more elegant and more Pythonian solution see the enumerate() function.

    XX = X.T @ X # Construct X'X
    XY = X.T @ Y # Construct X'Y

    coefs = np.linalg.inv(XX) @ XY # solve for formula (X'X)^(-1) X'Y

    # Congratulations we just ran a regression.
    return coefs


