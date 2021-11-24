#creating list:-
names=["neha",'arti','sai','neetu','ruby','shally']
#print(names)

number=[1,3,5,3,5,74,67,4,7,5,6,54,54,675]
#print(number)
#print(number[7])

fruits=['apple','banana','grapes','orange']
#print(fruits)
#print(fruits[3])


#access list:-................................................................
names=["neha",'arti','sai','neetu','ruby','shally']
#print(names[4])
#print(names[5])
#print(names[-3])

#negative indexing:-...............................................................
names=["neha",'arti','sai','neetu','ruby','shally']
#print(names[-3])
fruits=['apple','banana','grapes','orange']
#print(fruits[-4])
number=[1,3,5,3,5,74,67,4,7,5,6,54,54,675]
#print(number[-6])

#range of indexing:-..............................................................
list_of_fruits=['apple','banana','cherry','oranges','kiwi','melon','mango']
#print(list_of_fruits[2:5])
#print(list_of_fruits[0:6])
#print(list_of_fruits[:2])
#print(list_of_fruits[1:])
#print(list_of_fruits[-5:-1])
#print(list_of_fruits[0:-1])
#print(list_of_fruits[:5])

#change item value:-.........................................................
places=['tajmahal','kutuminar','temple','delhi','navgurukul']
#places[1]='bhalswa'
#print(places)
names=["neha",'arti','sai','neetu','ruby','shally']
#names[2]='ritesh'
#print(names)
number=[1,3,5,3,5,74,67,4,7,5,6,54,54,675]
#@number[-5]=5756868
#print(number)


#loop through list:-.............................................................
names=["neha",'arti','sai','neetu','ruby','shally']
#i=0
#for i in names:
#
#     print(i)

#i=0
#length=len(names)
#while i<length:
 #   print(names[i])
  #  i=i+1

#if:-
names=["neha",'arti','sai','neetu','ruby','shally']
#if 'sagar'  in names:........................................................
#    print("yes present")

#else:
#    print("not present")    
number=[1,3,5,3,5,74,67,4,7,5,6,54,54,675]
#if 564678 in number:
 #   print("yes present")
#else:
 #   print("not present")    

 ###add item:-(append)#####................................................
sweets=['toffee','biscuit','kurkure','sugar','chips','bread']
#sweets.append('fruity')
#print(sweets)

names=["neha",'arti','sai','neetu','ruby','shally']
#names.append('prashant')
#print(names)

number=[1,3,5,3,5,74,67,4,7,5,6,54,54,675]
#number.append(786)
#print(number)

places=['tajmahal','kutuminar','temple','delhi','navgurukul']
#places.append('bangalore')
#print(places)

list_of_fruits=['apple','banana','cherry','oranges','kiwi','melon','mango']
#list_of_fruits.append('chiku')
#print(list_of_fruits)

#insert item.......remove item.......................pop item.........................................
names=["neha",'arti','sai','neetu','ruby','shally']
#names.insert(1,'suman')
#names.insert(2,4)
#names.insert(4,'gurpreet')
#print(names)
#names.insert(3,'beena')
#print(names)

names=["neha",'arti','sai','neetu','ruby','shally']
#names.remove('neha')
#names.remove('sai')
#print(names)

number=[1,34,1,3,4,7,3,7,1,2,1,3,1,4,1]
#number.remove(1)
#print(number)

#number.pop(6)
#print(number)
list_of_fruits=['apple','banana','cherry','oranges','kiwi','melon','mango']
#list_of_fruits.pop(1)
#print(list_of_fruits)
#list_of_fruits.pop(4)
#list_of_fruits.pop()  if we leave pop with no argument then last element will remove automatically
#print(list_of_fruits)


list=['apple','banana','kiwi']# clear...........................
#list.clear()
#print(list)
list=['apple','banana','kiwi']  #copy....................
#list2=list.copy()
#print(list2)

name=['neha','shilpa']
#names=name.copy()
#print(names)

fruits=['apple','mango']
#fruits_list2=fruits.copy()
#print(fruits_list2)

number=[2,3,6,4,7]
#number2=number.copy()
#print(number2)

places=['delhi','gujarat','himachal']
#place=places.copy()
#print(place)

#del item...............................................................
places=['delhi','gujarat','himachal']
#del places # here it will shoe that places list is not defined due to deletion of whole list
#print(places)

list=['delhi','gujarat','himachal']
#del list[0]
#print(list)
list=['delhi','gujarat','himachal']
#del list #here if you want the whole list deletion but variable is list the it will give you the type list because list is also a keyword.
#print(list)

#joining two  list:-..............................................................
list1=[1,2,3,4,6,7,5,7,7]
list2=['neha','ritesh','sai']
#list3=list1+list2
#print(list3)

#list1.extend(list2)
#print(list1)

grocery=['dal','chawal','pickel','rice']
dal=['red','yellow','balck','green']
#grocery.extend(dal)
#print(grocery)

grocery=(('dal','chawal','pickel','rice'))
#print(grocery) ##double paranthesis works for the square bracket