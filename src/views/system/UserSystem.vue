<template>
    <el-card class="unit-card">
        <el-carousel trigger="click" height="600px" indicator-position="outside">
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">注册——登录</p>
                <img src="../../../public/user-login.jpg" alt="Image 1" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——修改个人信息</p>
                <img src="../../../public/user-modify.jpg" alt="Image 2" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——修改个人信息——个人信息编辑失败——退出编辑</p>
                <img src="../../../public/user-modify2.jpg" alt="Image 3" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">注册——手机号已注册——退出注册</p>
                <img src="../../../public/user-register2.jpg" alt="Image 4" style="width:90%;">
            </el-carousel-item>
    </el-carousel>
    </el-card>
    <el-button type="warning" plain class="run-button"  style="width:80%;margin-top:20px" @click="runTest">运行</el-button>
</template>

<script setup>
</script>

<style scoped>
.unit-card {
    border-radius: 20px;
    height:88vh
}
</style>