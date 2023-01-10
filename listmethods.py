#list methods
#1) append; adds the element at the end of the list

list=[10,20,30,40,50,60,50]
list.append('muski')
print(list)

list.append('cocci')
print(list)

list.append(20)
print(list)

#2)insert: insert the element at the perticular position

list.insert(2,'pooja')
print(list)

list.insert(0,55)
print(list)

#3) replace; this will remove the element

list.remove(20)
print(list)

list.remove('cocci')
print(list)

#4)pop();this will remove and return the last element
print(list.pop())
print(list)
print(list.pop())
print(list)

#5)reverse; this will reverse the whole list

list.reverse()
print(list)


#6)count: this will count the no. of occurence of perticular element

print(list.count(50))


#7)sort():this will sort the element asc or dec
list=[1,9,6,4,5,3]
print(list.sort(reverse=True))
print(list)

print(list.sort())
print(list)

print(list.sort(reverse=True))
print(list)

#8)index; this will show the index of perticular element

print(list.index(1))
print(list)

print(list.index(6))
print(list)

#9)extent: this will add the element of one list in to another list

p=[1,2,3,4,5,6]
p1=[7,8,9,10,11]

print(p.extend(p1))
print(p)
print(p1)

print(p1.extend(p))
print(p)
print(p1)

#10) clear; this will clear all the element of the list

pooja= ['cocci', 'bacillus', 'coli']
print(pooja.clear)
print(pooja)

#11) deleat:tis will deleat the entire list
# pooja=[1,2,3,44,55,]
# print(pooja.delete)
# print(pooja)
#################################################

# s=[10,20,30,'wednesday','pooji']
# print(s)
# s.append(10)
# print(s)

# s.insert(0,'addams')
# print(s)


# s.remove(20)
# print(s)

# s.pop()
# print(s)

# s.reverse()
# print(s)

# print(s.count('wednesday'))
# print(s)

# print(s.sort(reverse=True))
# print(s)

s=[200,300,400,500]
s1=[1,2,3,4,5,6]
print(s1.extend(s))
print(s)
print(s1)

print(s)
print(s.clear)
print(s)

print(s.deleat)
print(s)

print(s)