from db import init_db, add_student, get_all_students, get_student_by_id, get_students_by_name, update_student_age, delete_student, delete_database

if __name__ == "__main__":
    # 初始化数据库
    init_db()

    # 添加测试数据
    student_id1 = add_student("Alice", 20)
    student_id2 = add_student("Bob", 22)
    student_id3 = add_student("Alice", 23)

    # 查询所有学生
    print("📋 所有学生：")
    print(get_all_students())

    # 按ID查询学生
    print(f"🔍 查询 ID={student_id1} 的学生：")
    print(get_student_by_id(student_id1))

    # 按姓名查询学生
    print("🔍 查询名为 Alice 的学生：")
    print(get_students_by_name("Alice"))

    # 更新学生年龄
    if update_student_age(student_id1, 21):
        print(f"✅ 更新 ID={student_id1} 的学生年龄成功！")
    else:
        print(f"❌ 更新 ID={student_id1} 的学生年龄失败！")

    # 删除学生
    if delete_student(student_id2):
        print(f"✅ 删除 ID={student_id2} 的学生成功！")
    else:
        print(f"❌ 删除 ID={student_id2} 的学生失败！")

    # 删除数据库
    delete_database()
