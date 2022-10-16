# Module is basically just a python file that we can import into another python file
# Python modules: https://docs.python.org/3/py-modindex.html
# There are built-in and external modules (the same folder where python is installed)
# Source code of external modules is included at the top: https://docs.python.org/3/library/base64.html#module-base64
# If no path to the source code, the module is built-in
# To install additional external libraries use e.g. https://python-docx.readthedocs.io/en/latest/user/install.html
# Use pip for installation - package manager
import keyword
import includes as inc  # include local file


print(inc.roll_dice(22))
print(keyword.iskeyword("def"))
