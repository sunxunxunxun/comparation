import os, json
import variables

resDir = "/home/sunxun/data/results/"

def analyseOyente():
    resD =  resDir + "res_oyente/"
    resFls = os.listdir(resD)
    outfile = resDir + "oyente.txt"
    for fl in resFls:
        res = json.load(open(resD + fl, 'r', encoding='utf-8').read())
        print(res)
        vul = [0,0,0,0,0,0,0]

