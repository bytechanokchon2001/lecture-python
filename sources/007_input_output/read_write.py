# Read and Write file
file_name: str = "config.txt"

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