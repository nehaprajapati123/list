elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
sum2=0
c=0
c1=0
c2=0
while i<len(elements):
    if elements[i]%2==0:
        sum1=sum1+elements[i]
        c1=c1+1
    else:
        sum2=sum2+elements[i]
        c2=c2+1
    c=c+1  
    sum=sum+elements[i]
    i=i+1

print(sum,'sum of list')
print(sum1,'sum of even no.')
print(sum2,'sum of odd no.')
print(c,'count of list')
print(c1,'count of even no.')
print(c2,'count of odd no.')
print(sum/c,'average of list')
print(sum1/c1,'average of even no.')
print(sum2/c2,'average of odd no.')
