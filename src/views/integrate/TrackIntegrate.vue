<template>
    <div v-if="!showReport">
    <el-card class="unit-card">
       <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
       <el-tab-pane label="添加轨迹" name="first">
           <el-table :data="testCases1" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="查看轨迹" name="second">
           <el-table :data="testCases2" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="修改轨迹" name="third">
           <el-table :data="testCases3" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="创建轨迹" name="fourth">
           <el-table :data="testCases4" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>

   </el-tabs>
    </el-card>
    <el-button type="warning" plain class="run-button"  style="width:80%;margin-top:20px" @click="runTest">运行</el-button>
    </div>  
    <div v-else>
        <iframe src="http://localhost:12340" frameborder="0" style="width:100%;height:100vh"></iframe>
        </div>
</template>

<script setup>
import { ref } from 'vue'
// import axios from 'axios';

const showReport = ref(false)

const activeName = ref('first') 
const handleClick = (tab, event) => {
   console.log(tab, event)
}
const testCases1 = [
  {
    caseNumber: "JY_INT_004_001_001",
    caseDescription: "三个参数均为nom",
    input: `{
 "groupID": "",
 "points": [
   {"name": "testPointName1","address": "testaddress1","lat":30.11 ,"lng": 30.11},
   {"name": "testPointName2","address": "testaddress2","lat": 30.21,"lng": 30.21},
   {"name": "testPointName3","address": "testaddress3","lat": 30.31,"lng": 30.31},
   {"name": "testPointName4","address": "testaddress4","lat": 30.41,"lng": 30.41},
   {"name": "testPointName5","address": "testaddress5","lat": 30.51,"lng": 30.51}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": true,
"num": 5`
  },
  {
    caseNumber: "JY_INT_004_002_001",
    caseDescription: "point.length()取边界值，points为空",
    input: `{
 "groupID": "",
 "points": [],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": false,
"num": 0`
  },
  {
    caseNumber: "JY_INT_004_002_002",
    caseDescription: "point.length()取边界值，points只有一个点",
    input: `{
 "groupID": "group00000000000000001",
 "points": [
   {"name": "testPointName6","address": "testaddress6","lat":30.61 ,"lng": 30.61}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": true,
"num": 1`
  },
  {
    caseNumber: "JY_INT_004_002_003",
    caseDescription: "point.length()取边界值，points有两个点",
    input: `{
 "groupID": "",
 "points": [
   {"name": "testPointName7","address": "testaddress7","lat":30.71 ,"lng": 30.71},
   {"name": "testPointName8","address": "testaddress8","lat": 30.81,"lng": 30.81}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": true,
"num": 2`
  },
  {
    caseNumber: "JY_INT_004_003_001",
    caseDescription: "lat取边界值，所有点的lat为负值",
    input: `{
 "groupID": "",
 "points": [
   {"name": "testPointName1","address": "testaddress1","lat":-0.01 ,"lng": 30.11},
   {"name": "testPointName2","address": "testaddress2","lat": -0.01,"lng": 30.21},
   {"name": "testPointName3","address": "testaddress3","lat": -0.01,"lng": 30.31},
   {"name": "testPointName4","address": "testaddress4","lat": -0.01,"lng": 30.41},
   {"name": "testPointName5","address": "testaddress5","lat": -0.01,"lng": 30.51}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": false,
"num": 0`
  },
  {
    caseNumber: "JY_INT_004_003_002",
    caseDescription: "lat取边界值，所有点的lat为0",
    input: `{
 "groupID": "",
 "points": [
   {"name": "testPointName1","address": "testaddress1","lat":0 ,"lng": 30.11},
   {"name": "testPointName2","address": "testaddress2","lat": 0,"lng": 30.21},
   {"name": "testPointName3","address": "testaddress3","lat": 0,"lng": 30.31},
   {"name": "testPointName4","address": "testaddress4","lat":0,"lng": 30.41},
   {"name": "testPointName5","address": "testaddress5","lat": 0,"lng": 30.51}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": true,
"num": 5`
  },
  {
    caseNumber: "JY_INT_004_003_003",
    caseDescription: "lat取边界值，所有点的lat为正值",
    input: `{
 "groupID": "",
 "points": [
   {"name": "testPointName1","address": "testaddress1","lat":0.01 ,"lng": 30.11},
   {"name": "testPointName2","address": "testaddress2","lat": 0.01,"lng": 30.21},
   {"name": "testPointName3","address": "testaddress3","lat": 0.01,"lng": 30.31},
   {"name": "testPointName4","address": "testaddress4","lat": 0.01,"lng": 30.41},
   {"name": "testPointName5","address": "testaddress5","lat": 0.01,"lng": 30.51}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": true,
"num": 5`
  },
  {
    caseNumber: "JY_INT_004_004_001",
    caseDescription: "lng取边界值，所有点的lng为负值",
    input: `{
 "groupID": "group00000000000000001",
 "points": [
   {"name": "testPointName1","address": "testaddress1","lat":30.11 ,"lng": -0.01},
   {"name": "testPointName2","address": "testaddress2","lat": 30.21,"lng": -0.01},
   {"name": "testPointName3","address": "testaddress3","lat": 30.31,"lng": -0.01},
   {"name": "testPointName4","address": "testaddress4","lat": 30.41,"lng": -0.01},
   {"name": "testPointName5","address": "testaddress5","lat": 30.51,"lng": -0.01}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": false,
"num": 0`
  },
  {
    caseNumber: "JY_INT_004_004_002",
    caseDescription: "lng取边界值，所有点的lng为0",
    input: `{
 "groupID": "group00000000000000001",
 "points": [
   {"name": "testPointName1","address": "testaddress1","lat":30.11 ,"lng": 0},
   {"name": "testPointName2","address": "testaddress2","lat": 30.21,"lng": 0},
   {"name": "testPointName3","address": "testaddress3","lat": 30.31,"lng": 0},
   {"name": "testPointName4","address": "testaddress4","lat": 30.41,"lng": 0},
   {"name": "testPointName5","address": "testaddress5","lat": 30.51,"lng": 0}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": true,
"num": 5`
  },
  {
    caseNumber: "JY_INT_004_004_003",
    caseDescription: "lng取边界值，所有点的lng为正值",
    input: `{
 "groupID": "group00000000000000001",
 "points": [
   {"name": "testPointName1","address": "testaddress1","lat":30.11 ,"lng": 0.01},
   {"name": "testPointName2","address": "testaddress2","lat": 30.21,"lng": 0.01},
   {"name": "testPointName3","address": "testaddress3","lat": 30.31,"lng": 0.01},
   {"name": "testPointName4","address": "testaddress4","lat": 30.41,"lng": 0.01},
   {"name": "testPointName5","address": "testaddress5","lat": 30.51,"lng": 0.01}
 ],
 "userID": "user000000000000000001"
}`,
    expectedResult: `"status": true,
"num": 5`
  }
];



const testCases2 = [
  {
    caseNumber: "JY_INT_005_001_001",
    caseDescription: "输入参数合法情况",
    input: 'trackID="track00000000000000001"',
    expectedResult: "返回true，获取成功"
  },
  {
    caseNumber: "JY_INT_005_002_001",
    caseDescription: "输入特定参数为空或不合法的情况，轨迹ID不存在",
    input: 'trackID="track000000000000000-1"',
    expectedResult: "返回false，提示轨迹ID不存在"
  },
  {
    caseNumber: "JY_INT_005_002_002",
    caseDescription: "输入特定参数为空或不合法的情况，轨迹ID为空",
    input: 'trackID=""',
    expectedResult: "返回false，提示轨迹ID为空"
  }
];


const testCases3 = [
  {
    caseNumber: "JY_INT_006_001_001",
    caseDescription: "输入值合法",
    input: `{
      "trackID": "track00000000000000001",
      "pointLists": [
        {"pointID": "point00000000000000001", "segment": 0},
        {"pointID": "point00000000000000002", "segment": 1}
      ],
      "tag": ["tag"],
      "trackName": "track1"
    }`,
    expectedResult: "返回true"
  },
  {
    caseNumber: "JY_INT_006_002_001",
    caseDescription: "输入特定参数为空或者不合法的情况，路线ID为空",
    input: `{
      "trackID": "",
      "pointLists": [
        {"pointID": "point00000000000000001", "segment": 0}
      ],
      "tag": [],
      "trackName": "track1"
    }`,
    expectedResult: "返回false，提示路线ID为空"
  },
  {
    caseNumber: "JY_INT_006_002_002",
    caseDescription: "输入特定参数为空或者不合法的情况，路线名超出规定长度",
    input: `{
      "trackID": "track00000000000000001",
      "pointLists": [
        {"pointID": "point00000000000000001", "segment": 0},
        {"pointID": "point00000000000000002", "segment": 1}
      ],
      "tag": [],
      "trackName": "test-track1"
    }`,
    expectedResult: "返回false，提示路线名超出规定长度"
  },
  {
    caseNumber: "JY_INT_006_002_003",
    caseDescription: "输入特定参数为空或者不合法的情况，标签超出规定长度",
    input: `{
      "trackID": "track00000000000000001",
      "pointLists": [
        {"pointID": "point00000000000000001", "segment": 0},
        {"pointID": "point00000000000000002", "segment": 1}
      ],
      "tag": ["science"],
      "trackName": "track1"
    }`,
    expectedResult: "返回false，提示标签超出规定长度"
  },
  {
    caseNumber: "JY_INT_006_002_004",
    caseDescription: "输入特定参数为空或者不合法的情况，途经点列表为空",
    input: `{
      "trackID": "track00000000000000001",
      "pointLists": [],
      "tag": [],
      "trackName": "track1"
    }`,
    expectedResult: "返回false，提示途经点列表为空"
  },
  {
    caseNumber: "JY_INT_006_002_005",
    caseDescription: "输入特定参数为空或者不合法的情况，途经点不存在",
    input: `{
      "trackID": "track000000000000000-1",
      "pointLists": [
        {"pointID": "point000000000000000-1", "segment": 0},
        {"pointID": "point00000000000000002", "segment": 1}
      ],
      "tag": ["tag"],
      "trackName": "track1"
    }`,
    expectedResult: "返回false，提示途经点不存在"
  },
  {
    caseNumber: "JY_INT_006_002_006",
    caseDescription: "输入特定参数为空或者不合法的情况，途经点顺序超出规定范围",
    input: `{
      "trackID": "track00000000000000001",
      "pointLists": [
        {"pointID": "point00000000000000001", "segment": -1},
        {"pointID": "point00000000000000002", "segment": 1}
      ],
      "tag": ["tag"],
      "trackName": "track1"
    }`,
    expectedResult: "返回false，提示途经点顺序超出规定范围"
  }
];

const testCases4 = [
  {
    caseNumber: "JY_INT_007_001_001",
    caseDescription: "输入参数合法情况",
    input: `trackID="track00000000000000001"`,
    expectedResult: "返回true，删除成功"
  },
  {
    caseNumber: "JY_INT_007_002_001",
    caseDescription: "输入特定参数为空或不合法的情况，轨迹ID不存在",
    input: `trackID="track000000000000000-1"`,
    expectedResult: "返回false，提示轨迹ID不存在"
  },
  {
    caseNumber: "JY_INT_007_002_002",
    caseDescription: "输入特定参数为空或不合法的情况，轨迹ID为空",
    input: `trackID=""`,
    expectedResult: "返回false，提示轨迹ID为空"
  }
];






const runTest = () => {
 showReport.value = true
}
</script>

<style scoped>
.unit-card {
   border-radius: 20px;
   height:88vh
}
</style>