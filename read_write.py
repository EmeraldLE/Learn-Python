f=open('write_9x9.txt','w')
for i in [1,2,3,4,5,6,7,8,9]:
    for j in [1,2,3,4,5,6,7,8,9]:
        f.write(str(j)+"x"+str(i)+"="+str(i*j)+" ")
    f.write("\n")
f.close()

f=open('write_9x9.txt','r')
print(f.read())
f.close()

f=open('write_9x9.txt','r')
print(f.read(54))
f.close()





