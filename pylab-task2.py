list = [2, 0, 1, 0]
# # 1. Output:4
# #  -Code:
print("1. Output: ", len(list))

# # 2. Output: 2
print("2. Output: ", list[0])

# # 3. Output: 2
# # -  Code:
print("3. Output: ", list.count(0))

# # 4. Output: IndexError: list index out of range. due only 0,1,2,3 indexes.
# # -  Code: 
# print( list[4])
# note: this code assign as comment for continue.
print("4. Output: ", "list index out of range")


# # 5. Output: [2, 0, 1, 0]
# # -  Code:  2 in list
list = [2, 0, 1, 0]
if 2 in list:
    print("5. Output: ","Yes, ther is value: 2 in list")
else:
    print("5. Output: ","No")

# # 6.Output:[2, 0, 1, 0, 'A'] 
# # - Code:
list.append("A")
print("6. Output: ",list)

# # 7. Output:[0, 0, 1, 2]
# # - Code:
list.remove("A")
list.sort()
print("7. Output: ",list)

# # 8.Output:[2, 0, 1] 
# # - Code:
list = [2, 0, 1, 0]
list.pop()
print("8. Output: ", list)

# # 9. Output:[0, 1] 
# # - Code:
list = [2, 0, 1, 0]
print("9. Output: ", list[1:3])

# # 10. Output:[0, 1, 0, 2]
# # - Code:
list = [2, 0, 1, 0]
list.reverse()
print("10.Output: ", list)