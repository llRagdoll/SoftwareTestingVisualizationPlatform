<template>
    <div v-if="!showAllure">

     <el-card class="unit-card" >
        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="创建小队" name="first">
            <el-table :data="testCases1" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="解散小队" name="second">
            <el-table :data="testCases2" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="修改小队" name="third">
            <el-table :data="testCases3" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="收藏小队" name="fourth">
            <el-table :data="testCases4" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="退出小队" name="fifth">
            <el-table :data="testCases5" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="创建邀请" name="sixth">
            <el-table :data="testCases6" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="接受邀请" name="seventh">
            <el-table :data="testCases7" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="拒绝邀请" name="eighth">
            <el-table :data="testCases8" border style="width: 100%" max-height="600">
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

const testCases3=[
        { caseNumber: '001', caseDescription: '修改成功', input: 'teamId="0000000000000000000001", teamName="testName", detail="testDetail"', expectedResult: '小队修改成功' },
        { caseNumber: '002', caseDescription: '修改失败，小队ID为空', input: 'teamId=NULL, teamName="testName", detail="testDetail"', expectedResult: '修改失败，提示小队ID不能为空' },
        { caseNumber: '003', caseDescription: '修改失败，小队ID不存在', input: 'teamId="00000000000000000000-1", teamName="testName", detail="testDetail"', expectedResult: '修改失败，提示小队ID不存在' },
        { caseNumber: '004', caseDescription: '修改失败，小队名长度小于2', input: 'teamId="0000000000000000000001", teamName="t", detail="testDetail"', expectedResult: '修改失败，提示小队长度应不小于2' },
        { caseNumber: '005', caseDescription: '修改失败，小队名长度大于15', input: 'teamId="0000000000000000000001", teamName="1234567890123456", detail="testDetail"', expectedResult: '修改失败，提示小队名长度应不大于15' },
        { caseNumber: '006', caseDescription: '修改失败，小队名为空', input: 'teamId="0000000000000000000001", teamName=NULL, detail="testDetail"', expectedResult: '修改失败，提示小队名不能为空' },
        { caseNumber: '007', caseDescription: '修改失败，小队名重复', input: 'teamId="0000000000000000000001", teamName="testTeamName1", detail="testDetail"', expectedResult: '修改失败，提示小队名不能重复' },
        { caseNumber: '008', caseDescription: '修改失败，描述长度小于5', input: 'teamId="0000000000000000000001", teamName="testTeamName", detail="t"', expectedResult: '修改失败，提示描述长度应不小于5' },
        { caseNumber: '009', caseDescription: '修改失败，描述长度大于100', input: 'teamId="0000000000000000000001", teamName="testTeamName", detail="1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"', expectedResult: '修改失败，提示描述长度应不大于100' },
        { caseNumber: '010', caseDescription: '修改失败，描述为空', input: 'teamId="0000000000000000000001", teamName="testTeamName", detail=NULL', expectedResult: '修改失败，提示描述不能为空' }
      ]
const testCases4 = [
  { caseNumber: '001', caseDescription: '收藏成功', input: 'teamId="0000000000000000000001", userId="0000000000000000000001"', expectedResult: '收藏成功' },
  { caseNumber: '002', caseDescription: '收藏失败，小队ID为空', input: 'teamId=NULL, userId="0000000000000000000001"', expectedResult: '收藏失败，提示小队ID不能为空' },
  { caseNumber: '003', caseDescription: '收藏失败，小队ID不存在', input: 'teamId="00000000000000000000-1", userId="0000000000000000000001"', expectedResult: '收藏失败，提示小队ID不存在' },
  { caseNumber: '004', caseDescription: '收藏失败，用户ID为空', input: 'teamId="0000000000000000000001", userId=NULL', expectedResult: '收藏失败，提示用户ID不能为空' },
  { caseNumber: '005', caseDescription: '收藏失败，用户ID不存在', input: 'teamId="0000000000000000000001", userId="00000000000000000000-1"', expectedResult: '收藏失败，提示用户ID不存在' }
];

const testCases5 = [
  { caseNumber: '001', caseDescription: '退出成功', input: 'teamId="0000000000000000000001", userName="test"', expectedResult: '退出成功' },
  { caseNumber: '002', caseDescription: '退出失败，小队ID为空', input: 'teamId=NULL, userName="test"', expectedResult: '退出失败，提示小队ID不能为空' },
  { caseNumber: '003', caseDescription: '退出失败，小队ID不存在', input: 'teamId="00000000000000000000-1", userName="test"', expectedResult: '退出失败，提示小队ID不存在' },
  { caseNumber: '004', caseDescription: '退出失败，用户名为空', input: 'teamId="0000000000000000000001", userName=NULL', expectedResult: '退出失败，提示用户名不能为空' },
  { caseNumber: '005', caseDescription: '退出失败，用户名不存在', input: 'teamId="0000000000000000000001", userName="test0"', expectedResult: '退出失败，提示用户名不存在' }
];

const testCases6 = [
  { caseNumber: '001', caseDescription: '创建成功', input: 'teamId="0000000000000000000001", userName="test"', expectedResult: '创建成功' },
  { caseNumber: '002', caseDescription: '创建失败，小队ID为空', input: 'teamId=NULL, userName="test"', expectedResult: '创建失败，提示小队ID不能为空' },
  { caseNumber: '003', caseDescription: '创建失败，小队ID不存在', input: 'teamId="00000000000000000000-1", userName="test"', expectedResult: '创建失败，提示小队ID不存在' },
  { caseNumber: '004', caseDescription: '创建失败，用户名为空', input: 'teamId="0000000000000000000001", userName=NULL', expectedResult: '创建失败，提示用户名不能为空' },
  { caseNumber: '005', caseDescription: '创建失败，用户名不存在', input: 'teamId="0000000000000000000001", userName="test0"', expectedResult: '创建失败，提示用户名不存在' },
  { caseNumber: '006', caseDescription: '创建失败，用户已经在小队中', input: 'teamId="0000000000000000000001", userName="test1"', expectedResult: '创建失败，提示用户已在小队中' },
  { caseNumber: '007', caseDescription: '创建失败，用户已经被邀请', input: 'teamId="0000000000000000000000000001", userName="test2"', expectedResult: '创建失败，提示用户已经被邀请' }
];

const testCases7 = [
  { caseNumber: '001', caseDescription: '接受成功', input: 'teamId="0000000000000000000001", userName="test"', expectedResult: '接受成功' },
  { caseNumber: '002', caseDescription: '接受失败，小队ID为空', input: 'teamId=NULL, userName="test"', expectedResult: '接受失败，提示小队ID不能为空' },
  { caseNumber: '003', caseDescription: '接受失败，小队ID不存在', input: 'teamId="00000000000000000000-1", userName="test"', expectedResult: '接受失败，提示小队ID不存在' },
  { caseNumber: '004', caseDescription: '接受失败，用户名为空', input: 'teamId="0000000000000000000001", userName=NULL', expectedResult: '接受失败，提示用户名不能为空' },
  { caseNumber: '005', caseDescription: '接受失败，用户名不存在', input: 'teamId="0000000000000000000001", userName="test0"', expectedResult: '接受失败，提示用户名不存在' }
];

const testCases8 = [
  { caseNumber: '001', caseDescription: '拒绝失败，拒绝邀请中invitationId为空', input: 'invitationId=NULL', expectedResult: '拒绝失败，提示ID不能为空' },
  { caseNumber: '002', caseDescription: '拒绝失败，拒绝邀请中invitationId非空但不存在', input: 'invitationId="00000000000000000000-1"', expectedResult: '拒绝失败，提示ID不存在' },
  { caseNumber: '003', caseDescription: '拒绝成功', input: 'invitationId="0000000000000000000001"', expectedResult: '拒绝成功' }
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