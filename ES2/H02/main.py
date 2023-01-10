a=5
b=6
print(a)
a=b
print(a)
b=10
print(a)
# c=int(input("ahoj"))
# print("V promenne A:"+str(a)+"  a v promenne B:"+str(b))
mojeprom=f"V promenne A:{a} a v promenne B:{b}"
mojeprom2="V promenne A:{} a v promenne B:{}".format(a,b)
mojeprom3="V promenne A:"+str(a)+"  a v promenne B:"+str(b)
print(mojeprom)

# Podminky
a=4
if a>5:
    print("A je vetsi nez 5")
elif a<5:
    print("a je mensi nez 6")
elif a==4:
    print("a je rovno 4")
else:
    print("A je cokoliv jineho")
if a==4:
    print("a je rovno 4")
if a<5:
    print("a je mensi nez 5")
# Cykly

# while True:
# i=0
# while True:
#     print(i)
#     i+=1
#     if(i>10000):
#         break

for i in range(0,10,1):
    print(i)
    
x=10
for i in range(x):
    print(i)

for i in range(0,5,1):
    for j in range(0,5,1):
        if j%2==0:
            print(j+1,end="")
        else:
            print(" ",end="")
    print()