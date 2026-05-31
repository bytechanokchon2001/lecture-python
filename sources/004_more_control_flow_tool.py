# More control flow tool

print(">>>>> Example: if statement")
x: int = 0
if x < 0:
    print("Number should more than zero")
elif x > 100:
    print("Number should less than 100")
else:
    print("Save successful")

print(">>>>> Example: for statement")
animals = ["cat", "dog", "bird"]
for animal in animals:
    print(animal)

print(">>>>> Example: range()")
for i in range(5):
    print(i)

print(">>>>> Example: Break")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

print(">>>>> Example: Continue")
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

print(">>>>> Example: Loop else")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")

print(">>>>> Example: pass")
def my_function():
    pass
my_function()

print(">>>>> Example: match")
status: int = 400
match status:
    case 400:
        print("Bad Request")
    case 404:
        print("Not found")
    case 401 | 403:             # ใช้เครื่องหมาย | เพื่อรวมเงื่อนไข "หรือ"
        print("Not allowed")
    case _:                     # เครื่องหมาย _ ทำหน้าที่เป็น default (ถ้าไม่ตรงกับข้อไหนเลย)
        print("Sonthing's wrong with internet")

print(">>>>> Example: defininf function")
def fib(n):
    """Print a Fibbonacci series less than n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
# Not call the function we just defined
fib(2000)

print(">>>>> Example: More on definding function")
def ask_ok(prompt, retries=4): # Default argument, ถ้าไม่ส่งค่า retries มา ค่าของมันจะเป็น 4
    pass
ask_ok("Hello")
    
def plus(a: int, b: int): # Keyword argument, ส่งค่าโดยระบุชื่อตัวแปร
    pass
plus(a = 10, b = 5)

print(">>>> Example: Unpacking argument list")
# *args
def make_soup(meat, *toppings):
    print(f"ต้มซุบกระดูกหมูใส่เนื้อ: {meat}")
    
    print(f"เครื่องปรุงเพิ่มเติมที่ส่งมา (tuple): {toppings}")

    for topping in toppings:
        print(f" -> ใส่ {topping} เพิ่มลงในหม้อ")
make_soup("หมูสับ", "เห็ดหอม", "ผักชี") # คนที่ 1 ใสาท็อปปิ้ง 2 อย่าง
print("-" * 30)
make_soup("ไก่", "ฟัก", "มะนาวดอง", "กระเทียมเจียว", "พริกไทย") # คนที่ 2 ใส่ท็อปปิ้ง 4 อย่าง

print(">>>>> lambda expression")
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
f(0)
f(1)

