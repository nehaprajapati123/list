ch=['d eepa','tha pa','ne ha']
i=0
list1=[]
while i<len(ch):
    j=0
    s=''
    while j<len(ch[i]):
        if ch[i][j]==' ':
            pass
        else:
            s=s+ch[i][j]
        j=j+1
    i=i+1
    list1.append(s)
print(list1)