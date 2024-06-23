<template>
    <div v-if="!showAllure">
    <el-card class="unit-card">
       <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
       <el-tab-pane label="注册" name="first">
           <el-table :data="testCases1" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="登录" name="second">
           <el-table :data="testCases2" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="修改信息" name="third">
           <el-table :data="testCases3" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="拉黑用户" name="fourth">
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
    <div v-else class="report-container">
        <iframe src="http://localhost:12346" style="width:100%;height:100vh;border:none"></iframe>
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
    caseNumber: "JY_INT_001_001_001",
    caseDescription: "输入值合法",
    input: 'nickname="yy", password="yy123456..", phoneNumber="13576051402"',
    expectedResult: "true"
  },
  {
    caseNumber: "JY_INT_001_002_001",
    caseDescription: "输入不合法，nickname为空",
    input: 'nickname="", password="yy123456..", phoneNumber="13576051402"',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_002_002",
    caseDescription: "输入不合法，password为空",
    input: 'nickname="yy", password="", phoneNumber="13576051402"',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_002_003",
    caseDescription: "输入不合法，phoneNumber为空",
    input: 'nickname="yy", password="yy123456..", phoneNumber=""',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_002_004",
    caseDescription: "输入不合法，nickname超过长度限制",
    input: 'nickname="yyyyyyyyyyyyyyy", password="yy123456..", phoneNumber="13576051402"',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_002_005",
    caseDescription: "输入不合法，password不符合长度规定",
    input: 'nickname="yy", password="11", phoneNumber="13576051402"',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_002_006",
    caseDescription: "输入不合法，password中包含非ASCII字符",
    input: 'nickname="yy", password="yyyyyy好啊", phoneNumber="13576051402"',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_002_007",
    caseDescription: "输入不合法，phoneNumber为不符合典型有效值",
    input: 'nickname="yy", password="yy123456..", phoneNumber="1123"',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_002_008",
    caseDescription: "输入不合法，phoneNumber包含非数字型字符",
    input: 'nickname="yy", password="yy123456..", phoneNumber="1357605140y"',
    expectedResult: "false"
  },
  {
    caseNumber: "JY_INT_001_003_001",
    caseDescription: "输入值合法，但是不符合业务逻辑，用户已注册",
    input: 'nickname="danel", password="yy123456..", phoneNumber="13576051402"',
    expectedResult: "注册失败"
  },
  {
    caseNumber: "JY_INT_001_003_002",
    caseDescription: "输入值合法，但是不符合业务逻辑，手机号已注册",
    input: 'nickname="yy", password="yy123456", phoneNumber="13970917031"',
    expectedResult: "注册失败"
  }
];



const testCases2 = [
  {
    caseNumber: "JY_INT_002_001_001",
    caseDescription: "输入参数均为nom",
    input: 'nickname="yy", password="yy123456.."',
    expectedResult: "return true;"
  },
  {
    caseNumber: "JY_INT_002_002_001",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="", password="yy123456.."',
    expectedResult: "return false;"
  },
  {
    caseNumber: "JY_INT_002_002_002",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="y", password="yy123456.."',
    expectedResult: "return true;"
  },
  {
    caseNumber: "JY_INT_002_002_003",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="yyyyyyyyyy", password="yy123456.."',
    expectedResult: "return true;"
  },
  {
    caseNumber: "JY_INT_002_002_004",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="yyyyyyyyyyy", password="yy123456.."',
    expectedResult: "return false;"
  },
  {
    caseNumber: "JY_INT_002_002_005",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="yy", password="yy12"',
    expectedResult: "return false;"
  },
  {
    caseNumber: "JY_INT_002_002_006",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="yy", password="yy123"',
    expectedResult: "return true;"
  },
  {
    caseNumber: "JY_INT_002_002_007",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="yy", password="yy12345678910.."',
    expectedResult: "return true;"
  },
  {
    caseNumber: "JY_INT_002_002_008",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="yy", password="yy123456789101.."',
    expectedResult: "return false;"
  },
  {
    caseNumber: "JY_INT_002_002_009",
    caseDescription: "nickname取边界值、password取边界值",
    input: 'nickname="yyyyyyy", password="yy12345"',
    expectedResult: "return true;"
  },
  {
    caseNumber: "JY_INT_002_003_001",
    caseDescription: "输入参数合法，但是不符合业务逻辑",
    input: 'nickname="denal", password="yy123456.."',
    expectedResult: "用户名与密码不匹配，登录失败"
  }
];



const testCases3 = [
  {
    caseNumber: "JN_INT_003_001_001",
    caseDescription: "输入参数合法情况",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", UserBasicDTO={birthday: "2002-07-30T16:00:00.000+00:00", duration: 29, email: "2152211@tongji.edu.cn", fans: 0, follows: 0, gender: 0, headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png", location: "上海市", nickName: "yy", phoneNumber: "15577357881", vipGrade: 0, wechatNumber: "huhu"}',
    expectedResult: "User information updated successfully."
  },
  {
    caseNumber: "JN_INT_003_002_001",
    caseDescription: "输入特定参数自身类型或值不合法的情况，userID为空",
    input: 'userID="", UserBasicDTO={birthday: "2002-07-30T16:00:00.000+00:00", duration: 29, email: "2152211@tongji.edu.cn", fans: 0, follows: 0, gender: 0, headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png", location: "上海市", nickName: "yy", phoneNumber: "15577357881", vipGrade: 0, wechatNumber: "huhu"}',
    expectedResult: "Failed to update user information."
  },
  {
    caseNumber: "JN_INT_003_002_002",
    caseDescription: "输入特定参数自身类型或值不合法的情况，UserBasicDTO为空",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", UserBasicDTO={}',
    expectedResult: "Failed to update user information."
  },
  {
    caseNumber: "JN_INT_003_002_003",
    caseDescription: "输入特定参数自身类型或值不合法的情况，UserBasicDTO中有部分字段为空",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", UserBasicDTO={birthday: "", duration: 29, email: "2152211@tongji.edu.cn", fans: 0, follows: 0, gender: 0, headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png", location: "上海市", nickName: "yy", phoneNumber: "15577357881", vipGrade: 0, wechatNumber: "huhu"}',
    expectedResult: "Failed to update user information."
  },
  {
    caseNumber: "JN_INT_003_002_004",
    caseDescription: "输入特定参数自身类型或值不合法的情况，gender字段不合法",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", UserBasicDTO={birthday: "", duration: 29, email: "2152211@tongji.edu.cn", fans: 0, follows: 0, gender: 3, headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png", location: "上海市", nickName: "yy", phoneNumber: "15577357881", vipGrade: 0, wechatNumber: "huhu"}',
    expectedResult: "Failed to update user information."
  },
  {
    caseNumber: "JN_INT_003_002_005",
    caseDescription: "输入特定参数自身类型或值不合法的情况，email字段不合法",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", UserBasicDTO={birthday: "", duration: 29, email: "2152211", fans: 0, follows: 0, gender: 0, headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png", location: "上海市", nickName: "yy", phoneNumber: "15577357881", vipGrade: 0, wechatNumber: "huhu"}',
    expectedResult: "Failed to update user information."
  },
  {
    caseNumber: "JN_INT_003_002_006",
    caseDescription: "输入特定参数自身类型或值不合法的情况，vip标识字段不合法",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", UserBasicDTO={birthday: "", duration: 29, email: "2152211@tongji.edu.cn", fans: 0, follows: 0, gender: 0, headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png", location: "上海市", nickName: "yy", phoneNumber: "15577357881", vipGrade: 2, wechatNumber: "huhu"}',
    expectedResult: "Failed to update user information."
  },
  {
    caseNumber: "JN_INT_003_003_001",
    caseDescription: "输入参数合法但不符合业务逻辑",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", UserBasicDTO={birthday: "2002-07-30T16:00:00.000+00:00", duration: 29, email: "2152211@tongji.edu.cn", fans: 0, follows: 0, gender: 0, headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png", location: "上海市", nickName: "yy", phoneNumber: "15577357881", vipGrade: 0, wechatNumber: "huhu"}',
    expectedResult: "Failed to update user information."
  }
];


const testCases4 = [
  {
    caseNumber: "JY_INT_0019_001_001",
    caseDescription: "输入值合法",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", userStatus=1',
    expectedResult: "userID合法且符合业务逻辑，返回true"
  },
  {
    caseNumber: "JY_INT_0019_002_001",
    caseDescription: "输入特定参数为空或不合法的情况，userID为空",
    input: 'userID="", userStatus=1',
    expectedResult: "userID为空，返回false"
  },
  {
    caseNumber: "JY_INT_0019_002_002",
    caseDescription: "输入特定参数为空或不合法的情况，userStatus不为1",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", userStatus=0',
    expectedResult: "userStatus不为1，返回false"
  },
  {
    caseNumber: "JY_INT_0019_002_003",
    caseDescription: "输入特定参数为空或不合法的情况，userID不存在",
    input: 'userID="10C66B755C184EDF91EC80E526E0C182", userStatus=0',
    expectedResult: "userID不存在，返回false"
  },
  {
    caseNumber: "JY_INT_0019_003_001",
    caseDescription: "输入参数合法但不符合业务逻辑",
    input: 'userID="10C66B755C184EDF91EC80E526E0C183", userStatus=1',
    expectedResult: "该用户已被拉黑，不能重复拉黑，返回false"
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