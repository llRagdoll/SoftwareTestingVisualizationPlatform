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
            <el-icon><Notebook /></el-icon>
            <span>练习题</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/triangle"><el-icon><Position /></el-icon>判断三角形</el-menu-item>
            <el-menu-item index="/wannianli"><el-icon><Position /></el-icon>万年历问题</el-menu-item>
            <el-menu-item index="/computersale"><el-icon><Position /></el-icon>电脑销售系统</el-menu-item>
            <el-menu-item index="/telecom"><el-icon><Position /></el-icon>电信收费问题</el-menu-item>
            <el-menu-item index="/salesCommission"><el-icon><Position /></el-icon>销售问题</el-menu-item>
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
import {Notebook,Position}from '@element-plus/icons-vue'

import { debounce } from "lodash";
const resizeObserver  = window.ResizeObserver;
window.ResizeObserver = class ResizeObserver extends resizeObserver {
  constructor(callback) {
    // 使用 debounce 函数包装回调函数，使其在调用间隔 100 毫秒内不会重复调用
    callback = debounce(callback, 100);
    // 调用父类的构造函数，传递包装后的回调函数
    super(callback);
  }
};
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
