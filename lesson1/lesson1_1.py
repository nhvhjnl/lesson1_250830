import random
t=random.randint(1,5)

while True:
    g=int(input("猜數字"))
    if g==t:
        print("正確")
        
        break
    elif g<t:
        print("太小")
    else:
        print("太大")
print("結束")