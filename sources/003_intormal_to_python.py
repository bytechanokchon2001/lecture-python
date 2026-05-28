# An Informal Introduction to Python

print("NUMBER")
x: int = 5
y: int = 10
print(f"Result of + is: {x + y}")   # บวก
print(f"Result of - is: {x - y}")   # ลบ
print(f"Result of * is: {x * y}")   # คูณ
print(f"Result of / is: {x / y}")   # หาร
print(f"Result of % is: {x % y}")   # หารเอาเศษ
print(f"Result of ** is: {x ** y}") # ยกกำลัง

print("TEXT")
username: str = "byte.chanokchon"
print(username[0])      # เข้าถึงตัวแหน่งตัวอักษรด้วย index
print(username[5:11])   # เอาตัวอักษรตั้งแต่ตำแหน่งที่ 5 ถึง 11-1
print(username[:4])     # เอาตัวอักษรตั้งแต่ตำแหน่งแรกจนถึงตำแหน่งที่ 4
print(username[5:])     # เอาตัวอักษรตั้งแต่ตำแหน่งที่ 5 จนถึงตัวสุดท้าย
print(len(username))    # ดูจำนวนตัวอักษรในข้อความ

print("LIST")
foods = ["pizza", "egg", "banana", "rice", "potato"]
print(foods[0])                 # เข้าถึงข้อมูลด้วยตำแหน่ง
print(foods[0:2])               # เอาข้อมูลตั้งแต่ตำแหน่งที่ 0 ถึง 2-1
print(foods[0:1] + foods[2:])   # นำ list ทั้งสองตัวมาต่อกัน
foods.append("apple")           # เพิ่มข้อมูลเข้าไปใน list
print(foods)
food_copies = foods[:]          # คัดลอก foods ด้วย Slice (หากไม่ใช้ slice) จะทำให้ foods และ food_copies ชี้ไปที่ตำแหน่งเดียวกันบนแรม
print(food_copies)

