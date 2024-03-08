"""
Rankine Semi-Oval Class

DSPotential
"""

import numpy as np
from PotentialFlows.SourceSink import SourceSink
from PotentialFlows.Uniform import UniformFlow


class RankineSemiOval():
    def __init__(self, ovalHalfHeight, uniformStrength, uniformAngle=0, sourceX=0, sourceY=0):
        """
        Initializes the Rankine Oval
        """
        self.ovalHalfHeight = ovalHalfHeight
        self.uniformStrength = uniformStrength
        self.sourceX = sourceX
        self.sourceY = sourceY
        
        self.source = SourceSink(uniformStrength, sourceX, sourceY)
        self.uniform = UniformFlow(uniformStrength, uniformAngle)
        
    def velocityPotential(self, X, Y):
        """
        Returns the velocity potential of the Rankine Semi-Oval

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        psi: ndarray
            Velocity potential of the Rankine Semi-Oval
        """
        sourcePotential = self.source.velocityPotential(X, Y)
        uniformPotential = self.uniform.velocityPotential(X, Y)
        
        psi = sourcePotential + uniformPotential
        return psi
    
    def streamFunction(self, X, Y):
        """
        Returns the stream function of the Rankine Semi-Oval

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        psi: ndarray
            Stream function of the Rankine Semi-Oval
        """
        sourceStream = self.source.streamFunction(X, Y)
        uniformStream = self.uniform.streamFunction(X, Y)
        
        psi = sourceStream + uniformStream
        return psi
    
    def velocityField(self, X, Y):
        """
        Returns the velocity field of the Rankine Semi-Oval

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
        uSource, vSource = self.source.velocityField(X, Y)
        uUniform, vUniform = self.uniform.velocityField(X, Y)
        
        u = uSource + uUniform
        v = vSource + vUniform
        return u, v