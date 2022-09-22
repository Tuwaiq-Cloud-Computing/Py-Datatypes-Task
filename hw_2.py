# Py-datatypes-hw hw-2


list = [2, 0, 1, 0]

# 1- Output: 4
# 1- Code: ?
print("1-  ", len(list))

# 2- Output: ?
# 2- Code: print(list[0])
print("2-  ", list[0])

# 3- Output: ?
# 3- Code: print(list.count(0))
print("3-  ", list.count(0))

# 4- Output: ?
# 4- Code: print(list[4])
# - - print("4-  ", list[4])
# - - output: list index out of range

# 5- Output: ?
# 5- Code: 2 in list
print("5-  ", 2 in list)

# 6- Output: [2, 0, 1, 0, 'A']
# 6- Code: ?
list.append("A")
print("6-  ", list)

# 7- Output: [0, 0, 1, 2]
# 7- Code: ?
list.pop()
print("7-  ", sorted(list))

# 8- Output: [2, 0, 1]
# 8- Code: ?
print("8-  ", list[0:3])

# 9- Output: [0, 1]
# 9- Code: ?
print("9-  ", list[1:3])

# 10- Output: [0, 1, 0, 2]
# 10- Code: ?
list.reverse()
print("10- ", list)