<template>
    <div v-if="!showAllure">

     <el-card class="unit-card" >
        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="修改点赞" name="first">
            <el-table :data="testCases2" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="获取景区天气" name="second">
            <el-table :data="testCases1" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="智能推荐" name="third">
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
        <iframe src="http://localhost:12342" style="width:100%;height:100vh;border:none"></iframe>
    </div>
</template>

<script setup>
import { ref } from 'vue'
//import axios from 'axios';


const activeName = ref('first') 
const handleClick = (tab, event) => {
    console.log(tab, event)
}
const testCases1 = [
  {
    caseNumber: "JY_INT_0017_001",
    caseDescription: "输入值合法",
    input: "{ \"attractionID\": \"10C66B755C184EDF91EC80E526E0C183\" }",
    expectedResult: "true"
  },
  {
    caseNumber: "JY_INT_0017_002",
    caseDescription: "attractionID为空，获取天气失败",
    input: "{ \"attractionID\": \"\" }",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0017_003",
    caseDescription: "attractionID不存在，获取天气失败",
    input: "{ \"attractionID\": \"10C66B755C184EDF91EC80E526E0C183-1\" }",
    expectedResult: "false"
  }
];


const testCases2 = [
  // JY_INT_0018_001 测试项
  {
    caseNumber: "JY_INT_0018_001_001",
    caseDescription: "userID、commentID，type均合法，且符合取消点赞业务逻辑",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C183\",\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c3\",\n    \"type\": 0\n}",
    expectedResult: "true"
  },
  {
    caseNumber: "JY_INT_0018_001_002",
    caseDescription: "userID、commentID，type均合法，且符合新增点赞业务逻辑",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C183\",\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c3\",\n    \"type\": 1\n}",
    expectedResult: "true"
  },

  // JY_INT_0018_002 测试项
  {
    caseNumber: "JY_INT_0018_002_001",
    caseDescription: "userID为空",
    input: "{\n    \"userID\": null,\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c3\",\n    \"type\": 1\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0018_002_002",
    caseDescription: "commentID为空",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C183\",\n    \"commentID\": null,\n    \"type\": 1\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0018_002_003",
    caseDescription: "userID不存在",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C182\",\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c3\",\n    \"type\": 1\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0018_002_004",
    caseDescription: "commentID不存在",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C183\",\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c2\",\n    \"type\": 1\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0018_002_005",
    caseDescription: "type值非法",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C183\",\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c3\",\n    \"type\": 3\n}",
    expectedResult: "false"
  },

  // JY_INT_0018_003 测试项
  {
    caseNumber: "JY_INT_0018_003_001",
    caseDescription: "合法但数据库中没有该点赞，不能取消",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C183\",\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c3\",\n    \"type\": 0\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0018_003_002",
    caseDescription: "合法但数据库中已有点赞，不能再次点赞",
    input: "{\n    \"userID\": \"10C66B755C184EDF91EC80E526E0C183\",\n    \"commentID\": \"52c20f9b-e854-46dd-a6be-f0c078d180c3\",\n    \"type\": 1\n}",
    expectedResult: "false"
  }
];


const testCases3 = [
  {
    caseNumber: 'Unit_Attraction_AS_003_001',
    caseDescription: '成功点赞景区评论',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=1`,
    expectedResult: '返回true，点赞成功'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_001_002',
    caseDescription: '成功取消点赞景区评论',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=0`,
    expectedResult: '返回true，取消点赞成功'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_002',
    caseDescription: '改变点赞状态时任意参数为空',
    input: `userID=""
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=1`,
    expectedResult: '返回false，用户id不能为空，点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_002_002',
    caseDescription: '改变点赞状态时任意参数为空',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID=""
type=1`,
    expectedResult: '返回false，评论id不能为空，点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_002_003',
    caseDescription: '改变点赞状态时任意参数为空',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=null`,
    expectedResult: '返回false，type不能为空，点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_003',
    caseDescription: '改变点赞状态时，commentID非空但是不存在',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="wobucunzai"
type=1`,
    expectedResult: '返回false，评论不存在，点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_003_002',
    caseDescription: '改变点赞状态时，commentID非空但是不存在',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="wobucunzai"
type=0`,
    expectedResult: '返回false，评论不存在，取消点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_004',
    caseDescription: '改变点赞状态时，userID非空但是不存在',
    input: `userID="wobucunzai"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=1`,
    expectedResult: '返回false，用户不存在，点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_004_002',
    caseDescription: '改变点赞状态时，userID非空但是不存在',
    input: `userID="wobucunzai"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=0`,
    expectedResult: '返回false，用户不存在，取消点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_005',
    caseDescription: '改变点赞状态时，type值不合法',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=3`,
    expectedResult: '返回false，type值不合法，点赞/取消点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_005_002',
    caseDescription: '改变点赞状态时，type为1但数据库已有对应点赞',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=1`,
    expectedResult: '返回false，数据库已有对应点赞，点赞失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_003_005_003',
    caseDescription: '改变点赞状态时，type为0但数据库没有对应点赞',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"
type=0`,
    expectedResult: '返回false，数据库没有对应点赞，取消点赞失败'
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