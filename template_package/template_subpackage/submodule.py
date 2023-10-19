"""
Module in subpackage.
"""
import matplotlib
from matplotlib import pyplot as plt
import numpy

def plot_data(data):
    x_axis = numpy.linspace(start=1,stop=5,step=5)
    y_axis = data
    plt.plot(x_axis,y_axis)
    plt.show()
