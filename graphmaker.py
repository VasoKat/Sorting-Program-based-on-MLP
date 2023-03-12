#//Vasiliki Katogianni 
from matplotlib import pyplot as plt
with open('thirdcomb.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line[0]=="E" or line=="\n":
            continue
        if line[0]=="P":
            break
        line.strip()
        lineElements=line.split(',')
        x1=float(lineElements[0])
        x2=float(lineElements[1])
        category=float(lineElements[2])
        if category==1:
            plt.plot(x1,x2,marker='+',color='magenta')
        elif category==2:
            plt.plot(x1,x2,marker='+',color='green')
        elif category==3:
            plt.plot(x1,x2,marker='+',color='cyan')
        else:
            plt.plot(x1,x2,marker='+',color='red')
plt.show()
