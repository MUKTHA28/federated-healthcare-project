import numpy as np

def federated_average(weights):
    """
    weights = [(coef1, intercept1), (coef2, intercept2), ...]
    """

    avg_coef = np.mean([w[0] for w in weights], axis=0)
    avg_intercept = np.mean([w[1] for w in weights], axis=0)

    return avg_coef, avg_intercept
