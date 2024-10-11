# Nejde
# python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip

# instalace balicku
# python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade Flask

import pip
import numpy
import cv2

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)