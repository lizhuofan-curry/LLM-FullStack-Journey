import json
import os

file_path = 'contacts.json'

# ==================== 1. 读档（启动时自动执行） ====================
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contacts = json.load(f)
    print(f"📂 欢迎回来！已成功加载硬盘历史存档（当前共 {len(contacts)} 人）。")
else:
    # 第一次运行时初始化默认数据
    contacts = [
        {'name': 'Alice', 'phone': '111-2222', 'is_vip': True},
        {'name': 'Bob', 'phone': '333-4444', 'is_vip': False},
    ]
    print("🆕 首次运行，已自动为您初始化默认联系人。")


# ==================== 2. 自动存档工具函数 ====================
def save_to_disk():
    """只要调用这个函数，就会把内存里最新的 contacts 列表，完美覆写进硬盘"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
    print("💾 [系统提示] 数据已自动同步到硬盘文件！")


# ==================== 3. 核心功能函数 ====================

def show_all():
    """查看所有人"""
    print("\n================ 当前联系人名单 ================")
    if not contacts:
        print(" ( 暂无联系人数据 )")
    else:
        for idx, c in enumerate(contacts, 1):
            # 判断是不是 VIP，显示不同的尊贵标识
            vip_tag = "👑 VIP 会员" if c['is_vip'] else "普通成员"
            print(f"[{idx}] 姓名: {c['name']} | 电话: {c['phone']} | 身份: {vip_tag}")
    print("================================================")


def add_contact():
    """新增联系人（支持输入 VIP）"""
    print("\n--- ➕ 新增联系人 ---")
    name = input("请输入姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空！")
        return

    phone = input("请输入电话: ").strip()

    # 🌟 这里实现了让你输入 is_vip 的功能！
    vip_input = input("请问该联系人是否为 VIP？(请输入 y 或 n): ").strip().lower()
    is_vip = True if vip_input == 'y' else False

    # 组装字典，塞进内存列表
    contacts.append({'name': name, 'phone': phone, 'is_vip': is_vip})
    print(f"✅ 成功添加联系人: {name}")

    # 🟢 联动持久化：加完人，立刻存盘！
    save_to_disk()


def delete_contact():
    """根据姓名删除联系人（不用去开 json 文件删了！）"""
    print("\n--- ❌ 删除联系人 ---")
    name_to_delete = input("请输入你要删除的联系人姓名: ").strip()

    # 在内存列表里寻找这个人
    found = False
    for c in contacts:
        if c['name'] == name_to_delete:
            contacts.remove(c)  # 从内存列表中移除
            print(f"🗑️ 已成功从内存中删除: {name_to_delete}")
            found = True
            break  # 找到了就跳出循环

    if not found:
        print(f"❓ 未找到名叫 [{name_to_delete}] 的联系人，请核对后重试。")
    else:
        # 🟢 联动持久化：删完人，立刻存盘！
        save_to_disk()


# ==================== 4. 主循环菜单 ====================
if __name__ == "__main__":
    while True:
        show_all()
        print("\n=== 请输入数字选择操作 ===")
        print("1. 新增联系人 (可设置VIP)")
        print("2. 删除联系人")
        print("3. 退出系统")

        choice = input("你的选择是: ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            print("👋 感谢使用，再见！")
            break
        else:
            print("⚠️ 输入错误，请请输入 1、2 或 3！")