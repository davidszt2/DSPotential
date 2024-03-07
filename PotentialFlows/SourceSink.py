"""
Source/Sink Flow Class

DSPotential
"""

import numpy as np

class SourceSink():
    def __init__(self, strength, x, y):
        """
        Initializes the source/sink

        Parameters
        ----------
        strength: float
            Strength of the source/sink (positive if source, negative if sink)
        x: float
            x-coordinate of the source/sink
        y: float
            y-coordinate of the source/sink
        """
        self.strength = strength
        self.x = x
        self.y = y

    def velocityPotential(self, X, Y):
        """
        Returns the velocity potential of the source/sink

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        psi: ndarray
            Velocity potential of the source/sink
        """
        psi = self.strength / (2 * np.pi) * np.log(np.sqrt((X - self.x)**2 + (Y - self.y)**2))
        return psi
    
    def streamFunction(self, X, Y, c=0):
        """
        Returns the stream function of the source/sink

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid
        c: ndarray (optional)
            Constant to add to the stream function (default = 0)

        Returns
        -------
        psi: ndarray
            Stream function of the source/sink
        """
        psi = self.strength / (2 * np.pi) * np.arctan2((Y - self.y), (X - self.x)) + c
        return psi
    
    def velocityField(self, X, Y):
        """
        Returns the velocity field of the source/sink

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        u: ndarray
            x-component of the velocity field
        v: ndarray
            y-component of the velocity field
        """
        u = self.strength / (2 * np.pi) * (X - self.x) / ((X - self.x)**2 + (Y - self.y)**2)
        v = self.strength / (2 * np.pi) * (Y - self.y) / ((X - self.x)**2 + (Y - self.y)**2)
        return u, v
    