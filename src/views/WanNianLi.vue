<template>
    <el-row style="height:95vh">
        <el-col :span="15">
            <el-row style="height:30%">
                <div class="question-card">
                    <p class="question-title">万年历问题</p>
                </div>
            </el-row>
            <el-row>
                <div class="testcase-card">
                    <el-tabs v-model="activeName"  @tab-click="handleClick">
                        <el-tab-pane label="User" name="first">
                            <el-table :data="tableData" height="250" style="width: 100%">
                                <el-table-column prop="date" label="Date" width="180" />
                                <el-table-column prop="name" label="Name" width="180" />
                                <el-table-column prop="address" label="Address" />
                            </el-table>
                        </el-tab-pane>
                        <el-tab-pane label="Config" name="second">Config</el-tab-pane>
                        <el-tab-pane label="Role" name="third">Role</el-tab-pane>
                        <el-tab-pane label="Task" name="fourth">Task</el-tab-pane>
                    </el-tabs>
                </div>
            </el-row>
        </el-col>
        <el-col :span="9">
            <div class="run-chart">
                <div class="input-area">
                    <p>测试输入</p>
                    <el-input placeholder="请输入测试用例编号"></el-input>
                    <p>边长1：12</p>
                    <p>边长2：12</p>
                    <p>边长3：12</p>
                    <el-button type="warning" plain class="run-button">运行</el-button>
                </div>
                <div class="chart-area">
                  这是一张图
                </div>
            </div>
        </el-col>
    </el-row>
</template>

<script setup>
const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-08',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-06',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-07',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
]
</script>

<style>
.question-card{
    width: 100%;
    height: 24vh;
    background-color: #53B5B2;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding:10px
}

.question-title{
    font-size: 20px;
    color: #ffffff;
}

.testcase-card{
    width: 100%;
    height: 65vh;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding:10px
}

.run-chart{
    width: 90%;
    height: 93vh;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-left:5%;
    padding:10px
}

.input-area{
    height:50%
}

.chart-area{
    height:50%
}

.run-button{
    width:90%;
    
}
</style>