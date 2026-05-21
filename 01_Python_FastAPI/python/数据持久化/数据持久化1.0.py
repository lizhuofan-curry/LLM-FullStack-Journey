import json
import os
# 这个 os 是 Python 官方自带的一个核心标准库，它的全称就是 Operating System（操作系统）。
file_path = 'contacts.json'

# 1. 🟢 开机检查：先去硬盘里“复活”旧数据
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contacts = json.load(f)  # 如果有文件，就读取历史存档
    print(f"📂 成功加载历史存档，当前共有 {len(contacts)} 个联系人。")
else:
    # 如果是第一次运行，文件不存在，就初始化两个默认联系人
    contacts = [
        {'name': 'Alice', 'phone': '111-2222', 'is_vip': True},
        {'name': 'Bob', 'phone': '333-4444', 'is_vip': False},
    ]
    print("🆕 首次运行，初始化默认联系人。")

# 2. 🟢 模拟用户操作：每次运行都动态“多加一个人”
new_name = input("请输入新联系人姓名（直接回车跳过）: ")
if new_name:
    new_phone = input("请输入电话: ")
    contacts.append({'name': new_name, 'phone': new_phone, 'is_vip': False})

# 3. 🟢 存档：用 "w" 把当下最新、最全的名单整体覆写进硬盘
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(contacts, f, ensure_ascii=False, indent=4)
    #indent=4（缩进 4 个空格）：
    #Python 会像一个强迫症设计师一样，自动帮你换行、对齐、打空格


    #当你加上 ensure_ascii=False（关闭强制 ASCII 编码）：
    # 防止输入中文时出现乱码
print("💾 数据已成功持久化到硬盘！")

# 4. 打印当前最新的所有人
print("\n当前最新名单:", contacts)