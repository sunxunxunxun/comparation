import os, json, ast
import variables

resDir = "/home/sunxun/data/results/"

def analyseOyente():
    resD =  resDir + "res_oyente/"
    resFls = os.listdir(resD)
    outfile = resDir + "oyente.txt"
    wf = open(outfile, 'w', encoding='utf-8')
    # print(len(resFls))
    for fl in resFls:
        print(fl)
        res = json.load(open(resD + fl, 'r', encoding='utf-8'))
        # print(res, res['vulnerabilities'])
        # print(type(res))
        vul = [0 for _ in range(7)]  
        vul[variables.OYNETE['evm_code_coverage']] = res['evm_code_coverage']
        vul[variables.OYNETE['callstack']] = int(res['vulnerabilities']['callstack'])
        vul[variables.OYNETE['reentrancy']] = int(res['vulnerabilities']['reentrancy'])
        vul[variables.OYNETE['integer_overflow']] = len(res['vulnerabilities']['integer_overflow'])
        vul[variables.OYNETE['integer_underflow']] = len(res['vulnerabilities']['integer_underflow'])
        vul[variables.OYNETE['time_dependency']] = int(res['vulnerabilities']['time_dependency'])
        vul[variables.OYNETE['money_concurrency']] = int(res['vulnerabilities']['money_concurrency'])
        
        
        vul = [str(_) for _ in vul]
        addr = fl.split('.')[0]
        # print(addr + '#' + '#'.join(vul))
        wf.write(addr + '#' + '#'.join(vul) + '\n')
    wf.close()

def analyseOsiris():
    resD = resDir + 'res_osiris/'
    resFls = os.listdir(resD)
    outfile = resDir + 'osiris.txt'
    wf = open(outfile, 'w', encoding='utf-8')
    
    for fl in resFls:
        print(fl)
        res = json.load(open(resD + fl, 'r', encoding='utf-8'))
        # print(res)
        vul = [0 for i in range(15)]    # 
        # print(vul)
        for k, v in res.items():
            if k not in variables.OSIRIS:
                continue
            # print(k, v)
            if type(v) is bool:
                vul[variables.OSIRIS[k]] = int(v)
            elif v.find('Opcode') > 0:
                # print(v)
                vul[variables.OSIRIS[k]] = v.count('Opcode')
                # print(vul[variables.OSIRIS[k]], variables.OSIRIS[k])
            else:  
                vul[variables.OSIRIS[k]] = v
        
        addr = fl.split('.')[0]
        # print(addr, vul)
        vul = [str(_) for _ in vul]    
        print(addr + '#' + '#'.join(vul))
        wf.write(addr + '#' + '#'.join(vul) + '\n')
    
    wf.close()


if __name__ == "__main__":
    analyseOyente()
    # analyseOsiris()