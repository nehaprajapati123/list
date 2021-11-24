list1= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
while i<len(list1):
    if list1[i]=='a':
        c1=c1+1
    elif list1[i]=='n':
        c2=c2+1
    elif list1[i]=='t':
        c3=c3+1
    elif list1[i]=='x':
        c4=c4+1
    elif list1[i]=='u':
        c5=c5+1
    elif list1[i]=='g':
        c6=c6+1
    i=i+1
print( 'a-',c1 )
print( 'n-',c2)
print( 't-',c3)
print('x-' ,c4 )
print( 'u-',c5 )
print( 'g-',c6 )    