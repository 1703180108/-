import random
c = random.randint(0,1000)
print(c)
s = int(input("请输入一个数字："))
print(s)
i = 1
while s != c:
     if s > c:
        print("大了")
     elif s < c:
        print("小了")
     s = int(input("请输入一个字数："))
     i+=1
print("猜中的次数：",i)
