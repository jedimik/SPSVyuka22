# for i in range(0,5,1):
#     for j in range(0,5,1):
#         if i%2 == 0:
#             if j%2==1:
#                 print(j,end="")
#             else:
#                 print("*",end="")
# #       if i%2==0 and j%2==1:
# #           print(j,end="")
# #       elif i%2 ==0 and j%2==0:
# #           print("*",end="")
#         else:
#             print(i,end="")
#     print()

# for i in range(0,5,1):
#     for j in range(0,i+1,1):
#         print("*",end="")
#     print()

a=7
def fce(a):
    for i in range(0,a,1):
        for j in range(0,2*a-1,1):
            if j < a-(i*1):
                print(" ",end="")
        for j in range(0,1+(i*2),1):
                print("*",end="")
        print()
    for i in range(0,int(a/5)+1,1):
        for i in range(0,2*a,1):
            if i >= a-1 and i <= a+1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

listik=[0,3,4,5,2,6,8,9]

def hledej(a:int,listik:list):
    '''
        Fce mi podle vstupni hodnoty a rekne, zdali se tam toto cislo nachazi a na jakem 
        indexu
        Args:
            a(int): Input number to find in a list
            listik(list): Input list for searching
        Returns
            bool and position of number (if number exists)
    '''
    pass

if __name__=="__main__":
    # fce(11)
    pass