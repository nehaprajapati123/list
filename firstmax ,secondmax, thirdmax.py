n1=[5,40,23,70,56,12,5,10,7,89 ,90]
i=0
n2=0
n3=0
n4=0
while i<len(n1):
    if n1[i]>n2:
        n4=n3
        n3=n2
        n2=n1[i]
    i=i+1
print(n2,'largest number')
print(n3,'second largest')
print(n4,'third largest')