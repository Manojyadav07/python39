a1=input()
b1=len(a1)
c1="".join(a1[i:i+2][::-1] for i in range (0,b1,2))
print (c1)

