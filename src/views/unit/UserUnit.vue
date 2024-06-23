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
    caseNumber: "Unit_User_US_001_001",
    caseDescription: "用户注册成功",
    input: "nickname=\"yy\" password=\"yy123456..\" phoneNumber=\"13576051402\"",
    expectedResult: "返回true，用户注册成功"
  },
  {
    caseNumber: "Unit_User_US_001_002",
    caseDescription: "用户注册时任意参数为空",
    input: "nickname=\"\" password=\"yy123456..\" phoneNumber=\"13576051402\"",
    expectedResult: "返回false，反馈用户名为空"
  },
  {
    caseNumber: "Unit_User_US_001_002",
    caseDescription: "用户注册时任意参数为空",
    input: "nickname=\"yy\" password=\"\" phoneNumber=\"13576051402\"",
    expectedResult: "返回false，反馈密码为空"
  },
  {
    caseNumber: "Unit_User_US_001_002",
    caseDescription: "用户注册时任意参数为空",
    input: "nickname=\"yy\" password=\"yy123456..\" phoneNumber=\"\"",
    expectedResult: "返回false，反馈手机号为空"
  },
  {
    caseNumber: "Unit_User_US_001_003",
    caseDescription: "用户注册使用的nickname非合法",
    input: "nickname=\"yy\" password=\"yy123456..\" phoneNumber=\"13576051402\"",
    expectedResult: "返回false，反馈该用户已存在"
  },
  {
    caseNumber: "Unit_User_US_001_003",
    caseDescription: "用户注册使用的nickname非合法",
    input: "nickname=\"yyyyyyyyyyyyyyy\" password=\"yy123456..\" phoneNumber=\"13576051402\"",
    expectedResult: "用户名超过长度限制，注册失败"
  },
  {
    caseNumber: "Unit_User_US_001_004",
    caseDescription: "用户注册使用的password非合法",
    input: "nickname=\"yy\" password=\"你好\" phoneNumber=\"13576051402\"",
    expectedResult: "返回false，反馈密码存在非法字符"
  },
  {
    caseNumber: "Unit_User_US_001_004",
    caseDescription: "用户注册使用的password非合法",
    input: "nickname=\"yy\" password=\"11\" phoneNumber=\"13576051402\"",
    expectedResult: "返回false，反馈密码过短"
  },
  {
    caseNumber: "Unit_User_US_001_004",
    caseDescription: "用户注册使用的password非合法",
    input: "nickname=\"yy\" password=\"111111111111111111111111\" phoneNumber=\"13576051402\"",
    expectedResult: "返回false，反馈密码过长"
  },
  {
    caseNumber: "Unit_User_US_001_005",
    caseDescription: "用户注册使用的phoneNumber非合法",
    input: "nickname=\"yy\" password=\"yy123456..\" phoneNumber=\"13576051402\"",
    expectedResult: "返回false，反馈该手机号已注册"
  },
  {
    caseNumber: "Unit_User_US_001_005",
    caseDescription: "用户注册使用的phoneNumber非合法",
    input: "nickname=\"yy\" password=\"yy123456..\" phoneNumber=\"135760514021\"",
    expectedResult: "返回false，反馈手机号长度错误"
  },
  {
    caseNumber: "Unit_User_US_001_005",
    caseDescription: "用户注册使用的phoneNumber非合法",
    input: "nickname=\"yy\" password=\"yy123456..\" phoneNumber=\"13576051abc\"",
    expectedResult: "返回false，反馈手机号包含非法字符"
  }
];


const testCases2 = [
  {
    caseNumber: "Unit_User_US_002_001",
    caseDescription: "用户登录成功",
    input: "nickname=\"yy\" password=\"yy123456..\"",
    expectedResult: "返回true，登录成功"
  },
  {
    caseNumber: "Unit_User_US_002_002",
    caseDescription: "用户登录时任意参数为空",
    input: "nickname=\"\" password=\"yy123456..\"",
    expectedResult: "返回false，反馈用户名为空"
  },
  {
    caseNumber: "Unit_User_US_002_002",
    caseDescription: "用户登录时任意参数为空",
    input: "nickname=\"yy\" password=\"\"",
    expectedResult: "返回false，反馈密码为空"
  },
  {
    caseNumber: "Unit_User_US_002_003",
    caseDescription: "该用户不存在",
    input: "nickname=\"wobucunzai\" password=\"yy123456..\"",
    expectedResult: "返回false，反馈该用户不存在"
  },
  {
    caseNumber: "Unit_User_US_002_004",
    caseDescription: "用户登录时password与nickname不匹配",
    input: "nickname=\"jone\" password=\"yy123456..\"",
    expectedResult: "返回false，反馈用户密码错误"
  },
  {
    caseNumber: "Unit_User_US_002_005",
    caseDescription: "用户登录输入字段良好，但是用户被拉黑",
    input: "nickname=\"jone\" password=\"yy123456..\"",
    expectedResult: "返回false，反馈用户已被拉黑"
  }
];


const testCases3 = [
  {
    caseNumber: "Unit_User_US_003_004",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "11"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: 0
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中birthday字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_004",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211"
  fans: 0
  follows: 0
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中email字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_004",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: 0
  gender: 3
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中gender字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_004",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: 0
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 3
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中vipGrade字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_004",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: 0
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yyyyyyyyyyyyyyyyyyy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中nickName字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_005",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: 0
  gender: 0
  headImageUrl: ""
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中headImageUrl字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_006",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: ""
  fans: 0
  follows: 0
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中email字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_007",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: ""
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: 0
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中birthday字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_008",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: ""
  follows: 0
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中fans字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_009",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: ""
  gender: 0
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中follows字段不合法"
  },
  {
    caseNumber: "Unit_User_US_003_010",
    caseDescription: "用户修改个人信息时UserBasicDTO非空，但是里面字段不合法",
    input: `userID="10C66B755C184EDF91EC80E526E0C183"
UserBasicDTO={
  birthday: "2002-07-30T16:00:00.000+00:00"
  duration: 29
  email: "2152211@tongji.edu.cn"
  fans: 0
  follows: 0
  gender: ""
  headImageUrl: "https://jiyi-microservice.oss-cn-beijing.aliyuncs.com/storage/1717337521827.png"
  location: "上海市"
  nickName: "yy"
  phoneNumber: "15577357881"
  vipGrade: 0
  wechatNumber: "huhu"
}`,
    expectedResult: "返回false，反馈修改信息中gender字段不合法"
  }
];

const testCases4 = [
  {
    caseNumber: "Unit_Note_NS_004_001",
    caseDescription: "拉黑用户成功",
    input: `userID="user000000000000000001"
userStatus=1`,
    expectedResult: "返回true，拉黑用户成功"
  },
  {
    caseNumber: "Unit_Note_NS_004_002",
    caseDescription: "拉黑时部分参数为空",
    input: `userID=""
userStatus=1`,
    expectedResult: "返回false，反馈用户id为空"
  },
  {
    caseNumber: "Unit_Note_NS_004_002",
    caseDescription: "拉黑时部分参数为空",
    input: `userID="user000000000000000001"
userStatus=null`,
    expectedResult: "返回false，反馈拉黑状态为空"
  },
  {
    caseNumber: "Unit_Note_NS_004_003",
    caseDescription: "被拉黑用户不存在",
    input: `userID="wobucunzai"
userStatus=1`,
    expectedResult: "返回false，反馈用户不存在"
  },
  {
    caseNumber: "Unit_Note_NS_004_004",
    caseDescription: "输入拉黑状态不合法",
    input: `userID="user000000000000000001"
userStatus=0`,
    expectedResult: "返回false，反馈拉黑状态非法"
  },
  {
    caseNumber: "Unit_Note_NS_004_004",
    caseDescription: "输入拉黑状态不合法",
    input: `userID="user000000000000000001"
userStatus=1但是该用户拉黑状态已经是1，不能重复拉黑`,
    expectedResult: "返回false，反馈不能重复拉黑"
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