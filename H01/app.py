
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
        if i<3:
            for j in range(0,len(pole2d[i]),1):
                if j<4:
                    print(f"{pole2d[i][j]} ",end="")
        print()


if __name__=="__main__":
    pole2d=[
    [5,4,6,1,2],
    [4,8,5,4,2],
    [1,9,8,5,4],
    [2,5,4,6,3],
    [4,2,3,6,7]]
    # fce(pole2d)
    fce2(pole2d)