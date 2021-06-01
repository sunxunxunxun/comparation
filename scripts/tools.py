import os, pickle

dataDir = '/home/sunxun/data/'
resDir = dataDir + 'results/'

def getAddr(resfile):
    addrs = {}
    lines = []
    with open(resDir + resfile, 'r', encoding='utf-8') as rf:
        lines = rf.readlines()
    print(len(lines))
    for l in lines:
        l = l.strip()
        print(l.split('#')[0])
        addrs[l.split('#')[0]] = True
        
    return addrs
    

def getCommonAddr():
    mythAddr = getAddr('mythril.txt')
    osiAddr = getAddr('osiris.txt')
    oyeAddr = getAddr('oyente.txt')
    smtAddr = getAddr('smartcheck.txt')
    vandAddr = getAddr('vandal.txt')
    # print(smtAddr)
    addrlist = []
    wf = open(resDir + 'commonAddrs.txt', 'w', encoding='utf-8') 
    for addr in mythAddr:
        # print(addr)
        if (addr in osiAddr) and (addr in oyeAddr) and (addr in vandAddr):
            # print(addr)
            addrlist.append(addr)
            # write to commonAddrs.txt
            wf.write(addr + '\n')
    return addrlist

def matchSrcBc():
    bcDir = dataDir + 'bytecode/'
    totalSrcDir = dataDir + 'sourcecodes/'
    desSrcDir = dataDir + 'sourcecode/'
    addrs = os.listdir(bcDir)
    cnt = 0
    for addr in addrs:
        srcfile = totalSrcDir + addr
        if os.path.exists(srcfile):
            cnt += 1
            os.system('cp ' + srcfile + ' ' + desSrcDir)
    print(cnt)

def getLabel():
    


if __name__ == "__main__":
    cmnAddrs = getCommonAddr()
    print(len(cmnAddrs))
    
    # matchSrcBc()