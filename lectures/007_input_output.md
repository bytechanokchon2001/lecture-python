# Input and Output
## Fancier Output Formatting (การจัดรูปแบบการแสดงผลที่สวยงาม)
ปกติเราใช้ฟังก์ชัน print() ในการแสดงผลพื้นฐาน แต่ในหัวข้อนี้จะพูดถึงวิธีทำให้ข้อมูลแสดงผลออกมาเป็นระเบียบและอ่านง่าย โดยมี 3 วิธีหลักที่นิยมใช้

### Formatted String Literals (หรือเรียกสั้น ๆ ว่า f-strings)
วิธีนี้เริ่มใช้ตั้งแต่ Python 3.6 เป็นต้นมาและเป็นวิธีที่แนะนำที่สุด โดยการเติมตัวอักษร **f หรือ F** ไว้หน้าเครื่องหมายคำพูด (String) จากนั้นเราสามารถนำตัวแปรหรือคำสั่งคำนวณต่าง ๆ ไปใส่ไว้ในวงเล็บปีกกา `{ }` ได้โดยตรง

    # ตัวอย่างโค้ดที่ 1 (ใช้งาน f-strings ทั่วไป)
    name: str = "Byte Chanokchon"
    age: int = 25
    money: float = 2000.30
    print(f"Hello {name}, at your {age} year old. You have {money} dollar.")

    # ตัวอย่างโค้ดที่ 2 (การกำหนดรูปแบบทศนิยมและความกว้างด้วย f-strings):
    print(f"PI value is: {math.pi:.3f}") # แสดงทศริยม 3 ตัวแหน่ง
    table_data = { "Apple": 35, "Banana": 120, "Cherry": 9 }
    for fruit, price in table_data.items():
    print(f"Fruit name: {fruit:10}, price: {price:5} dollars.") # บังคับให้ชื่อผลไม้ใช้พื้นที่ 10 ช่อง และราคาใช้พื้นที่ 5 ช่องจัดชิดขวา

### The String format() Method
เป็นวิธีแบบดั้งเดิมที่ใช้กันมาก่อน f-strings โดยเราจะใช้ปีกกา `{ }` เป็นตัวจองที่ (placeholder) ภายในสตริง แล้วเรียกใช้เมธอด `.format()` เพื่อส่งค่าตัวแปรเข้าไปแทนที่ตามลำดับ

    print("I like to eat {} and {}".format("Pizza", "Durian")) # แทนที่ตามลำดับการส่งค่า
    print("I like to play {1} and {0}".format("Valorant", "Minecraft")) # ระบุตำแหน่งของค่าที่ต้องการ
    print("Position[x: {x}, y: {y}, z: {z}]".format(x=10.5, y=20.5, z=39.2)) # ระบุชื่อของข้อมูลในผ่อน format
    user_info = { "username": "byte_chanokchon", "role": "admin" }
    print("Hello {username} your role is {role}".format(**user_info)) # สามารถนำข้อมูลต่ก dictionary มาใส่ได้ โดนเติมเครื่องหมาย **

### Manual String Formatting (การจัดรูปแบบด้วยมือผ่าน String Methods)
หากเราไม่ต้องการใช้ `f-string` หรือ `.format()` เราสามารถเขียนการจัดช่องไฟด้วยตัวเองได้ โดยใช้เครื่องหมายสไลซ์สตริงคู่วิธีการเพิ่มพื้นที่ เช่น `.rjust()` (จัดชิดขวา), `.ljust()` (จัดชิดซ้าย) และ `.center()` (จัดกึ่งกลาง) ซึ่งมันจะเติมช่องว่าง (Space) ให้ได้ความกว้างตามที่กำหนด

## Reading and Writing Files (การอ่านและการเขียนไฟล์)
ในการทำงานกับไฟล์ Python มีฟังก์ชันฝังตัวที่ชื่อว่า `open()` เพื่อสร้าง File Object ขึ้นมาจัดการ
โดยมีรูปแบบการใช้งานคือ `open(filename, mode, encoding='utf-8')`
- **mode='r'** อ่านไฟล์ (default)
- **mode='w'** เขียนไฟล์ใหม่ (ถ้ามีไฟล์เดิมจะโดนทับ)
- **mode='a'** เขียนต่อท้ายไฟล์เดิม
- **mode='r+'** ทั้งอ่านและเขียนไฟล์พร้อมกัน

**ข้อแนะนำที่สำคัญที่สุด** ควรใช้คำสั่ง `with` เสมอในการเปิดไฟล์ เพราะเมื่อจบบล็อกคำสั่ง Python จะทำการปิดไฟล์ให้เราโดยอัตโนมัติ *ช่วยป้องกันปัญหาไฟล์ค้างหรือเสียหาย*

### Methods of File Objects (การสั่งงานเพื่อจัดการข้อมูลในไฟล์)

    # เปิดไฟล์ชื่อ config.txt เพื่อเขียนข้อมูลลงไป (ถ้าไม่มีไฟล์ระบบจะสร้างให้ใหม่)
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write("line 1\n")
        f.write("Welcome to project config\n")

    # การอ่านทีเดียวทั้งหมดด้วย .read()
    with open(file_name, 'r', encoding='utf-8') as f:
        print("Read all line")
        content = f.read()
        print(content)

    # อ่านไฟล์ทีละบรรทัด (ประหยัดแรมและแนะนำที่สุดเมื่อไฟล์มีขนาดใหญ่)
    with open(file_name, 'r', encoding="utf-8") as f:
        print("Read line by line using loop")
        for line in f:
            print(line, end='')
        print()

    # อ่านไฟล์และเก็บไว้เป็น string list ด้วย .readlines()
    with open(file_name, 'r', encoding="utf-8") as f:
        print("Read line as list")
        lines = f.readlines()
        print(lines)

### Saving structured data with json (การบันทึกข้อมูลโครงสร้างด้วย JSON)
เมื่อเราต้องการเซฟข้อมูลประเภทคอลเลกชัน เช่น List หรือ Dictionary ลงในไฟล์ หากเราเขียนลงไปตรง ๆ มันจะมองเป็นตัวอักษรสตริงและเวลากลับมาอ่านจะแปลงค่าเป็นข้อมูลดั้งเดิมยาก Python จึงเตรียม*โมดูล json มาให้เพื่อแปลงโครงสร้างข้อมูลเป็นรูปแบบข้อความมาตรฐาน* (เรียกว่าการ `Serialize`)

    # สร้างข้อมูล dictionary ที่ซับซ้อนขึ้นมา
    user_info = {
        "username": "byte.chanokchon",
        "age": 25,
        "skill": ["Python", "C#", "Java"],
        "is_online": True
    }

    # บันทึกข้อมูลลงในไฟล์ .json
    with open("user_infos.json", 'w', encoding="utf-8") as f:
        # dump เอาไว้เขียนลงไฟล์โดยตรง (indent=4 ช่วยจัดบรรทัดให้มนุษย์อ่านง่าย)
        json.dump(user_info, f, indent=4)
        print("Save as json succcessful")

    