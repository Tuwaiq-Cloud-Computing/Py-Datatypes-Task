# Py-datatypes-hw hw-2
# Conisder the following list:
# ```list = [2, 0, 1, 0]```
# According to the question, write down the code or the output

# Notes: 
#  These are not sequential, the code is only affecting the original list. 
#  Answers should only be 1 line long

# 1
list = [2, 0, 1, 0] 
print(len(list))

# 2
print(list[0])

# 3
print(list.count(0))

# 4
print(list[4])

# 5
print(2 in list)

# 6
list.append("A")
print(list)

# 7
list.sort()
print(list)

# 8
list.remove(0)
print(list)

# 9
list.pop(0)
list.pop(2)
print(list)

# 10
list.reverse()
print(list)

# 1. Output: ```4```
# -  Code: print(len(list))

# 2. Output: ```2```
# -  Code: ```print(list[0])``` 

# 3. Output: ```2```
# -  Code: ```print(list.count(0))``` 

# 4. Output: ```out of index```
# -  Code: ```print(list[4])```

# 5. Output: ```True```
# -  Code: ``` 2 in list```

# 6. Output: ```[2, 0, 1, 0, 'A'] ```
# -  Code: ```list.append("A")        print(list)``` 

# 7. Output: ```[0, 0, 1, 2] ```
# -  Code: ```list.sort()            print(list)```

# 8. Output: ``` [2, 0, 1] ``` 
# -  Code: ```list.remove(0)         print(list)```

# 9. Output: ```[0, 1] ```
# -  Code: ```list.pop(0)    list.pop(2)     print(list)``` 

# 10. Output: ```[0, 1, 0, 2] ```
# -  Code: ```list.reverse()            print(list)``` 
