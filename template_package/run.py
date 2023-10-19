""""
Run code from package and subpackage.
"""
import template_package
import template_package.template_subpackage

data = template_package.module.get_data()

template_package.template_subpackage.submodule.plpot_data(data)