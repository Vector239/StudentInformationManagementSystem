<template>
  <div class="login">
    <el-card class="login-card" shadow="hover">
      <h2 style="text-align: center">登录</h2>
      <el-form :model="loginForm" label-width="80px">
        <el-form-item label="用户名">
          <el-input
            v-model="loginForm.username"
            placeholder="请输入用户名"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input
            v-model="loginForm.password"
            type="password"
            placeholder="请输入密码"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="login">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "UserLogin",
};
</script>

<script setup>
import { ref } from "vue";
import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

const loginForm = ref({
  username: "",
  password: "",
});

const login = async () => {
  try {
    const response = await axios.post(`${BASE_URL}/login`, loginForm.value);
    alert("登录成功！");
    console.log(response.data);
    // 登录成功后跳转到学生管理页面
    window.location.href = "/";
  } catch (error) {
    alert("登录失败：" + error.response.data.detail);
  }
};
</script>

<style scoped>
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}
.login-card {
  width: 400px;
  padding: 20px;
}
</style>