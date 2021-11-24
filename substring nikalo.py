mainstr='the quick brown fox  jumbed over the lazy dog the dog slept over the verandh'
a=''
substr='over'
d=mainstr.split()
i=0
while i<len(d):
    if d[i]==substr:
        a=a+" "
    else:
        a=a+d[i]+" "
    i=i+1
print(a)
mainstr='the quick brown fox jumbed over the lazy dog the dog slept over the verandh'
a=''
b='on'
substr='over'
d=mainstr.split()
i=0
while i<len(d):
    if d[i]==substr:
        a=a+b+" "
    else:
        a=a+d[i]+" "
    i=i+1
print(a)