# Py-Datatypes-Task

## Tasks:

Conisder the following list:
```list = [2, 0, 1, 0]```
According to the question, write down the code or the output

Notes: 
 These are not sequential, the code is only affecting the original list. 
 Answers should only be 1 line long

-------------------------
1  Output: 4
#Code: is
list = [2, 0, 1, 0]
print(len(list))
------------------------------
2 Output: 2
print(list[0])
------------------------------
3 Output: 2
print(list.count(0))
------------------------------
4 Output: out of range
print(list[4])
File "<string>", line 5, in <module>
IndexError: list index out of range
------------------------------
5 Output: ?
 2 in list
SyntaxError: invalid syntax
------------------------------
6 Output: [2, 0, 1, 0, 'A']
list.append('A')
print(list)
------------------------------

7 Output: [0, 0, 1, 2]
Code: is
list = [2, 0, 1, 0]
sorted_list = sorted(list)
print("Sorted list:", sorted_list)
------------------------------
8 Code:
Output: [2, 0, 1]
list = [2, 0, 1, 0]
list.pop()
print(list)
------------------------------
9 Output: [0, 1]
Code: ia
list = [2, 0, 1, 0]
list.pop(0)
list.pop()
print(list)
------------------------------
10 Output: [0, 1, 0, 2]
Code: is
list = [2, 0, 1, 0]
list.reverse()
print(list)

## Submission:

- Modify this file to complete the tasks then create a pull request
