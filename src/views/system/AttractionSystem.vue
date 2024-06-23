<template>
    <el-card class="unit-card">
        <el-carousel trigger="click" height="600px" indicator-position="outside">
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录系统-查看地图-选择地点-查看附近景区-查看景区详情-发布评论-点赞评论</p>
                <img src="../../../public/attraction-comment.jpg" alt="Image 1" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录系统-查看地图-选择地点-查看附近景区-查看景区详情-发布评论-发布详情为空-发布失败</p>
                <img src="../../../public/attraction-comment2.jpg" alt="Image 2" style="width:90%;">
            </el-carousel-item>
            <el-carousel-item>
                <p style="font-size:16px;font-weight:600;color:palevioletred">登录系统-进入寻迹页面-智能推荐-图像识别</p>
                <img src="../../../public/attraction-recommend.jpg" alt="Image 3" style="width:90%;">
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