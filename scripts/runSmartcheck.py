import os

sourceDir = "/home/sunxun/data/sourcecode/"

# -> .sol
# sourcefiles = os.listdir(sourceDir)
# for fl in sourcefiles:
#     os.system("mv " + sourceDir + fl + " " + sourceDir + fl + ".sol")

sourcefiles = os.listdir(sourceDir)
resultDir = "/home/sunxun/data/results/res_smartcheck/"
for fl in sourcefiles:
    addr = fl.split('.')[0]
    print(addr)
    os.system("smartcheck -p " + sourceDir + fl + " >> " + resultDir + addr)
