<template>
  <div v-if="!showAllure">

   <el-card class="unit-card" >
      <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
      <el-tab-pane label="退出小队" name="first">
          <el-table :data="testCases4" border style="width: 100%" max-height="600">
              <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
              <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
              <el-table-column prop="input" label="输入"></el-table-column>
              <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
          </el-table>
      </el-tab-pane>
      <el-tab-pane label="邀请成员" name="second">
          <el-table :data="testCases2" border style="width: 100%" max-height="600">
              <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
              <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
              <el-table-column prop="input" label="输入"></el-table-column>
              <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
          </el-table>
      </el-tab-pane>
      <el-tab-pane label="创建小队" name="third">
          <el-table :data="testCases1" border style="width: 100%" max-height="600">
              <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
              <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
              <el-table-column prop="input" label="输入"></el-table-column>
              <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
          </el-table>
      </el-tab-pane>
      <el-tab-pane label="获取收藏小队" name="fourth">
          <el-table :data="testCases3" border style="width: 100%" max-height="600">
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
  <div v-else class="report-container">
      <iframe src="http://127.0.0.1:12344" style="width:100%;height:100vh;border:none"></iframe>
  </div>
</template>

<script setup>
import { ref } from 'vue'
//import axios from 'axios';


const activeName = ref('first') 
const handleClick = (tab, event) => {
  console.log(tab, event)
}
const testCases1=[
      { caseNumber: '001', caseDescription: '创建成功', input: 'teamName="testTeamName", detail="testDetail", leaderName="testLeaderName"', expectedResult: '小队创建成功' },
      { caseNumber: '002', caseDescription: '创建失败，小队名为空', input: 'teamName=NULL, detail="testDetail", leaderName="testLeaderName"', expectedResult: '创建失败，提示小队名不能为空' },
      { caseNumber: '003', caseDescription: '创建失败，小队名重复', input: 'teamName="testTeamName1", detail="testDetail", leaderName="testLeaderName"', expectedResult: '创建失败，提示小队名不能重复' },
      { caseNumber: '004', caseDescription: '创建失败，小队名长度小于2', input: 'teamName="t", detail="testDetail", leaderName="testLeaderName"', expectedResult: '创建失败，提示小队长度应不小于2' },
      { caseNumber: '005', caseDescription: '创建失败，小队名长度大于15', input: 'teamName="testTeamNameeeee", detail="testDetail", leaderName="testLeaderName"', expectedResult: '创建失败，提示小队名长度应不大于15' },
      { caseNumber: '006', caseDescription: '创建失败，描述长度小于5', input: 'teamName="testTeamName", detail="t", leaderName="testLeaderName"', expectedResult: '创建失败，提示描述长度应不小于5' },
      { caseNumber: '007', caseDescription: '创建失败，描述长度大于100', input: 'teamName="testTeamName", detail="1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890", leaderName="testLeaderName"', expectedResult: '创建失败，提示描述长度应不大于100' },
      { caseNumber: '008', caseDescription: '创建失败，描述为空', input: 'teamName="testTeamName", detail=NULL, leaderName="testLeaderName"', expectedResult: '创建失败，提示描述不能为空' },
      { caseNumber: '009', caseDescription: '创建失败，队长名为空', input: 'teamName="testTeamName", detail="testDetail", leaderName=NULL', expectedResult: '创建失败，提示队长名不能为空' },
      { caseNumber: '010', caseDescription: '创建失败，队长名不存在', input: 'teamName="testTeamName", detail="testDetail", leaderName="testLeaderName0"', expectedResult: '创建失败，提示小队名不存在。。。。。把这些数据给我画成一个el-table' }
    ]

const testCases2= [
      { caseNumber: '001', caseDescription: '解散失败，删除小队中teamId为空', input: 'teamId=NULL', expectedResult: '解散失败，提示ID不能为空' },
      { caseNumber: '002', caseDescription: '解散失败，删除小队中teamId非空但不存在', input: 'teamId="00000000000000000000-1"', expectedResult: '解散失败，提示ID不存在' },
      { caseNumber: '003', caseDescription: '解散成功', input: 'teamId="0000000000000000000001"', expectedResult: '解散成功，，，变成testCases2' }
    ]

    const testCases3 = [
  {
    caseNumber: "JY_INT_0014_001",
    caseDescription: "输入参数合法且符合逻辑",
    input: "{ \"userId\": \"88b00cbc341543328d155238cb7158f7\" }",
    expectedResult: "收藏列表"
  },
  {
    caseNumber: "JY_INT_0014_002",
    caseDescription: "输入特定参数为空的情况",
    input: "{ \"userId\": null }",
    expectedResult: "null"
  },
  {
    caseNumber: "JY_INT_0014_003",
    caseDescription: "输入参数合法但不存在",
    input: "{ \"userId\": \"88b00cbc341543328d155238cb7158-7\" }",
    expectedResult: "null"
  }
];
const testCases4 = [
  {
    caseNumber: "JY_INT_0015_001_001",
    caseDescription: "输入参数合法且符合逻辑",
    input: "{\n    \"teamId\": \"0e259e3026994d27afddf3caf831e30d\",\n    \"userName\": \"Kiwi\"\n}",
    expectedResult: "退出成功"
  },
  {
    caseNumber: "JY_INT_0015_002_001",
    caseDescription: "teamId为null，退出失败",
    input: "{\n    \"teamId\": null,\n    \"userName\": \"Kiwi\"\n}",
    expectedResult: "退出失败"
  },
  {
    caseNumber: "JY_INT_0015_002_002",
    caseDescription: "userName为null，退出失败",
    input: "{\n    \"teamId\": \"0e259e3026994d27afddf3caf831e30d\",\n    \"userName\": null\n}",
    expectedResult: "退出失败"
  },
  {
    caseNumber: "JY_INT_0015_003_001",
    caseDescription: "teamId不存在，退出失败",
    input: "{\n    \"teamId\": \"0e259e3026994d27afddf3caf831e3-d\",\n    \"userName\": null\n}",
    expectedResult: "退出失败"
  },
  {
    caseNumber: "JY_INT_0015_003_002",
    caseDescription: "userName不存在，退出失败",
    input: "{\n    \"teamId\": \"0e259e3026994d27afddf3caf831e30d\",\n    \"userName\": \"Kiki\"\n}",
    expectedResult: "退出失败"
  },
  {
    caseNumber: "JY_INT_0015_004_001",
    caseDescription: "用户为小队的队长，退出失败",
    input: "{\n    \"teamId\": \"0e259e3026994d27afddf3caf831e30d\",\n    \"userName\": \"Sheeep\"\n}",
    expectedResult: "退出失败"
  }
];



const showAllure = ref(false)
const runTest = () => {
  showAllure.value=true
//   axios.get('/api/team/runUnitTest', {
//     params: {
//       className:"com.jiyi.team.service.TeamUnitTest"
//     }
//   })
//   .then(response => {
//     console.log(response)
//     console.log(response.data);
//   })
//   .catch(error => {
//     console.error("请求出错：", error)
//   });
};
</script>

<style scoped>
.unit-card {
  border-radius: 20px;
  height:88vh
}

.report-container {
width: calc(100% + 40px); /* 20px padding * 2 = 40px */
/* height: calc(100% + 40px);  */
height:100vh;
margin: -20px; /* 抵消el-main的默认padding */
display: flex;
justify-content: center;
align-items: center;
}
</style>