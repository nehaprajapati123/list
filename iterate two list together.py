students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
i=0
list2=[]
while i<len(students):
    list=(students[i]+str(marks[i]))
    list2.append(list)
    i=i+1
print(list2)
