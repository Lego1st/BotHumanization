import os
import tarfile

#path is the location of the *.tar.gz file
def ExtractProfile(path) :
    tar = tarfile.open(path, "r:gz")
    tar.extractall()
    tar.close()