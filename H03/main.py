a=int(input("Zadej hodnotu\n"))
b=int(input("Zadej hodnotu\n"))
# print(a)
# print(type(a))
c=(2*a+b*3)/2
for i in range(4):
    print(c)

#Uloha 4
# if c%3== 1 or c%3==0:
if c%3<2:
    r=int(a/2)
else:
    r=a
s=int(c/2)
# Uloha 5
for i in range(r):
    for j in range(0,s):
        if i%2==0:
            print(i,end="")
        else:
            if j%2==0:
                print("*",end="")
            else:
                print(j+1,end="")
    print()