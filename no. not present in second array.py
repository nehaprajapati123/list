list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
list3=[]
i=0
while i<len(list1):
    if list1[i] in list2:
        pass
    else:
        list3.append(list1[i])
    i=i+1     
print(list3)