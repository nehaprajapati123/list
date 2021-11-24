n=[1,2,3,[4,5],6,7,8,9]
i=0
while i<len(n):
    if type(n[i])!=list:
        print(n[i],end=",")
    else:
        j=0
        while j<len(n[i]):
            if type(n[i])==list:
                print(n[i][j],end=",")
            j=j+1
    i=i+1
    
        