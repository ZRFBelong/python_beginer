#/usr/bin/python3
# -*- encoding :utf-8
lista = [1,2,3,4,5,66]
listb = [66,5,4,3,2,1]
print(lista[0])
print(lista[0:5])
print(lista[-6])
#上述展示索引与切片 除此之外还有列表的拼接
print(listb)
print(lista+listb)
print("#"*50)

print(lista.append(777))
#上面仅仅输出了append方法的返回值
print(lista)

print(lista.pop())
#上面方法返回值为被弹栈（类似栈）出来的para
print(lista)

print(lista.clear())
#输出的是方法的返回值
print(lista)

print(listb.index(1))
print(listb.count(66))
print(listb.append(66))
print(listb.count(66))
print(len(listb))
print(listb.__add__([1,2,3,4,5,66]))


# 斐波那契数列：
# 前两项之和即下一项的值
a, b = 0, 1
while a < 10000:
    print(a,end='-')
    a, b = b, a+b