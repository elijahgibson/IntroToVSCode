import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

##open source language, can use anyone's, extensive library, 
# plot will chart a line graph, 
## downside is no governance, when you install libraries on root python, they can step on each other's toes and cause errors
## that are difficult to decipher
## best practice is installing a virtual environment, creates folder which is copy of pyhton interpreter, can install all the libraries in that environment
## will be on quiz 1, create virtual environment and install third party libraries
## 1.Create a Virtual Environment
# top "new terminal", "py -3 -m venv introvenv" hit enter, will receive notification, will swith the interpreter to virtual environment
## switch will show on bottom, can see different interpreters, virtual environment is basically a file, python.exe is what it made copy of
## 2. Activate Virtual Environment
## introvenv --> scripts --> activate ".\introvenv\Scripts\activate"
## 3. Install 3rd party libraries in Environment
## make sure it has been selected (bottom right) and activated
## install command is "pip3 install"
## eg pip3 install matplotlib

## git is source control or version control
## source is  code, version could be videos, images, etc in addition to code, Git will take snapshot of it whenever you save it
## can review changes, accept it into main branch, so if they messed up can simply go back to a past version, git can keep track of there
## 


