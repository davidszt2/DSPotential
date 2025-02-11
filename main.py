"""
Main file to call functions and compute potential flow solutions

DSPotential
"""

from MeshTools import setupGrid, computeCp
from PotentialFlows.SourceSink import SourceSink
from PotentialFlows.Uniform import UniformFlow
from PotentialFlows.RankineSemiOval import RankineSemiOval
from PotentialFlows.RankineOval import RankineOval
import numpy as np
import matplotlib.pyplot as plt

# Create meshgrid
n = 200
xbounds = np.array([-2, 2])
ybounds = np.array([-1, 1])

X, Y = setupGrid(n, xbounds, ybounds)

# Create potential flow objects and get velocity fields
source1 = SourceSink(1.0, -0.5, 0.0)
source2 = SourceSink(1.0, -0.5, 0.0)
sink1 = SourceSink(-1.0, 0.5, 0.0)
uniform1 = UniformFlow(1.0, 0.0)
semiOval1 = RankineSemiOval(0.25, 1.0)
oval1 = RankineOval(3.0, 2.0, 1.0)

uSource1, vSource1 = source1.velocityField(X, Y)
uSource2, vSource2 = source2.velocityField(X, Y)
uSink1, vSink1 = sink1.velocityField(X, Y)
uUniform1, vUniform1 = uniform1.velocityField(X, Y)
uSemiOval1, vSemiOval1 = semiOval1.velocityField(X, Y)
uOval1, vOval1 = oval1.velocityField(X, Y)

plt.figure()
uTotal = uSource1 + uUniform1
vTotal = vSource1 + vUniform1
plt.streamplot(X, Y, uTotal, vTotal, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter(source1.x, source1.y, color='r', marker='o', s=80)

"""EXAMPLE 1: SOURCE FLOW"""
plt.figure()
plt.title("Example 1: Source")
plt.streamplot(X, Y, uSource1, vSource1, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter(source1.x, source1.y, color='r', marker='o', s=80)

"""EXAMPLE 2: SUPERPOSITION OF TWO SOURCES"""
plt.figure()
plt.title("Example 2: Source + Source")
uTotal = uSource1 + uSource2
vTotal = vSource1 + vSource2
plt.streamplot(X, Y, uTotal, vTotal, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter(source1.x, source1.y, color='r', marker='o', s=80)
plt.scatter(source2.x, source2.y, color='g', marker='o', s=80)

"""EXAMPLE 3: SUPERPOSITION OF SOURCES AND SINK (DOUBLET)"""
plt.figure()
plt.title("Example 3: Source + Sink")
uTotal = uSource1 + uSink1
vTotal = vSource1 + vSink1
plt.streamplot(X, Y, uTotal, vTotal, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter(source1.x, source1.y, color='r', marker='o', s=80)
plt.scatter(sink1.x, sink1.y, color='g', marker='o', s=80)

"""EXAMPLE 4: RANKINE OVAL (SOURCE + SINK + UNIFORM FLOW)"""
plt.figure()
plt.title("Example 4: Rankine Oval")
plt.streamplot(X, Y, uOval1, vOval1, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
contf = plt.contourf(X, Y, computeCp(uOval1, vOval1, oval1.uniform), levels=np.linspace(-2, 1, 100), extend='both')
plt.contour(X, Y, oval1.streamFunction(X, Y), levels=[-0.5, 0.0, 0.5], colors='r', linestyles='solid')
plt.colorbar(contf)
plt.scatter(source1.x, source1.y, color='r', marker='o', s=80)
plt.scatter(sink1.x, sink1.y, color='g', marker='o', s=80)

"""EXAMPLE 5: RANKINE SEMI-OVAL (SOURCE + UNIFORM FLOW)"""
plt.figure()
plt.title("Example 5: Rankine Semi-Oval")
plt.streamplot(X, Y, uSemiOval1, vSemiOval1, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
plt.scatter(semiOval1.sourceX, semiOval1.sourceY, color='r', marker='o', s=40)
plt.scatter(semiOval1.xSP, semiOval1.ySP, color='g', marker='o', s=40)
plt.contour(X, Y, semiOval1.streamFunction(X, Y), levels=[-semiOval1.sourceStrength/2, semiOval1.sourceStrength/2], colors='r', linestyles='solid')
plt.show()
