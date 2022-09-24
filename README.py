# # Py-datatypes-hw hw-2
# Conisder the following list:
# ```list = [2, 0, 1, 0]```
# According to the question, write down the code or the output

# Notes: 
#  These are not sequential, the code is only affecting the original list. 
#  Answers should only be 1 line long



# 1. Output: ```4```
# -  Code:  ```?``` 

from re import L


list = [2, 0, 1, 0]

print(len(list))

# 2. Output: ```?```
# -  Code: ```print(list[0])``` 

print(list[0])

#answer: 2


# 3. Output: ```?```
# -  Code: ```print(list.count(0))``` 
print(list.count(0))

# answer is : 2

# 4. Output: ```?```
# -  Code: ```print(list[4])``` 

#print(list[4]) 

#answer : IndexError: list index out of range

# 5. Output: ```?```
# -  Code: ``` 2 in list```  

2 in list

#output : nothing

# 6. Output: ```[2, 0, 1, 0, 'A'] ```
# -  Code: ```?``` 

list.append("A")
print(list)

# 7. Output: ```[0, 0, 1, 2] ```
# -  Code: ```?```
list.remove('A')
list.sort()
print(list)



# 8. Output: ``` [2, 0, 1] ``` 
# -  Code: ```?```


print("[" , list[3],",", list[1], ",", list[2], "]")


# 9. Output: ```[0, 1] ```
# -  Code: ```?``` 

print(list[1:3])

# 10. Output: ```[0, 1, 0, 2] ```
# -  Code: ```?``` 
list.reverse
list[1]=1
list[2]=0
print(list)