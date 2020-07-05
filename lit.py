import os,re

def withh(data_1,data_2):
    with open("lit","w") as ff :
         ff.write(str(data_1)+'\n'+str(data_2))
                           
def mainl():
    path = 'bin\\'
    data_1 = {}
    data_2 = []
    for root,dirs,files in os.walk(path):
        for name in files:
            if re.match('main -liunx.py',name):
               abc = os.path.join(root,name)
               #print(abc)
               data_1[abc] = 'liunx'
               data_2.append(abc)
               #print(1)
            elif re.match('main -windows.py',name):
               abc = os.path.join(root,name)
               #print(abc)
               data_1[abc] = 'windows'
               data_2.append(abc)
               #print(2)
            elif re.match('main -lw.py',name):   
               abc = os.path.join(root,name)
               #print(abc)
               data_1[abc] = 'lw'
               data_2.append(abc)
               #print(3)
        for name in dirs:
             pass
    
    withh(data_1,data_2)      
def main():
   qp()
   mainl()   
if __name__ == '__main__':  
   
   mainl()
   
    
