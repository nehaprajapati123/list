# grocery_list = ['flour','cheese','carrots']
# i=0
# while i<len(grocery_list):
#     print(i,':',grocery_list[i])          que1..................
#     i=i+1

# list1=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# while i<len(list1):
#     if type(list1[i])==list:
#         j=0
#         while j<len(list1[i]):
#             j=j+1
#         i=i+1              que2.............
#     print(list1[i][j])

# a= [6,1,3,5,6,3,1]
# i=0
# produact=1
# while i<len(a):
#     product=product*(a[i])
#     i=i+1
# print(product)                   que3....................


# list1= [1, 2, 2, 5, 8, 4, 4, 8]
# i=0
# list2=[]
# while i<len(list1):
#     if list1[i] not in list2:
#         list2.append(list1[i])
#     i=i+1
# j=0
# c=0
# while j<len(list2):
#         j=j+1
#         c=c+1
# print(c)       que5.................

# n1=[4,5,32,7,3,7,865,78,6,89,6,9]
# i=0
# n2=0
# while i<len(n1):
#     if n1[i]>n2:
#         n2=n1[i]
#     i=i+1
# print(n2)                  first max.................

# list1='neha is in navgurukul'       split function...........
# list1.split()
# print(list1)


        
# n=9119
# rev=0
# while n>0:
#     rem=n%10
#     rev=(rev*0)+rem**2
#     n=n//10
#     print(rev,end='')      question.11...........................



# list1 = [1,2,3,1,2,2]
# list2=[]
# i=0
# while i<len(list1):
#     if list1[i] not in list2:
#         list2.append(list1[i])
#     i=i+1
# print(list2)                   que24.....................

# i=10
# a=[]
# while i>0:
#     num=int(input('enter your number'))
#     a.append(num)
#     i=i-1
# num1=int(input('check no.is in list or not'))   

# if num1 in a:
#     print('present')
# else:
#     print('not,present')

# i=20
# a=[]
# while i>0:
#     num=int(input('enter your number'))
#     a.append(num)
#     i=i-1
# i=20
# positive=0
# negative=0
# even=0
# odd=0
# while i>=0:
#     if a[i]>0:
#         positive=positive+1
#         if a[i]%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#     else:
#         negative=negative+1
#         if a[i]%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#     i=i-1
# print(even,'even number')
# print(odd,'odd number')
# print(negative,'negative number')
# print(positive,'positive number')..................................

# i=0
# a=[]
# while i<10:
#     num=int(input('enter your number'))
#     a.append(num)
#     a.reverse()
#     i=i+1
# print(a) 

# output:-10,8,6,4,,2,1,3,5,7,9.........................

# i=5
# a=[]
# while i>0:
#     num=int(input('enter your number'))
#     a.append(num)
#     i=i-1
# print(a) 
# a.reverse()
# print(a)                      reverse list..............................

# list1=[1,2,3,4,5]
# i=0
# while i<len(list1):
#     sum=sum+(list1[i])
#     i=i+1
# print(sum)         ..................................

# list1=[1,2,3,4,5]
# i=0
# product=1
# while i<len(list1):
#     product=product*(list1[i])
#     i=i+1
# print(product)         .......................................

# l=[[1,2,3,4,5],[6,7,8,9]]
# i=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         print(l[i][j])
#         j=j+1
#     i=i+1                .......................................

# list1=[34,354,645,75]
# i=0
# sum=0
# c=0
# while i<len(list1):
#     sum=sum+list1[i]
#     i=i+1
#     c=c+1
# print(sum,'sum') 
# print(sum/c,'average')    ..........sum snd average


# list1=[34,354,645,75]
# i=0
# a=0
# while i<len(list1):
#     if list1[i]>a:
#         a=list1[i]
#     i=i+1
# print(a,'largest')   
    
# i1=0
# b=a
# while i1<len(list1):
#     if list1[i1]<b:
#         b=list1[i1]
#     i1=i1+1
# print(b,'smallest')...................largest ans smalllest

# list1=[123454321]
# i=0
# i1=-1
# while i<len(list1):
#     if list1[i]==list1[-i]:
#         print('yes palindrome')
#     else:
#         print('nor palimdrome')
#     i=i=1     ...........................palindrome

# n=[1,2,3,2,1,3,12,12,32]
# i=0
# m=[]
# while i<len(n):
#     if n[i] not in m:
#         m.append(n[i])
#     i=i+1
# print(m)..................repeat detetion...........

# n=[12,34,543,6567,876,878,67,89,34,5463,7,9]
# i=0
# m=[]
# while i<len(n):
#     if n[i]%2==0:
#         m.append(n[i])
#     else:
#         pass
#     i=i+1
# print(m)         .....................even number.................

# n=[1,2,3,[4,5],6,7,8,9]
# i=0
# m=[]
# while i<len(n):
#     j=0
#     while j<len(n):
#         if :
#             print(n[i][j])
#         else:
#             print(n[i])
#         j=j+1
#     i=i+1

#     i=i+1
    # j=0
    # while j<len(n):
    #     if n[i]==[]
        # print(n[i])
        # m.append(n[i][j])
        
        # print(n[i][j])
            # print(n[i])
    #     j=j+1
    # i=i+1
# print(m)

# a=5,7
# print(list(a))


            


