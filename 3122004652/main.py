def readfile(address):
    f = open(address,'r',encoding='utf-8')   #设置文件对象
    p = f.read()
    f.close()
    return p