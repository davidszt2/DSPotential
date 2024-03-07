"""
Uniform Flow Class

DSPotential
"""

import numpy as np

class UniformFlow():
    def __init__(self, strength, angle):
        """
        Initializes the uniform flow

        Parameters
        ----------
        strength: float
            Strength of the uniform flow
        angle: float
            Angle of the uniform flow
        """
        self.strength = strength
        self.angle = angle
        
    def velocityPotential(self, X, Y):
        """
        Returns the velocity potential of the uniform flow

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        psi: ndarray
            Velocity potential of the uniform flow
        """
        psi = self.strength * (X * np.cos(self.angle) + Y * np.sin(self.angle))
        return psi
    
    def streamFunction(self, X, Y, c=0):
        """
        Returns the stream function of the uniform flow

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
            Stream function of the uniform flow
        """
        psi = self.strength * (X * np.sin(self.angle) - Y * np.cos(self.angle)) + c
        return psi
    
    def velocityField(self, X, Y):
        """
        Returns the velocity field of the uniform flow

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        u: ndarray
            x-component of the velocity of the uniform flow
        v: ndarray
            y-component of the velocity of the uniform flow
        """
        u = self.strength * np.cos(self.angle) * np.ones(np.shape(X))
        v = self.strength * np.sin(self.angle) * np.ones(np.shape(Y))
        return u, v
    