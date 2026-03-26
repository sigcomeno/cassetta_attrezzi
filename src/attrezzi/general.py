import sys
import os

#Trova il path sia se eseguito da terminale sia da eseguibile
def getpath():
    if getattr(sys, 'frozen',False):
        executable_path = sys.executable
        path = os.path.dirname(executable_path)
    else:
        path = os.path.dirname(__file__)
    return path
