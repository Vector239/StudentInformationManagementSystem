<template>
  <div id="app">
    <!-- 页面头部 -->
    <el-header style="text-align: center; font-size: 20px; background-color: #fff">
      学生信息管理系统
    </el-header>
    <!-- 页面主体 -->
    <el-container style="height: calc(100vh - 60px);">
      <el-main>
        <!-- 路由出口：根据地址渲染对应页面 -->
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
</script>

<style scoped>
/* 简单样式重置 */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.el-header {
  line-height: 60px;
  border-bottom: 1px solid #e6e6e6;
}
</style>