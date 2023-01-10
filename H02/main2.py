
# if __name__=="__main__":
# for i in range(0,5,1):
#     for j in range(5):
#         if j%2==1:
#             print("/",end="")
#         else:
#             print("*",end="")
#     print()

# for i in range(0,5,1):
#     for j in range(5):
#         if j%2==1 or i%2==1:
#             print("/",end="")
#         else:
#             print("*",end="")
#     print()
# print()
# a=5
# for i in range(0,a,1):
#     for j in range(a):
#         if i%2==1:
#             if j%2==1:
#                 print("/",end="")
#             else:
#                 print("/",end="")
#         else:
#             if j%2==1:
#                 print("/",end="")
#             else:
#                 print("*",end="")
#     print()
a=5
# for i in range(0,a,1):
#     for j in range(int(a/2)):
#         if i%2==1:
#             print(a-(j+1),end="")
#         else:
#             print(i,end="")
#     print()
# a=7
# for i in range(a):
#     for j in range(0,a,1):
#         if i%2==0:
#             print(j,end="")
#         else:
#             print(a-(j+1),end="")
#     print()

# a=7
# for i in range(a):
#     for j in range(0,a,1):
#         if i%2==0:
#             print(i,end="")
#         else:
#             print(a-(j+1),end="")
#     print()

a=5
for i in range(a):
    for j in range(0,a,1):
        if i==j:
            print(1,end="")
        else:
            print(0,end="")
    print()