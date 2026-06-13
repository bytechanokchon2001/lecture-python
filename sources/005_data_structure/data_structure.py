# Data Structure
from collections import deque

print("Example: List")
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(f"Count of apple is: {fruits.count('apple')}")
print(f"Count of tangerine is: {fruits.count('tangerine')}")
print(f"First index of banana is: {fruits.index('banana')}")
print(f"Find next banana, index of next banana is: {fruits.index('banana', 4)}")
print(f"Fruits before reverse: {fruits}")
fruits.reverse()
print(f"Revert after reverse: {fruits}")
fruits.append('grape')
print(f"Fruits after append new item: {fruits}")
fruits.sort()
print(f"Fruits after sort: {fruits}")
last_fruit: str = fruits.pop()
print(f"Fruit popped: {last_fruit}")
print(f"Fruits after pop one: {fruits}")

print("Exanple: Using list as stack")
stacks = [3, 4, 5]
stacks.append(6)
stacks.append(7)
print(stacks)
stacks.pop()
print(stacks)
stacks.pop()
print(stacks)

print("Example: Using list as queue")
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)

print("Example: List Comprehensions")
print("Normal")
squares_1 = []
for x in range(10):
    squares_1.append(x**2)
print(squares_1)
print("List comprehensions")
squares_2 = [x**2 for x in range(10)]
print(squares_2)
print("List comprehensions with condition")
print([x for x in squares_2 if x > 50])

print("Example: Nested List Comprehensions")
print("Normal nested")
combs_1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs_1.append((x, y))
print(combs_1)
print("Comprehension nested")
combs_2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs_2)

print("Example: The del statement")
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a 

print("Example: Tuple")
tuple_empty = ()
print(len(tuple_empty))
print(tuple_empty)
tuple_single = "Hello",
print(len(tuple_single))
print(tuple_single)
t = 1, 2, "Hello World"
x, y, z = t
print(x, y, z)

print("Example: Set")
set_a = {"apple", "banana", "orange"}
set_b = {"banana", "grape", "watermelon"}
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference: {set_a - set_b}")
print(f"Symetric difference: {set_a ^ set_b}")

print("Example: Dictionary")
student = {
    "name": "Byte Chanokchon",
    "age": 25,
    "gpa": 2.99,
    "is_graduated": True,
    "favorite_subject": ["Programming"]
}
print(f"Student name: {student['name']}")
print(f"Favorite subject: {student.get("favorite_subject")}")
student["school"] = "Rajavinit Bangkhen" # เพิ่มข้อมูลเข้าไป
student["age"] = 18 # แก้ไขข้อมูล
print(student)
del student["is_graduated"] # ลบข้อมูลออก
print(student)