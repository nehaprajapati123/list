number=[1,2,3,[4,5,6],7]
i=0
sum=0
number2=[]
while i<len(number):
    if type(number[i])==list:
        j=0
        while j<len(number[i]):
            sum=sum+(number[i][j])
            j=j+1
    i=i+1
print(sum)
number2.append(number)
print(number2)
