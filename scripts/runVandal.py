import os

btcDir = "/home/sunxun/data/bytecode/"
resultDir = "/home/sunxun/data/results/res_vandal/"

btcFls = os.listdir(btcDir)
resFls = os.listdir(resultDir)
vis = {}
for add in resFls:
    vis[add] = True

for btc in btcFls:
    if btc in vis:
        continue

    # record problem block
    reentrantCall = []
    originUsed = []
    checkedCallStateUpdate = []
    uncheckedCall = []
    unsecuredValueSend = []
    destroyable = []

    os.system("../bin/analyze.sh " + btcDir + btc + " ../datalog/demo_analyses.dl")

    with open("reentrantCall.csv", 'r', encoding = 'utf-8') as rf:
        lines = rf.readlines()
        for l in lines:
            reentrantCall.append(l.strip())
    with open("originUsed.csv", 'r', encoding = 'utf-8') as rf:
        lines = rf.readlines()
        for l in lines:
            originUsed.append(l.strip())
    with open("checkedCallStateUpdate.csv", 'r', encoding = 'utf-8') as rf:
        lines = rf.readlines()
        for l in lines:
            checkedCallStateUpdate.append(l.strip())
    with open("uncheckedCall.csv", 'r', encoding = 'utf-8') as rf:
        lines = rf.readlines()
        for l in lines:
            uncheckedCall.append(l.strip())
    with open("unsecuredValueSend.csv", 'r', encoding = 'utf-8') as rf:
        lines = rf.readlines()
        for l in lines:
            unsecuredValueSend.append(l.strip())
    with open("destroyable.csv", 'r', encoding = 'utf-8') as rf:
        lines = rf.readlines()
        for l in lines:
            destroyable.append(l.strip())

    print(reentrantCall, originUsed, checkedCallStateUpdate, uncheckedCall, unsecuredValueSend, destroyable)

    with open(resultDir + btc, 'w', encoding='utf-8') as wf:
        wf.write("reentrantCall:" + ','.join(reentrantCall) + "\n")
        wf.write("originUsed:" + ','.join(originUsed) + "\n")
        wf.write("checkedCallStateUpdate:" + ','.join(checkedCallStateUpdate) + "\n")
        wf.write("uncheckedCall:" + ','.join(uncheckedCall) + "\n")
        wf.write("unsecuredValueSend:" + ','.join(unsecuredValueSend) + "\n")
        wf.write("destroyable:" + ','.join(destroyable) + "\n")

    os.system("rm *.csv")