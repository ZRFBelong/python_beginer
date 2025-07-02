#/usr/bin/python3
# -*- encoding :utf-8
name = 'this is python script'
print(name)
print('hello,world'+'\t'+name)

# 转义字符表
# print("Hello\\World")      # 输出：Hello\World
# print('It\'s a test')      # 输出：It's a test
# print("He said, \"Hi\"")   # 输出：He said, "Hi"
# print("Beep\a")            # 触发蜂鸣声（可能无效）
# print("Hello\bWorld")      # 输出：HellWorld（删除了 o）
# print("Hello\tWorld")      # 输出：Hello    World（中间有 Tab）
# print("Line1\nLine2")      # 输出两行 Line1 和 Line2
# print("Hello\rWorld")      # 输出：World（覆盖前面内容） 
# print("Page1\fPage2")      # 换页（取决于终端支持）
# print("Line\vMore")        # 垂直 Tab（在某些终端中换行显示） 

print(r"this's a good test")
print("\"are you a good learner\"")
print(" \"yes,i\'m.\"")

print(name[:3])
print(name[:-1])
print(name[0:-1])
print(name[1:-1])
print(name[0])
print('C:\some\name')
print(r"C:\some\name")
print("hello,world",end="\n!")