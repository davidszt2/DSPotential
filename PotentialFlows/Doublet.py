"""
Doublet Class

DSPotential
"""

class Doublet():
    def __init__(self, strength, x, y):
        """
        Initializes the doublet

        Parameters
        ----------
        strength: float
            Strength of the doublet
        x: float
            x-coordinate of the doublet
        y: float
            y-coordinate of the doublet
        """
        self.strength = strength
        self.x = x
        self.y = y
        
    def velocityPotential(self, X, Y):
        """
        Returns the velocity potential of the doublet
        """
        pass