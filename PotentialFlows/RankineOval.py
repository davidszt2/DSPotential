"""
Rankine Oval Class

DSPotential
"""

import numpy as np
from PotentialFlows.SourceSink import SourceSink
from PotentialFlows.Uniform import UniformFlow

class RankineOval():
    def __init__(self, sourceSinkStrength, sourceSinkDistance, uniformStrength, uniformAngle=0):
        """
        Initializes the Rankine Oval
        """
        
        self.sourceSinkStrength = sourceSinkStrength
        self.sourceSinkDistance = sourceSinkDistance
        self.uniformStrength = uniformStrength
        self.uniformAngle = uniformAngle
        
        self.source = SourceSink(sourceSinkStrength, -sourceSinkDistance/2, 0)
        self.sink = SourceSink(-sourceSinkStrength, sourceSinkDistance/2, 0)
        self.uniform = UniformFlow(uniformStrength, uniformAngle)
        
    def velocityPotential(self, X, Y):
        """
        Returns the velocity potential of the Rankine Oval

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        psi: ndarray
            Velocity potential of the Rankine Oval
        """
        sourcePotential = self.source.velocityPotential(X, Y)
        sinkPotential = self.sink.velocityPotential(X, Y)
        uniformPotential = self.uniform.velocityPotential(X, Y)
        
        psi = sourcePotential + sinkPotential + uniformPotential
        return psi
    
    def streamFunction(self, X, Y):
        """
        Returns the stream function of the Rankine Oval

        Parameters
        ----------
        X: ndarray
            X array of meshgrid
        Y: ndarray
            Y array of meshgrid

        Returns
        -------
        psi: ndarray
            Stream function of the Rankine Oval
        """
        sourceStream = self.source.streamFunction(X, Y)
        sinkStream = self.sink.streamFunction(X, Y)
        uniformStream = self.uniform.streamFunction(X, Y)
        
        psi = sourceStream + sinkStream + uniformStream
        return psi
    
    def velocityField(self, X, Y):
        """
        Returns the velocity field of the Rankine Oval

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
        uSink, vSink = self.sink.velocityField(X, Y)
        uUniform, vUniform = self.uniform.velocityField(X, Y)
        
        u = uSource + uSink + uUniform
        v = vSource + vSink + vUniform
        
        return u, v
    