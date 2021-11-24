que=[['how many states india have ?'],
['what is the capital of india?'],
['how many days there in feb in leap year?']]

opn=[[1.29,2.34,3.28,4.22]
,['1.bihar','2.delhi','3.mumbai','4.kolkata'],
[1.28,2.29,3.30,4.31]]
sol=[3,2,1]

opn2=[[1.29,2.28],['1.delhi','2.mumbai'],[1.29,2.28]]
sol2=[2,1,2]

c=1
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
    elif n==5050:
        if c==1:
            c=c+1
            k=0
            while k<len(opn2[i]):
                print(opn2[i][k])
                k=k+1
            m=int(input('enter your ans.'))
            if m==sol2[i]:
                print('congratulation')
            else:
                print('you  loss')
                break
        else:
            print('you alredy used')
            continue       
    else:
        print('you loss')
        break
    i=i+1
print('kbc done')
