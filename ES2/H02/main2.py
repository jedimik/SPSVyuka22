# b=6
# a=b
# print(a)
# b=7
# print(a)
# b=[0,5,3,1]
# a=b.copy()
# print(a)
# b[0]=1000
# print(a)
a=5
b="hodnota"
# V a je <string b>:<a>
print("V a je "+b+": "+str(a))
print("V a je {}: {}".format(b,a))
print(f"V a je {b}: {a}")
b=10
# " B, ktere je:<10> je dvojnasobkem a, ktere je:<a>"
str0="B, ktere je:"+str(10)+" je dvojnasobkem a, ktere je:"+str(a);
str1="B, ktere je:{} je dvojnasobkem a, ktere je:{}".format(b,a);
str2=f"B, ktere je:{b} je dvojnasobkem a, ktere je:{a}"

print(str0,end="  ")
print(str1)
print(str2)
# If
# a=5
# if a>5:
#     print("A je vetsi nez 5")
# elif a==5:
#     print("A je rovno 5")
# elif a <6:
#     print("A je mensi nez 6")
# else:
#     print("A je cokoliv jineho")
# if a <6:
#     print("A je mensi nez 6 znova")
# if a==5:
#     print("A je rovno 5 znova")

# Cykly
# while True:
#     i=0
#     while True:
#         print(i)
#         i+=1
#         if i==10000:
#             break

for i in range(0,5,1):
    for j in range(5):
        print("*",end="")
    print()

for i in range(0,5,1):
    for j in range(5):
        print(j+1,end="")
    print()

for i in range(0,5,1):
    for j in range(5):
        if j%2==0:
            print(j+1,end="")
        else:
            print("   ",end="")
    print()