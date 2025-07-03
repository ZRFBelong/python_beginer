#/usr/bin/python3
# -*- encoding :utf-8
lista = ["lily","lucy","lilei","boy"]

for i in lista:
#    print(i,end='-\n')
    print(i+'-'+str(len(i)))

dictory ={1:"apple",2:"orange",3:"grape",4:"melon",5:"peal"}
for i,j in dictory.copy().items():
    print(i,j)
dictory2={}
for i,j in dictory.copy().items():
    dictory2[i] = j
    print(i,dictory2[i])
