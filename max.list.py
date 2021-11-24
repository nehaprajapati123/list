number=[50,40,23,70,56,12,5,10,7,89]
i=0                                
num=0
while i<len(number):
    if number[i]>num:
        num=num+1
        num=number[i]
    i=i+1
print(num,'is greater') 