a=[[1,2,4,5,6,7],[8,60,11,9]]
i=0
sum=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        sum=0
        while j<len(a[i]):
            sum=sum+(a[i][j])
            j=j+1
        i=i+1
    b.append(sum)
print(b)
      
    

    

