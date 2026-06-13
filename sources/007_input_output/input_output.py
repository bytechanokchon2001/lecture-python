import math

# Input and Output
print("Example: Formatted String Literals")
name: str = "Byte Chanokchon"
age: int = 25
money: float = 2000.30
print(f"Hello {name}, at your {age} year old. You have {money} dollar.")

print("Exanple: format string with decimal")
print(f"PI value is: {math.pi:.3f}") # แสดงทศริยม 3 ตัวแหน่ง
table_data = { "Apple": 35, "Banana": 120, "Cherry": 9 }
for fruit, price in table_data.items():
    print(f"Fruit name: {fruit:10}, price: {price:5} dollars.") # บังคับให้ชื่อผลไม้ใช้พื้นที่ 10 ช่อง และราคาใช้พื้นที่ 5 ช่องจัดชิดขวา

print("Example: format() method")
print("I like to eat {} and {}".format("Pizza", "Durian")) # แทนที่ตามลำดับการส่งค่า
print("I like to play {1} and {0}".format("Valorant", "Minecraft")) # ระบุตำแหน่งของค่าที่ต้องการ
print("Position[x: {x}, y: {y}, z: {z}]".format(x=10.5, y=20.5, z=39.2)) # ระบุชื่อของข้อมูลในผ่อน format
user_info = { "username": "byte_chanokchon", "role": "admin" }
print("Hello {username} your role is {role}".format(**user_info)) # สามารถนำข้อมูลต่ก dictionary มาใส่ได้ โดนเติมเครื่องหมาย **

print("Example: Manual format string")
for x in range(1, 6): # แสดงตารางสูตรคูณแม่ 2 แบบจัดรูปเล่มด้วยมือ
    # .rjust(2) คือ ให้มีความกว้าง 2 ตัวอักษรและชิดขวา
    # .rjust(3) คือ ให้มีความกว้าง 3 ตัวอักษรและชิดขวา
    print(str(x).rjust(2), "x 2 = ", str(x*2).rjust(3))
print("12".zfill(5)) # เติมเลข 0 ด้านหน้าจนครบ 5 ตัวอักษร (นับรวมตัวอักษรที่มีอยู่แล้ว)
print("-3.45".zfill(7))