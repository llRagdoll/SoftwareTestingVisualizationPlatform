<template>
    <div v-if="!showAllure">

     <el-card class="unit-card" >
        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="评论景区" name="first">
            <el-table :data="testCases1" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="删除评论" name="second">
            <el-table :data="testCases2" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="点赞评论" name="third">
            <el-table :data="testCases3" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="拉踩评论" name="fourth">
            <el-table :data="testCases4" border style="width: 100%" max-height="600">
                <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
                <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
                <el-table-column prop="input" label="输入"></el-table-column>
                <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="附近景区推荐" name="fifth">
            <el-table :data="testCases5" border style="width: 100%" max-height="600">
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
    caseNumber: 'Unit_Attraction_AS_001_001',
    caseDescription: '成功创建景区评论',
    input: `userID="983dd2ae81b7471fba6449e66f140ade"
commentRequestBody={
  attractionID："2310",
  commentDetail: "好",
  avgScore: 5,
  commentSrc: ['https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312588764-275.jpg', 'https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312589013-955.jpg']
}`,
    expectedResult: '返回true，创建景区评论成功'
  },
  {
    caseNumber: 'Unit_Attraction_AS_001_002',
    caseDescription: '创建景区评论时任意参数为空',
    input: `userID="983dd2ae81b7471fba6449e66f140ade"
commentRequestBody={}`,
    expectedResult: '返回false，反馈评论内容不能为空'
  },
  {
    caseNumber: 'Unit_Attraction_AS_001_002_001',
    caseDescription: '创建景区评论时，avgScore参数为null',
    input: `userID="983dd2ae81b7471fba6449e66f140ade"
commentRequestBody={
  attractionID："2310",
  commentDetail: "好",
  avgScore: null,
  commentSrc: ['https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312588764-275.jpg', 'https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312589013-955.jpg']
}`,
    expectedResult: '返回false，反馈评论中评分不能为空'
  },
  {
    caseNumber: 'Unit_Attraction_AS_001_002_002',
    caseDescription: '创建景区评论时，commentDetail参数为空字符串',
    input: `userID="983dd2ae81b7471fba6449e66f140ade"
commentRequestBody={
  attractionID："2310",
  commentDetail: "",
  avgScore: 5,
  commentSrc: ['https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312588764-275.jpg', 'https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312589013-955.jpg']
}`,
    expectedResult: '返回false，反馈评论中评论详情不能为空'
  },
  {
    caseNumber: 'Unit_Attraction_AS_001_002_003',
    caseDescription: '创建景区评论时，attractionID参数为空字符串',
    input: `userID="983dd2ae81b7471fba6449e66f140ade"
commentRequestBody={
  attractionID："",
  commentDetail: "好",
  avgScore: 5,
  commentSrc: ['https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312588764-275.jpg', 'https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312589013-955.jpg']
}`,
    expectedResult: '返回false，反馈景区id不可为空'
  },
  {
    caseNumber: 'Unit_Attraction_AS_001_002_004',
    caseDescription: '创建景区评论时，userID参数为空字符串',
    input: `userID=""
commentRequestBody={
  attractionID："2310",
  commentDetail: "好",
  avgScore: 5,
  commentSrc: ['https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312588764-275.jpg', 'https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312589013-955.jpg']
}`,
    expectedResult: '返回false，反馈用户id不可为空'
  },
  {
    caseNumber: 'Unit_Attraction_AS_001_003',
    caseDescription: '创建景区评论时，景区id非空但不存在',
    input: `userID="983dd2ae81b7471fba6449e66f140ade"
commentRequestBody={
  attractionID："wobucunzai",
  commentDetail: "好",
  avgScore: 5,
  commentSrc: ['https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312588764-275.jpg', 'https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312589013-955.jpg']
}`,
    expectedResult: '返回false，反馈不可对未录入景区发布评论'
  },
  {
    caseNumber: 'Unit_Attraction_AS_001_004',
    caseDescription: '创建景区评论时，用户id非空但不存在',
    input: `userID="wobucunzai"
commentRequestBody={
  attractionID："2310",
  commentDetail: "好",
  avgScore: 5,
  commentSrc: ['https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312588764-275.jpg', 'https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717312589013-955.jpg']
}`,
    expectedResult: '返回false，反馈未注册用户不可发布景区评论'
  }
];


const testCases2 = [
  {
    caseNumber: 'Unit_Attraction_AS_002_001',
    caseDescription: '删除评论中任意参数为空',
    input: `userID=""
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"`,
    expectedResult: '返回false，提示userID不能为空'
  },
  {
    caseNumber: 'Unit_Attraction_AS_002_001_002',
    caseDescription: '删除评论中任意参数为空',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID=""`,
    expectedResult: '返回false，提示commentID不能为空'
  },
  {
    caseNumber: 'Unit_Attraction_AS_002_002',
    caseDescription: '删除评论中userID非空但不存在',
    input: `userID="wobucunzai"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"`,
    expectedResult: '返回false，提示userID不存在'
  },
  {
    caseNumber: 'Unit_Attraction_AS_002_003',
    caseDescription: '删除评论中commentID非空但不存在',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="wobucunzai"`,
    expectedResult: '返回false，提示commentID不存在'
  },
  {
    caseNumber: 'Unit_Attraction_AS_002_004',
    caseDescription: 'userID和commentID均合法，删除成功',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"`,
    expectedResult: '返回true，删除成功'
  },
  {
    caseNumber: 'Unit_Attraction_AS_002_005',
    caseDescription: '删除人userID和commentID不匹配',
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
commentID="52c20f9b-e854-46dd-a6be-f0c078d180c3"`,
    expectedResult: '返回false，提示非自己发布的评论无法删除'
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

const testCases4 = [
  {
    caseNumber: 'Unit_Attraction_AS_004_001',
    caseDescription: '成功拉踩景区评论',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 1
    },
    expectedResult: '返回true，拉踩成功'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_001',
    caseDescription: '成功取消拉踩景区评论',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 0
    },
    expectedResult: '返回true，取消拉踩成功'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_002',
    caseDescription: '改变拉踩状态时任意参数为空',
    input: {
      userID: '',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 1
    },
    expectedResult: '返回false，用户id不能为空，拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_002',
    caseDescription: '改变拉踩状态时任意参数为空',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: '',
      type: 1
    },
    expectedResult: '返回false，评论id不能为空，拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_002',
    caseDescription: '改变拉踩状态时任意参数为空',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: null
    },
    expectedResult: '返回false，type不能为空，拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_003',
    caseDescription: '改变拉踩状态时，commentID非空但是不存在',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: 'wobucunzai',
      type: 1
    },
    expectedResult: '返回false，评论不存在，拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_003',
    caseDescription: '改变拉踩状态时，commentID非空但是不存在',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: 'wobucunzai',
      type: 0
    },
    expectedResult: '返回false，评论不存在，取消拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_004',
    caseDescription: '改变拉踩状态时，userID非空但是不存在',
    input: {
      userID: 'wobucunzai',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 1
    },
    expectedResult: '返回false，用户不存在，拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_004',
    caseDescription: '改变拉踩状态时，userID非空但是不存在',
    input: {
      userID: 'wobucunzai',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 0
    },
    expectedResult: '返回false，用户不存在，取消拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_005',
    caseDescription: '改变拉踩状态时，type值不合法',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 3
    },
    expectedResult: '返回false，type值不合法，点赞/取消拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_005',
    caseDescription: '改变拉踩状态时，type值不合法',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 1
    },
    expectedResult: '但数据库里已有该用户对该评论的拉踩，返回false，数据库已有对应点赞，拉踩失败'
  },
  {
    caseNumber: 'Unit_Attraction_AS_004_005',
    caseDescription: '改变拉踩状态时，type值不合法',
    input: {
      userID: '10C66B755C184EDF91EC80E526E0C183',
      commentID: '52c20f9b-e854-46dd-a6be-f0c078d180c3',
      type: 0
    },
    expectedResult: '但数据库里没有该用户对该评论的拉踩，返回false，数据库没有对应点赞，取消拉踩失败'
  }
];


const testCases5 = [
  {
    "caseNumber": "Unit_Note_NS_005_001",
    "caseDescription": "获取附近景区列表成功",
    "input": "longitude=116.2972404837544, latitude=40.00526406522876",
    "expectedResult": "返回附近景区列表，获取附近景区列表成功"
  },
  {
    "caseNumber": "Unit_Note_NS_005_002",
    "caseDescription": "获取附近景区时任意参数为空",
    "input": "longitude=116.2972404837544, latitude=null",
    "expectedResult": "返回获取失败结果，纬度信息为空"
  },
  {
    "caseNumber": "Unit_Note_NS_005_002",
    "caseDescription": "获取附近景区时任意参数为空",
    "input": "longitude=null, latitude=40.00526406522876",
    "expectedResult": "返回获取失败结果，经度信息为空"
  },
  {
    "caseNumber": "Unit_Note_NS_005_003",
    "caseDescription": "获取附近景区时任意参数不合法",
    "input": "longitude=116.2972404837544, latitude=\"123\"",
    "expectedResult": "返回获取失败结果，纬度信息不合法"
  },
  {
    "caseNumber": "Unit_Note_NS_005_003",
    "caseDescription": "获取附近景区时任意参数不合法",
    "input": "longitude=\"123\", latitude=40.00526406522876",
    "expectedResult": "返回获取失败结果，经度信息不合法"
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