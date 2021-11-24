a=[1,2,3,4,[5,6,7,[8,10],11]]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type (a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    if 9 in (a[i][j]):
                        k=k+1
                    else:
                        print("not present")
            j=j+1
    i=i+1
print(9,"yes present")
