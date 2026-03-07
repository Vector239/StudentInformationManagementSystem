import sqlite3
from contextlib import contextmanager

# 数据库配置
DB_FILE = 'student.db'

# 数据库连接管理器


@contextmanager
def get_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # 支持字段名访问
        cursor = conn.cursor()
        yield cursor
        conn.commit()  # 提交事务
    except Exception as e:
        if conn:
            conn.rollback()  # 出现异常时回滚事务
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# 初始化数据库


def init_db():
    with get_connection() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )
        ''')
        print("✅ 数据库表已创建！")

# 添加学生


def add_student(name, age):
    with get_connection() as cursor:
        cursor.execute(
            "INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        return cursor.lastrowid

# 查询所有学生


def get_all_students():
    with get_connection() as cursor:
        cursor.execute("SELECT * FROM students ORDER BY id")
        return [dict(row) for row in cursor.fetchall()]

# 按ID查询学生


def get_student_by_id(student_id):
    with get_connection() as cursor:
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

# 按姓名查询学生


def get_students_by_name(name):
    with get_connection() as cursor:
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        return [dict(row) for row in cursor.fetchall()]

# 删除学生


def delete_student(student_id):
    with get_connection() as cursor:
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        return cursor.rowcount > 0  # 返回是否删除成功

# 更新学生年龄


def update_student_age(student_id, new_age):
    with get_connection() as cursor:
        cursor.execute("UPDATE students SET age = ? WHERE id = ?",
                       (new_age, student_id))
        return cursor.rowcount > 0  # 返回是否更新成功

# 删除数据库文件


def delete_database():
    import os
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"🗑️ 数据库文件 {DB_FILE} 已删除！")
    else:
        print(f"❌ 数据库文件 {DB_FILE} 不存在！")
