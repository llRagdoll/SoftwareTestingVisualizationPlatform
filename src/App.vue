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
            <el-menu-item index="/wannianli">万年历问题</el-menu-item>
            <el-menu-item index="/triangle">判断三角形</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group>
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-4">
            <template #title>item four</template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="2">
          <el-icon><icon-menu /></el-icon>
          <span>Navigator Two</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <el-icon><document /></el-icon>
          <span>Navigator Three</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>Navigator Four</span>
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
import {
  Menu as IconMenu,
  Setting,
} from '@element-plus/icons-vue'
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
