import os
from shutil import *
#==================================================================================================
def lir(txt):
    "renvoi le contenu d'un fichier text sous forme d'une liste ou False si txt n'existe pas"
    r = []
    tmp = " "
    if (os.path.exists(txt) == True):
        f = open(txt)
        while (tmp != ""):
            tmp=f.readline()
            if (tmp==""):
                break
            else:
                r.append(tmp[0:len(tmp)-1])
        return r
    else:
        return False
#==================================================================================================
def cop(files,dest):
    "Copie files vers dest et renvoi True ou False si files n'existe pas"
    if (os.path.exists(files)==True):
        copyfile(files,dest)
        return True
    else:
        return False
#==================================================================================================
def sup(files):
    "Supprime files et renvoi True ou False si files n'existe pas"
    if (os.path.exists(files)==True):
        os.remove(files)
        return True
    else:
        return False
#==================================================================================================
