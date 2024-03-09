"""
Tools to set up meshing and potential distributions

DSPotential
"""

import numpy as np
from PotentialFlows.Uniform import UniformFlow

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

def computeCp(u, v, uniformFlow:UniformFlow):
    """
    Returns the pressure coefficient distribution
    
    Parameters
    ----------
    u: ndarray
        x-component of the velocity field
    v: ndarray
        y-component of the velocity field
    uniformFlow: UniformFlow
        UniformFlow object
    
    Returns
    -------
    Cp: ndarray
        Pressure coefficient distribution
    """
    Cp = 1 - (u**2 + v**2) / uniformFlow.strength**2
    return Cp
