n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
list1=[]
while i<len(n):
    c=0
    j=0
    list2=[]
    while j< len(n):
        if n[i]==n[j]:
            c=c+1
        j=j+1
    list2.append(n[i])
    list2.append(c)
    if list2 not in list1:
       list1.append(list2)
    i=i+1
print(list1)


n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
list1=[]
while i<len(n):
    j=0
    c=0
    list2=[]
    while j<len(n):
        if n[i]==n[j]:
            c=c+1
        j=j+1
    list2.append(n[i])
    if list2 not in list1:
        list1.append(list2)
    i=i+1
print(list1)


