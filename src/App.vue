<template>
    <div class="common-layout" style="padding: 0;">
    <el-container>
      <el-aside width="250px">
        <div style="width:100%;height:100vh;background-color: #d4ebeb;">
          <div style="padding:10%">
          <el-menu
        active-text-color="#ffd04b"
        background-color="#fff"
        default-active="2"
        text-color="#3D3D3D"
        @open="handleOpen"
        @close="handleClose"
        style="border-radius: 20px;box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);;"
        router
        collapse-transition="false"
        default-expand-all="true"
        :default-openeds="openeds"
      >
        <el-sub-menu index="1">
          <template #title >
            <el-icon><location /></el-icon>
            <span>练习题</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/triangle">判断三角形</el-menu-item>
            <el-menu-item index="/wannianli">万年历问题</el-menu-item>
            <el-menu-item index="/computersale">电脑销售系统</el-menu-item> 
          </el-menu-item-group>
           
        </el-sub-menu>
        <el-menu-item index="empty">
          <el-icon><icon-menu /></el-icon>
          <span></span>
        </el-menu-item>
      </el-menu>
    </div>
        </div>
       
      </el-aside>
      <el-main style="background-color: #f0f8fa;">
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const openeds = ref(['1', '3'])
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 0
}

body{
  margin:0
}
</style>
