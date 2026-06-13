import json

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

# อ่านข้อมูลจากไฟล์ .json
with open("user_infos.json", 'r', encoding="utf-8") as f:
    user_info_loaded = json.load(f)

print("File json user info")
print(type(user_info_loaded))
print(f"Username: {user_info_loaded["username"]} with max skill {user_info_loaded["skill"][0]}")