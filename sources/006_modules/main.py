# import แบบปกติ
# import fibo
# # เรียกใช้งานฟังก์ชันผ่านชื่อโมดูล
# fibo.fib1(1000)
# # เรียกใช้ fib2
# print(fibo.fib2(1000))

# นำเข้าฟังก์ชันเฉพาะเจาะจงโดยตรง
# from fibo import fib1, fib2
# fib1(1000)
# print(fib2(1000))

# นำเข้าทุกอย่าง (from ... import *)
# from fibo import *
# fib1(500)

# การตั้งชื่อเล่นหรือนามแฝง (import ... as ...)
import fibo as f
f.fib1(500)

from fibo import fib1 as fibonacci
fibonacci(500)