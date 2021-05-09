import os

def count_contracts(lines):
    cont = 0
    for l in lines:
        if (l.find("contract")!=-1 or l.find("library")!=-1) and (l.find("{")!=-1) and (l.find("function") == -1):
            cont = cont+1

    return cont

if __name__ == '__main__':
    files = os.listdir("../../examples/todos/")
    result = 0
    for f in files:
        fp = open("../../examples/todos/"+f,"r")
        lines = fp.readlines()
        result = result+count_contracts(lines)
    print len(files)
    print result
    
