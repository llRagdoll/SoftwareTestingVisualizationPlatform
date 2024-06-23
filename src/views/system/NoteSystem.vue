<template>
    <el-card class="unit-card">
        <el-carousel trigger="click" height="600px" indicator-position="outside">
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——查看地图——查看轨迹详情——发布随记</p>
                <img src="../../../public/note-comment.jpg" alt="Image 1" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——进入随记广场——搜索随记——收藏随记——评论随记</p>
                <img src="../../../public/note-create.jpg" alt="Image 2" style="width:90%;">
            </el-carousel-item>
        
    </el-carousel>
    </el-card>
    <el-button type="warning" plain class="run-button"  style="width:80%;margin-top:20px" @click="runTest">运行</el-button>
</template>

<script setup>
import axios from 'axios';
const runTest = () => {
  axios.get('http://localhost:9092/api/notesystem', {
  })
  .then(response => {
    console.log(response.data.result);
  })
  .catch(error => {
    console.error("请求出错：", error)
  });
};
</script>

<style scoped>
.unit-card {
    border-radius: 20px;
    height:88vh
}
</style>