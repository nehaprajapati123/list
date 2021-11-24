elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum1=0
sum2=0
while i<len(elements):
    if elements[i]%2==0:
        sum1=sum1+elements[i]
    else:
        sum2=sum2+elements[i]
    i=i+1
print(sum1,'sum of even no.')
print(sum2,'sum of odd no.')