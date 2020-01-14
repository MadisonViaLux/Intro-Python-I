"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print (sys.argv)
for m in sys.argv:
    print('argument: ', m)
#https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv

# Print out the OS platform you're using:
# YOUR CODE HERE
import platform
print (platform.system() + platform.release(), "Version " + platform.version())
#https://stackoverflow.com/questions/1854/what-os-am-i-running-on

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
#https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
print(os.name)
# Print the current process ID
# YOUR CODE HERE
#print(os.getuid) <----- Work is here, but this doesn't work on Windows?
# Print the current working directory (cwd):
# YOUR CODE HERE
print("Looky here! " + os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
#print(os.uname) <----- Work is here, but this doesn't work on Windows?