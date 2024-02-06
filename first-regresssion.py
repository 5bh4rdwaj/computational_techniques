import numpy as np
import matplotlib.pypilot as plt


def estimate_coef(x,y):
    # establishing number of obsevations
    n = np.size(x)

    # mean of x and y
    m_x =   np.mean(x)
    m_y = np.mean(y)
    