<template>
    <div v-if="!showReport">
    <el-card class="unit-card">
       <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
       <el-tab-pane label="创建随记" name="first">
           <el-table :data="testCases1" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="删除随记" name="second">
           <el-table :data="testCases2" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="搜索随记" name="third">
           <el-table :data="testCases3" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="评论随记" name="fourth">
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
//import axios from 'axios';
const showReport = ref(false)

const activeName = ref('first') 
const handleClick = (tab, event) => {
   console.log(tab, event)
}
const testCases1 = [
    {
        caseNumber: "JY_INT_008_001_001",
        caseDescription: "输入值合法 - overt 为 true",
        input: '{"trackID": "3F27DEA3953DEEC84E5F223B437D092C","overt": true,"note":{"title":"上海三日游","articleBody":"aaaaaaaaaaaaaaaaaaaaaaaaa"}}',
        expectedResult: "true"
    },
    {
        caseNumber: "JY_INT_008_001_002",
        caseDescription: "输入值合法 - overt 为 false",
        input: '{"trackID": "3F27DEA3953DEEC84E5F223B437D092C","overt": false,"note":{"title":"上海三日游","articleBody":"aaaaaaaaaaaaaaaaaaaaaaaaa"}}',
        expectedResult: "true"
    },
    {
        caseNumber: "JY_INT_008_002_001",
        caseDescription: "trackID 为空",
        input: '{"trackID": "","overt": true,"note":{"title":"上海三日游","articleBody":"aaaaaaaaaaaaaaaaaaaaaaaaa"}}',
        expectedResult: "false"
    },
    {
        caseNumber: "JY_INT_008_002_002",
        caseDescription: "trackID 不为空但不存在",
        input: '{"trackID": "3F27DEA3953DEEC84E5F223B437D092C-1","overt": true,"note":{"title":"上海三日游","articleBody":"aaaaaaaaaaaaaaaaaaaaaaaaa"}}',
        expectedResult: "false"
    },
    {
        caseNumber: "JY_INT_008_002_003",
        caseDescription: "title 为空",
        input: '{"trackID": "3F27DEA3953DEEC84E5F223B437D092C","overt": true,"note":{"title":"","articleBody":"aaaaaaaaaaaaaaaaaaaaaaaaa"}}',
        expectedResult: "false"
    },
    {
        caseNumber: "JY_INT_008_002_004",
        caseDescription: "title 超过字数上限",
        input: '{"trackID": "3F27DEA3953DEEC84E5F223B437D092C","overt": true,"note":{"title":"人均8000元三天两晚上海旅行","articleBody":"aaaaaaaaaaaaaaaaaaaaaaaaa"}}',
        expectedResult: "false"
    },
    {
        caseNumber: "JY_INT_008_002_005",
        caseDescription: "articleBody 为空",
        input: '{"trackID": "3F27DEA3953DEEC84E5F223B437D092C","overt": true,"note":{"title":"上海三日游","articleBody":""}}',
        expectedResult: "false"
    },
    {
        caseNumber: "JY_INT_008_002_006",
        caseDescription: "articleBody 超过字数上限",
        input: '{"trackID": "3F27DEA3953DEEC84E5F223B437D092C","overt": true,"note":{"title":"上海三日游","articleBody":"这次的上海旅行真是令人难忘。我们参观了外滩、东方明珠塔和上海博物馆。外滩的夜景美得让人惊叹，东方明珠塔的高度让人感受到城市的现代化，而上海博物馆则展现了丰富的历史文化。整个旅程充满了惊喜和感动，是一次难得的经历。"}}',
        expectedResult: "false"
    }
];


const testCases2 = [
  {
    caseNumber: "JY_INT_009_001",
    caseDescription: "noteID合法，返回true",
    input: "{ \"noteID\": \"7FB98E7F9A834E64AC8C7B3FFAEAAFFC\" }",
    expectedResult: "true"
  },
  {
    caseNumber: "JY_INT_009_002", 
    caseDescription: "noteID为空，返回false",
    input: "{ \"noteID\": \"\" }",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_009_002", 
    caseDescription: "noteID不为空但不存在，返回false",
    input: "{ \"noteID\": \"7FB98E7F9A834E64AC8C7B3FFAEAAFFC-1\" }",
    expectedResult: "false"
  }
];

const testCases3 = [
  {
    caseNumber: "JY_INT_0010_001",
    caseDescription: "两者均合法，返回true",
    input: "{\n    \"noteID\": \"3F27DEA3953DEEC84E5F223B437D092C\",\n    \"userID\":\"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "true"
  },
  {
    caseNumber: "JY_INT_0010_001",
    caseDescription: "noteID为空，返回false",
    input: "{\n    \"noteID\": \"\",\n    \"userID\":\"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0010_001",
    caseDescription: "noteID不为空但不存在，返回false",
    input: "{\n    \"noteID\": \"3F27DEA3953DEEC84E5F223B437D092C-1\",\n    \"userID\":\"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0010_001",
    caseDescription: "userID为空，返回false",
    input: "{\n    \"noteID\": \"3F27DEA3953DEEC84E5F223B437D092C\",\n    \"userID\":\"\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0010_001",
    caseDescription: "userID不为空但不存在，返回false",
    input: "{\n    \"noteID\": \"3F27DEA3953DEEC84E5F223B437D092C\",\n    \"userID\":\"3D4E2D5DE08945CCBBF0AAA18B3D92BD-1\"\n}",
    expectedResult: "false"
  }
];

const testCases4 = [
  {
    caseNumber: "JY_INT_0011_001",
    caseDescription: "输入值合法",
    input: "{\n    \"noteID\": \"2DEF9CAA255E4EF3930BC2675512D7BE\",\n    \"content\": \"我也想旅游！\",\n    \"userID\": \"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "true"
  },
  {
    caseNumber: "JY_INT_0011_001",
    caseDescription: "noteID为空，返回false",
    input: "{\n    \"noteID\": \"\",\n    \"content\": \"我也想旅游！\",\n    \"userID\": \"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0011_001",
    caseDescription: "noteID不为空但不存在，返回false",
    input: "{\n    \"noteID\": \"2DEF9CAA255E4EF3930BC2675512D7BE-1\",\n    \"content\": \"我也想旅游！\",\n    \"userID\": \"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0011_001",
    caseDescription: "content为空，返回false",
    input: "{\n    \"noteID\": \"2DEF9CAA255E4EF3930BC2675512D7BE\",\n    \"content\": \"\",\n    \"userID\": \"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0011_001",
    caseDescription: "content大于50字符，返回false",
    input: "{\n    \"noteID\": \"2DEF9CAA255E4EF3930BC2675512D7BE\",\n    \"content\": \"没想到还有这么漂亮的地方，我的女朋友一定会喜欢这里。这个暑假我可以带她一起来，到时候就参照这个旅游路线！\",\n    \"userID\": \"3D4E2D5DE08945CCBBF0AAA18B3D92BD\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0011_001",
    caseDescription: "userID为空，返回false",
    input: "{\n    \"noteID\": \"2DEF9CAA255E4EF3930BC2675512D7BE\",\n    \"content\": \"我也想旅游！\",\n    \"userID\": \"\"\n}",
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_0011_001",
    caseDescription: "userID不为空但不存在，返回false",
    input: "{\n    \"noteID\": \"2DEF9CAA255E4EF3930BC2675512D7BE\",\n    \"content\": \"我也想旅游！\",\n    \"userID\": \"3D4E2D5DE08945CCBBF0AAA18B3D92BD-1\"\n}",
    expectedResult: "false"
  }
];





const runTest = () => {
    showReport.value = true
//  axios.get('/api/team/runUnitTest', {
//    params: {
//      className:"com.jiyi.team.service.TeamUnitTest"
//    }
//  })
//  .then(response => {
//    console.log(response)
//    console.log(response.data);
//  })
//  .catch(error => {
//    console.error("请求出错：", error)
//  });
};
</script>

<style scoped>
.unit-card {
   border-radius: 20px;
   height:88vh
}
</style>