<template>
    <el-card class="unit-card">
        <el-carousel trigger="click" height="600px" indicator-position="outside">
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——查看地图——编辑点——编辑轨迹</p>
                <img src="../../../public/map-edit.jpg" alt="Image 1" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——查看地图——分享地图</p>
                <img src="../../../public/map-share.jpg" alt="Image 2" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——查看地图——编辑点—放弃编辑—直接编辑轨迹</p>
                <img src="../../../public/map-edit2.jpg" alt="Image 3" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录——查看地图——分享地图——分享失败</p>
                <img src="../../../public/map-share2.jpg" alt="Image 4" style="width:90%;">
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