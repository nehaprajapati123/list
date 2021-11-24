list1=[79,2,4,2,56,45,35]
i=0
list2=[]
while i<len(list1):
    j=0
    while j<len(list1):
        if list1[i]>=list1[j]:
            list2.append(list1[i])
            j=j+1
        i=i+1
print(list2)
