import os

srcDir = "bytecode/"
resultsDir = "results/"

srcFls = os.listdir(srcDir)

for src in srcFls:
    os.system("python osiris/osiris.py -s " + srcDir + src + " -b -j")