import os

bcDir = "/home/sunxun/data/bytecode/"
resultDir = "/home/sunxun/data/results/res_mythril/"

bcfiles = os.listdir(bcDir)

for addr in bcfiles:
    inputfl = bcDir + addr
    outputfl = resultDir + addr
    os.system("myth analyze a -f " + inputfl + " -o json | tee " + outputfl)

