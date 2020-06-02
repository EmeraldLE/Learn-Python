import numpy as np

print("one dimensional array :")
x=np.array([1.0, 2.0, 3.0])
y=np.array([2.0, 4.0, 6.0])

print(x)
print("type="+str(type(x)))

print("x+y="+str(x+y))
print("x-y="+str(x-y))
print("x*y="+str(x*y))
print("x/y="+str(x/y))
print("x/2.0="+str(x/2.0))

print("\n")
print("two dimensional array :")
A=np.array([[1,2],[3,4]])
B=np.array([[3,0],[6,0]])

print(A)
print("type="+str(A.dtype))
print("shape="+str(A.shape))

print("A+B="+str(A+B))
print("A*B="+str(A*B))
print("A*10="+str(A*10))

print("\n")
print("broadcast :")
C=np.array([10,20])
print("A*C="+str(A*C))

print("\n")
print("access elements :")
w=np.array([[51,55],[14,19],[0,4]])
print(w)
print("w[0]="+str(w[0]))
print("w[0][1]="+str(w[0][1]))
print("all row of w :")
for row in w:
    print(row)

print("\n")
print("two dimensional array to one :")
w=w.flatten()
print(w)
print("w[0,2,4]="+str(w[np.array([0,2,4])]))
print("w>15="+str(w>15))
print("w[w>15]="+str(w[w>15]))