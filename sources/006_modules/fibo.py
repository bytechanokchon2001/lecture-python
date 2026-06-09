def fib1(n):                # เขียนฟังก์ชันหาลำดับฟีโบนัชชีแบบพริ้นต์ออกหน้าจอ
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

def fib2(n):                # ฟังก์ชันส่งคืนค่าลำดับฟีโบนัชชีเป็นลิสต์
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    print("Module run from terminal")
    fib1(sys.argv[1])

    