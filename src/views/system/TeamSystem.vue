<template>
    <el-card class="unit-card">
        <el-carousel trigger="click" height="600px" indicator-position="outside">
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——进入我发布的小队——创建小队——进入小队详情——邀请成员</p>
                <img src="../../../public/create-team.jpg" alt="Image 1" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——进入我发布的小队——进入小队详情——编辑小队——移出成员——解散小队</p>
                <img src="../../../public/manage-team.jpg" alt="Image 2" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——进入我加入的小队——接受邀请——退出小队</p>
                <img src="../../../public/join-team.jpg" alt="Image 3" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——进入我加入的小队——拒绝邀请</p>
                <img src="../../../public/refuse-join.jpg" alt="Image 4" style="width:90%;">
            </el-carousel-item>
    </el-carousel>
    </el-card>
    <el-button type="warning" plain class="run-button"  style="width:80%;margin-top:20px" @click="runTest">运行</el-button>
</template>

<script setup>
import axios from 'axios';

const runTest = () => {
  axios.get('http://localhost:9092/api/teamsystem', {
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