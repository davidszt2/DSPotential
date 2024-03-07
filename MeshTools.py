"""
Tools to set up meshing and potential distributions

DSPotential
"""

import numpy as np

def setupGrid(n, xbounds, ybounds):
    """
    Returns a set of x and y coordinates (meshgrid)
    
    Parameters
    ----------
    n: float
        Number of points in the meshgrid
    xbounds: ndarray
        x-axis bounds of the meshgrid (e.g.: [-2, 2])
    ybounds: float
        y-axis bounds of the meshgrid (e.g.: [-2, 2])
    
    Returns
    -------
    X: ndarray
        X array of meshgrid
        
    Y: ndarray
        Y array of meshgrid
    """
    
    x_min, x_max = xbounds
    y_min, y_max = ybounds
    
    x = np.linspace(x_min, x_max, n)
    y = np.linspace(y_min, y_max, n)
    
    X, Y = np.meshgrid(x, y)
    
    return X, Y
