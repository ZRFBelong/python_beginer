#/usr/bin/python3
# -*- encoding :utf-8
number = int(input("请输入你的猜测的数字:"))
print("你输入的数字是:{}".format(number))
if number == 5:
    print("good choice")
elif number == 10:
    print("what do you mean?")
elif number == 11:
    print("you did !")
else :
    print("what you have entered????")