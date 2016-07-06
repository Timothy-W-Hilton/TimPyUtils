"""module to implement standard error calculation, with optional
effective sample size adjustment of Wilks (1995)

REFERENCES

Wilks, D. (1995), Statistical Methods in the Atmospheric Sciences: An
Introduction, Academic Press, New York.
"""

import numpy as np
import pandas as pd


class MeanStdError(object):
    """class to implement standard error calculation on a numpy array
    """

    def __init__(self, arr):
        """Class constructor.

        arr (array-like): array of numeric values to calculate
           standard error of mean
        """

        self.arr = arr
        self.std_err = None
        self.neff = None
        self.std_err_neff = None

    def calc(self, dim=0):
        """calculate the standard error of the mean

        Calculate the standard error of the mean along a specified
        dimension of self.arr using equation (1) of Efron and Tibshirani
        (1991).  The standard error is placed in field std_err, the
        "effective sample size" standard error is placed in field
        std_err_neff, and the effective sample size is placed in field
        neff.  neff is calculated according to Wilks (1995).

        ARGS:
        dim (int): the dimension of self.arr along which the mean, standard error should be calculated
        adjust_n (boolean): if True, use the "effective sample size" of Wilks (1995) to account for autocorrelation in the data.

        REFERENCES:
        Efron, B. & Tibshirani, R., 1991.  Statistical Data Analysis in the Computer Age.  Science, 253, 5018, p 390- 395.
        Wilks, D., 1995 Statistical Methods in the Atmospheric Sciences: An Introduction.  Academic Press, New York
        """

        self.neff = calc_neff(self.arr, dim=dim)
        self.std_err = calc_std_err(self.arr, dim=dim)
        self.std_err_neff = calc_std_err(self.arr, dim=dim, n=self.neff)


def calc_std_err(arr, dim=0, n=None):
    """calculate standard error of the mean

    Calculates standard error of the mean for an array along a
    specified axis.  Uses the definition given by Efron and Tibshirani
    (1991) equation 1.

    ARGS:
    arr (array-like): numpy array of numeric values
    dim (int): the dimension of arr along which the effective sample size should be calculated.  Default is 0.
    n (array-like): value of n to be used for each element of arr along axis dim. Default is the number of elements along axis dim of arr (i.e. arr.shape[dim]).  That is, the default is to treat each element of arr as an independent data point.  A different value of n may be useful to, for example, account for autocorrelation in arr (see function calc_autocorr).

    RETURNS:
    A numpy array containing standard error of the mean along axis dim of arr.

    REFERENCES
    Efron, B. & Tibshirani, R., 1991.  Statistical Data Analysis in the Computer Age.  Science, 253, 5018, p 390- 395.
    """
    if n is None:
        n = arr.shape[dim]
    x_bar = np.mean(arr, axis=dim).squeeze()
    # calculate standard error according to Efron & Tibshirani (1991) eq 1.
    se = np.sqrt(np.sum(np.square(arr - x_bar), dim) / (n * (n - 1)))
    return se


def calc_neff(arr, dim=0):
    """calculate effective sample size accounting for lag-1 autocorrelation

    Effective sample size is calculated according to Wilks (1995).  If
    arr is multi-dimensional it is flattened first

    ARGS:
    arr (array-like): numpy array of numeric values
    dim (int): the dimension of arr along which the effective sample size should be calculated.  Default is 0.

    RETURNS:
    effective sample size accounting for lag-1 autocorrelation

    REFERENCES:
    Wilks, D., 1995 Statistical Methods in the Atmospheric Sciences: An Introduction.  Academic Press, New York
    """
    rho = calc_autocorr(arr, dim, lag=1)
    n = arr.shape[dim]
    neff = n * ((1 - rho) / (1 + rho))
    return neff


def calc_autocorr(arr, dim=0, lag=1):
    """calculate lag-1 autocorrelation along an array dimension

    ARGS:
    arr (array-like): numpy array of numeric values
    dim (int): the dimension of arr along which the autocorrelation should be calculated.  Default is 0.
    lag (int): lag to use for autocorrelation calculation.

    RETURNS:
    effective sample size accounting for lag-1 autocorrelation
    """
    rho = np.apply_along_axis(_autocorr_helper, axis=dim, arr=arr, lag=lag)
    return rho


def _autocorr_helper(arr1d, lag):
    """helper function for calc_autocorr.  Gets around the synactic
    problem of calling a method (autocorr) on the result of
    np.apply_along_axis.

    ARGS:
    arr (array-like): one-dimensional numpy array of numeric values
    lag (int): lag to use for autocorrelation calculation.

    RETURNS:
    A numpy array containing the lag-(lag) autocorrelation of arr1d
    """
    return pd.Series(arr1d).autocorr(lag=lag)
