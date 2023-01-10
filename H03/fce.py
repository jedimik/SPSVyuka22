
def mojeFce(r,s,znak="*"):
    for i in range(r):
        for j in range(s):
            print(f" {znak} ",end="")
        print()
    print()

if __name__=="__main__":
    mojeFce(5,10)
    mojeFce(2,8,"Ahoj")