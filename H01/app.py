
def fce(pole2d):
    for i in range(0,len(pole2d),1):
        # if i!=2:
        for j in range(0,len(pole2d[i]),1):
            # if i <2:#nd j<4:
            #     if j<4:
            #         print(f"{pole2d[i][j]} ",end="")
            # elif i>2: # and j<3:
            #     if j<3:
            #         print(f"{pole2d[i][j]} ",end="")
            if i<3 and j<2:
                print(f"{pole2d[i][j]} ",end="")
            elif i>1 and j>2:
                print(f"{pole2d[i][j]} ",end="")
            else:
                print(f"  ",end="")
        print()

def fce2(pole2d):
    for i in range(0,len(pole2d),1):
        if i==0 or i > 2:
            for j in range(0,len(pole2d[i]),1):
                if i==0 and j<4:
                    print(f"{pole2d[i][j]} ",end="")
                elif i==3 and j<2:
                    print(f"{pole2d[i][j]} ",end="")
                elif i==4 and j>1:
                    print(f"{pole2d[i][j]} ",end="")
                else:
                    print(f"  ",end="")
        print()


def fce3(pole2d):
    for i in range(0,len(pole2d),1):
        for j in range(0,i+1,1):
            # if not (i==5 and j<3):
            print(f" {pole2d[i][j]} ",end=" ")
            # else:
            #     pass
                # print(f"    ",end="")
        print()

if __name__=="__main__":
    pole2d=[
    [5,4,6,1,2,9],
    [4,8,5,4,2,0],
    [1,9,8,5,4,1],
    [2,5,4,6,3,2],
    [4,2,3,6,7,5],
    [1,3,4,2,1,3]]
    # fce(pole2d)
    fce3(pole2d)