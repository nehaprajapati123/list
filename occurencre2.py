list1=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
list2=[]
i=0
while i<len(list1):
    list3=[]
    c=0
    j=0
    while j<len(list1):
        if list1[i]==list1[j]:
            c=c+1
        j=j+1
    list3.append(list1[i])
    list3.append(c)
    if list3 not in list2:
        list2.append(list3)
    i=i+1
print(list2)
        
