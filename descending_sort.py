list=[]
n=int(input("enter number of elements "))
k=0
while k<n:
    element=int(input("enter your number "))
    list.append(element)
    k=k+1
i=0
while i<len(list):
    j=0
    while j<len(list):
        if list[i]>list[j]:
            a=list[i]
            list[i]=list[j]
            list[j]=a
            
            
        j=j+1
    i=i+1
print(list)