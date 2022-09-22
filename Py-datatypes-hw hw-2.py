'''
Conisder the following list:
```list = [2, 0, 1, 0]```
According to the question, write down the code or the output

Notes:
 These are not sequential, the code is only affecting the original list.
 Answers should only be 1 line long
'''

mylist = [2, 0, 1, 0]
print("\n", mylist)
print("1. Output: ```4```")
print("code: ", "is", "len(mylist)")
print("The output after using the previous code is: ", len(mylist))

print("\n", mylist)
print("2. Output: ```?```")
print("Code is: ```print(mylist[0])```")
print("The output after using the previous code is: ", mylist[0])

print("\n", mylist)
print("3. Output: ```?```")
print("Code: ```print(mylist.count(0))```")
print("The output after using the previous code is: ", mylist.count(0))

print("\n", mylist)
print("4. Output: ```?```")
print("Code: ```print(mylist[4])```")
#print(mylist[4])
print("As the list has four element, and the index numbering starts from 0 so the code mylist[4] will return an error as the list index out of range")


print("\n", mylist)
print("5. Output: ```?```")
print("Code: ``` 2 in mylist```")
print("The output after using the previous code is: ", 2 in mylist)


print("\n", mylist)
print("6. Output: ```[2, 0, 1, 0, 'A'] ```")
print("To have this output use this code mylist.append('A'); print(mylist) ")
mylist.append('A'); print(mylist)

mylist = [2, 0, 1, 0]
print("\n", mylist)
print("7. Output: ```[0, 0, 1, 2] ```")
print("To have this output use this code mylist.sort(); print(mylist) ")
mylist.sort(); print(mylist)

mylist = [2, 0, 1, 0]
print("\n8. Output: ``` [2, 0, 1] ```")
print("To have this output use this code print(mylist[0:3]) ")
print(mylist[0:3])


mylist = [2, 0, 1, 0]
print("\n", mylist)
print("9. Output: ```[0, 1] ```")
print("To have this output use this code print(mylist[1:3]) ")
print(mylist[1:3])


print("\n", mylist)
print("10. Output: ```[0, 1, 0, 2] ```")
print("To have this output use this code mylist.reverse(); print(mylist) ")
mylist.reverse(); print(mylist)