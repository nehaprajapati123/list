a=[1,2,3,4,[5,6,7,[8,9,10],11]]
sum=0
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type (a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    sum=sum+(a[i][j][k])
                    k=k+1
            j=j+1
    i=i+1
print(sum)
       
                 
                
