from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import init_db, add_student, get_all_students, get_student_by_id, get_students_by_name, update_student_age, delete_student, delete_database
from fastapi.middleware.cors import CORSMiddleware

# 定义 FastAPI 应用
app = FastAPI()

# 配置 CORS 中间件，允许前端应用访问后端 API，解决跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],  # 允许的前端地址
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 请求头
)

# 定义 Pydantic 模型，用于请求和响应数据验证，用于请求体参数的验证，确保传入的数据格式正确
# 添加学生时候的传入参数需满足name和age字段
class Student(BaseModel):
    name: str
    age: int

class UpdateStudent(BaseModel):
    age: int

class LoginRequest(BaseModel):
    username: str
    password: str
    
# 初始化数据库
@app.on_event("startup")
async def startup_event():
    init_db()

#登录方法接口
@app.post("/login", summary="用户登录", description="验证用户名和密码")
async def login(request: LoginRequest):
    if request.username == "admin" and request.password == "123456":
        return {"message": "登录成功", "token": "fake-jwt-token"}
    else:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    
# 获取所有学生
@app.get("/students", summary="获取所有学生", description="返回所有学生信息")
async def get_students():
    students = get_all_students()
    return students

# 按 ID 获取学生 这里的student_id是路径参数，类型为int
@app.get("/students/{student_id}", summary="按 ID 获取学生", description="根据学生 ID 返回学生信息")
async def get_student(student_id: int):
    student = get_student_by_id(student_id)
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# 按姓名获取学生 这里的name是查询参数，类型为str,访问路径为/students/search?name=xxx
@app.get("/students/search", summary="按姓名获取学生", description="根据学生姓名返回学生信息")
async def search_students(name: str):
    students = get_students_by_name(name)
    if students:
        return students
    else:
        raise HTTPException(status_code=404, detail="No students found with the given name")

# 添加学生，这里的student是请求体参数，类型为Student模型，访问路径为/students，使用POST方法，请求体需要包含name和age字段，
@app.post("/students", summary="添加学生", description="添加一个新的学生")
async def create_student(student: Student):
    student_id = add_student(student.name, student.age)
    return {"id": student_id, "name": student.name, "age": student.age}

# 更新学生年龄
@app.put("/students/{student_id}", summary="更新学生年龄", description="根据学生 ID 更新学生年龄")
async def update_student(student_id: int, student: UpdateStudent):
    if update_student_age(student_id, student.age):
        return {"message": "Student updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# 删除学生
@app.delete("/students/{student_id}", summary="删除学生", description="根据学生 ID 删除学生")
async def delete_student_route(student_id: int):
    if delete_student(student_id):
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# 删除整个数据库
@app.delete("/database", summary="删除数据库", description="删除整个数据库文件")
async def delete_db():
    delete_database()
    return {"message": "Database deleted successfully"}