def tri1(a):
    for i in range(1,a+1,1):
        for j in range(1,i+1,1):
            print("*",end="")
        print(" ")
def tri2(b):
    for i in range(1,b+1,1):
        for j in range(1,b-i+1,1):
            print(" ",end="")
        for k in range(1,i+1,1):
            print("*",end="")
        print(" ")
def tri3(c):
    if(c%2==0):
        x=int(c/2)
    else:
        x=int(c/2)+1
    p=0
    for i in range(1,x+1,1):
        for j in range(1,x-i+1,1):
            print(" ",end="")
        for k in range(1,i+1+p,1):
            print("*",end="")
        p=p+1
        print(" ")
def tri4(d):
    p=0
    for i in range(1,d+1,1):
        for j in range(1,d-i+1,1):
            print(" ",end="")
        for k in range(1,i+1+p,1):
            print("*",end="")
        p=p+1
        print(" ")
def tri5(e):
    p=0
    for i in range(1,e+1,1):
        for j in range(1,e-i+1,1):
            print(" ",end="")
        for k in range(1,i+1+p,1):
            print("*",end="")
        p=p+1
        print(" ")
    p=p-1
    for i in range(e-1,0,-1):
        for j in range(1,e+1-i,1):
            print(" ",end="")
        for k in range(1,i+p,1):
            print("*",end="")
        p=p-1
        print(" ")


line=input("lines=")
tri1(int(line))
print("\n")
tri2(int(line))
print("\n")
tri3(int(line))
print("\n")
tri4(int(line))
print("\n")
tri5(int(line))
