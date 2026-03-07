<template>
  <div class="student-manager">
    <el-card shadow="hover" style="margin-bottom: 20px">
      <!-- 1. 添加学生表单 -->
      <el-form
        :model="addForm"
        label-width="80px"
        inline
        @submit.prevent="addStudent"
      >
        <el-form-item label="姓名">
          <el-input v-model="addForm.name" placeholder="请输入姓名"></el-input>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input
            v-model="addForm.age"
            type="number"
            placeholder="请输入年龄"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="addStudent">添加学生</el-button>
        </el-form-item>
      </el-form>
    </el-card>

    <el-card shadow="hover">
      <!-- 2. 查询区域 -->
      <el-form
        :model="searchForm"
        label-width="80px"
        inline
        style="margin-bottom: 20px"
      >
        <el-form-item label="按ID查询">
          <el-input
            v-model="searchForm.id"
            type="number"
            placeholder="学生ID"
          ></el-input>
        </el-form-item>
        <el-form-item label="按姓名查询">
          <el-input v-model="searchForm.name" placeholder="学生姓名"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="success" @click="searchById">ID查询</el-button>
          <el-button type="warning" @click="searchByName">姓名查询</el-button>
          <el-button type="info" @click="getAllStudents">查询全部</el-button>
        </el-form-item>
      </el-form>

      <!-- 3. 学生列表表格 -->
      <el-table
        :data="studentList"
        border
        stripe
        style="width: 100%"
        v-loading="loading"
      >
        <el-table-column
          prop="id"
          label="学生ID"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="name"
          label="姓名"
          align="center"
        ></el-table-column>
        <el-table-column
          prop="age"
          label="年龄"
          align="center"
        ></el-table-column>
        <el-table-column label="操作" align="center">
          <template #default="scope">
            <!-- 修改按钮：打开弹窗 -->
            <el-button
              type="primary"
              size="small"
              @click="openUpdateDialog(scope.row)"
              >修改</el-button
            >
            <!-- 删除按钮 -->
            <el-button
              type="danger"
              size="small"
              @click="deleteStudent(scope.row.id)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>

      <!-- 4. 修改年龄弹窗 -->
      <el-dialog v-model="updateDialogVisible" title="修改学生年龄" width="30%">
        <el-form :model="updateForm" label-width="80px">
          <el-form-item label="学生ID">
            <el-input v-model="updateForm.id" disabled></el-input>
          </el-form-item>
          <el-form-item label="新年龄">
            <el-input v-model="updateForm.age" type="number"></el-input>
          </el-form-item>
        </el-form>
        <template #footer>
          <el-button @click="updateDialogVisible = false">取消</el-button>
          <el-button type="primary" @click="updateStudentAge"
            >确认修改</el-button
          >
        </template>
      </el-dialog>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const addForm = ref({ name: "", age: "" });
const searchForm = ref({ id: "", name: "" });
const studentList = ref([]);
const loading = ref(false);
const updateDialogVisible = ref(false);
const updateForm = ref({ id: "", age: "" });

const addStudent = async () => {
  try {
    const response = await axios.post(`${BASE_URL}/students`, addForm.value);
    console.log(response); // 打印后端返回的数据
    console.log(response.data); // 打印后端返回的数据
    alert("学生添加成功！");
    addForm.value = { name: "", age: "" };
    getAllStudents();
  } catch (error) {
    alert("添加学生失败：" + error.response.data.detail);
  }
};

const getAllStudents = async () => {
  loading.value = true;
  try {
    const response = await axios.get(`${BASE_URL}/students`);
    studentList.value = response.data;
  } catch (error) {
    alert("获取学生列表失败：" + error.response.data.detail);
  } finally {
    loading.value = false;
  }
};

const searchById = async () => {
  if (!searchForm.value.id) {
    alert("请输入学生ID！");
    return;
  }
  try {
    const response = await axios.get(
      `${BASE_URL}/students/${searchForm.value.id}`
    );
    studentList.value = [response.data];
  } catch (error) {
    alert("查询失败：" + error.response.data.detail);
  }
};

const searchByName = async () => {
  if (!searchForm.value.name) {
    alert("请输入学生姓名！");
    return;
  }
  try {
    const response = await axios.get(`${BASE_URL}/students/search`, {
      params: { name: searchForm.value.name },
    });
    studentList.value = response.data;
  } catch (error) {
    alert("查询失败：" + error.response.data.detail);
  }
};

const updateStudentAge = async () => {
  try {
    await axios.put(`${BASE_URL}/students/${updateForm.value.id}`, {
      age: updateForm.value.age,
    });
    alert("学生年龄修改成功！");
    updateDialogVisible.value = false;
    getAllStudents();
  } catch (error) {
    alert("修改失败：" + error.response.data.detail);
  }
};

const deleteStudent = async (id) => {
  if (!confirm("确认删除该学生吗？")) return;
  try {
    await axios.delete(`${BASE_URL}/students/${id}`);
    alert("学生删除成功！");
    getAllStudents();
  } catch (error) {
    alert("删除失败：" + error.response.data.detail);
  }
};

const openUpdateDialog = (student) => {
  updateForm.value = { id: student.id, age: student.age };
  updateDialogVisible.value = true;
};

onMounted(() => {
  getAllStudents();
});
</script>

<style scoped>
.el-card {
  margin-top: 10px;
}
</style>