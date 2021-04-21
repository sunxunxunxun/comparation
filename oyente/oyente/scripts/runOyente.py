import os

evmCodeDir = "../evm_bytecode/"
resultDir = "../results/"
inputfiles = os.listdir(evmCodeDir)

for addr in inputfiles:
    bc = open(evmCodeDir + addr, 'r', encoding = 'utf-8').readline().strip()
    bcPath = evmCodeDir + addr
    print("=======>" + addr)
    os.system("python ../oyente/oyente.py -s " + bcPath + " -b -j")
    os.system("mv " + evmCodeDir + "*.json " + resultDir)
    