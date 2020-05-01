
from sklearn.linear_model import LogisticRegression
import numpy as np
import array
import sys


def fit(X: list, y: list, sample_weight: list, X_shape_x: int, X_shape_y: int) -> int:

    """
    Fit the model according to the given training data.


    :param X: Training vector, where n_samples is the number of samples and
                    n_features is the number of features.
    :type X: array
    :param y: Target vector relative to X.
    :type y: array
    :param sample_weight: Array of weights that are assigned to individual samples.
                    If not provided, then each sample is given unit weight.
                    
                    .. versionadded:: 0.17
                       *sample_weight* support to LogisticRegression.
    :type sample_weight: array
    :param return: Fitted estimator.
    :type return: self
    
    """

    X = np.array(X).reshape(X_shape_x,X_shape_y)
    fit = LogisticRegression().fit(X, y, sample_weight)
    size_fit = sys.getsizeof(fit)

    return size_fit

