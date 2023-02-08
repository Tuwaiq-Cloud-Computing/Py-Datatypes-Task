lst = [2, 0, 1, 0]
print("1. Output: ```4```")
print("- code: len(lst)")
print("Output:",len(lst))
print(20*"#")

print("2. Output: ```2```")
print("- code: lst[0]`")
print("Output:",lst[0])
print(20*"#")

print("3. Output: ```None```")
print("- code: lst.count(0)")
print("Output:",print(lst.count(0)))
print(20*"#")

print("4. Output: ```list index out of range```")
print("- code: lst[4]")
try: print("Output:",lst[4])
except Exception as e: print(e)

print("5. Output: ```True```")
print("- code: 2 in lst`")
print("Output:",2 in lst)
print(20*"#")

print("6. Output: ```[2, 0, 1, 0, 'A']```")
print("- code: lst.append(\"A\")")
lst.append("A")
print("Output:",lst)
print(20*"#")

print("7. Output: ```[0, 0, 1, 2] ```")
print("-  Code: ``` sorted([i for i in lst if i !=\"A\"]))```")

print("Output",sorted([i for i in lst if i !="A"]))
print(20*"#")

print("8. Output: ``` [2, 0, 1] ``` ")
print("-  Code: ```lst[:3]```")

print(lst[:3])
print(20*"#")

print("9. Output: ```[0, 1] ```")
print("-  Code: ```lst[1:3]```")
print(lst[1:3])
print(20*"#")

print("10. Output: ```[0, 1, 0, 2] ```")
print("-  Code: ```list(reversed([i for i in lst if i !=\"A\"]))``` ")

print(list(reversed([i for i in lst if i !="A"])))