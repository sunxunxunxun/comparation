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
    cmnAddrs = open(resDir + 'commonAddrs.txt', 'r', encoding='utf-8').readlines()
    cmnAddrs = [_.strip() for _ in cmnAddrs]
    print(len(cmnAddrs))
    addr2label = pickle.load(open('/home/sunxun/classification/pydata/addr2label.dict', 'rb'))
    
    wf = open(resDir + 'cmnAddrsWithLabel.txt', 'w', encoding='utf-8')
    cnt = [0 for range(7)]
    for addr in cmnAddrs:
        if addr in addr2label:
            l = addr + '#' + str(addr2label[addr])
        else:
            l = addr + '#-1'
        print(l)
        wf.write(addr + '\n')
    
    wf.close()



if __name__ == "__main__":
    # 获取5个工具共同分析的合约, 并写入到commonAddrs.txt
    # cmnAddrs = getCommonAddr()
    # print(len(cmnAddrs))
    
    # 获取与bytecode相匹配的srccode文件（因为smartcheck分析的是src，其它分析bytecode
    # matchSrcBc()
    
    # 获取commonaddrs的类别label, 并在commonAddrs.txt中显示 
    getLabel()