from ctypes import sizeof
from inspect import indentsize
from operator import index
from unicodedata import numeric


list = [2, 0 ,1 , 0]

#Q1
print(len(list))

#Q2
print(list[0]) #print 2

#Q3
print(list.count(0)) #print 2

#Q4
#print(list[4]) #list index out of range

#Q5
print(2 in list) #True

#Q6
list.append('A')
print(list)
list.pop(4)

#Q7
list.sort()
print(list)
list = [2, 0 ,1 , 0]

#Q8
print(list[0:3])

#Q10
print(list[2:4])

#Q10
list.reverse()
print(list)

