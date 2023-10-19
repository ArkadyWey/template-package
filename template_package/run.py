""""
Run code from package and subpackage.
"""
import numpy

import module
import template_subpackage.submodule

data = module.get_data()

template_subpackage.submodule.plot_data(data)