elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum1=0
sum2=0
c1=0
c2=0
while i<len(elements):
    if elements[i]%2==0:
        sum1=sum1+elements[1]
        c1=c1+1
    else:
        sum2=sum2+elements[i]
        c2=c2+1
    i=i+1
print(sum1/c1,'average of even no.')
print(sum2/c2,'average of odd no.')
    
