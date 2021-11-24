que=[['how many states india have ?'],
['what is the capital of india?'],
['how many days there in feb in leap year?']]

opn=[[29,34,28,22]
,['1.bihar','2.delhi','3.mumbai','4.kolkata'],
[28,29,30,31]]
sol=[3,2,1]

"""  """
i=0
while i<len(que):
    print(que[i])
    j=0

    while j<len(opn[i]):
        print(opn[i][j])
        j=j+1 
    n=int(input('enter your  answwer'))
    if n==sol[i]:
        print('comgratulations')
    else:
        print('you loss')
        break
    i=i=1
print('kbc done')
