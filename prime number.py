number=[2,7,4,3,5,13,17,27]
i=0
c=0
a=1
while i<len(number):
    while a<=number[i]:
        if number[i]%a==0:
            if c<3:
                c=c+1
                a=a+1
        if c==2:
                print(number[i],'is not prime number')

        else:
                print(number[i],' prime number')
        i=i+1
