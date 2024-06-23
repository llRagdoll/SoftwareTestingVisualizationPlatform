<template>
    <div v-if="!showReport">
    <el-card class="unit-card">
       <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
       <el-tab-pane label="创建随记" name="first">
           <el-table :data="testCases1" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="用例序号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="修改随记" name="second">
           <el-table :data="testCases2" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="用例序号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="删除随记" name="third">
           <el-table :data="testCases3" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="用例序号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="评论随记" name="fourth">
           <el-table :data="testCases4" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="用例序号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="收藏随记" name="fifth">
           <el-table :data="testCases5" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="用例序号"></el-table-column>
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
    "caseNumber": "Unit_Note_NS_001_001",
    "caseDescription": "创建成功（overt为true）",
    "input": {
      "addNoteRequestBody": {
        "trackID": "123",
        "overt": true,
        "note": {
          "title": "上海旅行",
          "articleBody": "外滩一日游",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": "user000"
    },
    "expectedResult": "返回true，成功创建随记"
  },
  {
    "caseNumber": "Unit_Note_NS_001_002",
    "caseDescription": "trackID为空",
    "input": {
      "addNoteRequestBody": {
        "trackID": "",
        "overt": true,
        "note": {
          "title": "上海旅行",
          "articleBody": "外滩一日游",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈trackID为空"
  },
  {
    "caseNumber": "Unit_Note_NS_001_003",
    "caseDescription": "创建成功（overt为false）",
    "input": {
      "addNoteRequestBody": {
        "trackID": "123",
        "overt": false,
        "note": {
          "title": "上海旅行",
          "articleBody": "外滩一日游",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": "user000"
    },
    "expectedResult": "返回true，成功创建随记"
  },
  {
    "caseNumber": "Unit_Note_NS_001_004",
    "caseDescription": "title为空",
    "input": {
      "addNoteRequestBody": {
        "trackID": "123",
        "overt": false,
        "note": {
          "title": "",
          "articleBody": "外滩一日游",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈title为空"
  },
  {
    "caseNumber": "Unit_Note_NS_001_005",
    "caseDescription": "title超过10字符",
    "input": {
      "addNoteRequestBody": {
        "trackID": "123",
        "overt": false,
        "note": {
          "title": "人均8000元三天两晚上海旅行",
          "articleBody": "外滩一日游",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈title超过10字符"
  },
  {
    "caseNumber": "Unit_Note_NS_001_006",
    "caseDescription": "articleBody为空",
    "input": {
      "addNoteRequestBody": {
        "trackID": "123",
        "overt": false,
        "note": {
          "title": "上海旅行",
          "articleBody": "",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈articleBody为空"
  },
  {
    "caseNumber": "Unit_Note_NS_001_007",
    "caseDescription": "articleBody超过100字符",
    "input": {
      "addNoteRequestBody": {
        "trackID": "123",
        "overt": false,
        "note": {
          "title": "上海旅行",
          "articleBody": "这次的上海旅行真是令人难忘。我们参观了外滩、东方明珠塔和上海博物馆。外滩的夜景美得让人惊叹，东方明珠塔的高度让人感受到城市的现代化，而上海博物馆则展现了丰富的历史文化。整个旅程充满了惊喜和感动，是一次难得的经历。",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈articleBody超过100字符"
  },
  {
    "caseNumber": "Unit_Note_NS_001_008",
    "caseDescription": "userID为空",
    "input": {
      "addNoteRequestBody": {
        "trackID": "123",
        "overt": true,
        "note": {
          "title": "上海旅行",
          "articleBody": "外滩一日游",
          "noteID": "note000",
          "createTime": "20240603",
          "lastEditTime": "20240603"
        }
      },
      "userID": ""
    },
    "expectedResult": "返回false，反馈userID为空"
  }
];


const testCases2 = [
  {
    "caseNumber": "Unit_Note_NS_002_001",
    "caseDescription": "修改随记成功",
    "input": {
      "request": {
        "noteID": "note000",
        "title": "北京旅行",
        "articleBody": "故宫半日游"
      }
    },
    "expectedResult": "返回true，成功修改随记"
  },
  {
    "caseNumber": "Unit_Note_NS_002_002",
    "caseDescription": "noteID不存在",
    "input": {
      "request": {
        "noteID": "note001",
        "title": "北京旅行",
        "articleBody": "故宫半日游"
      }
    },
    "expectedResult": "返回false，反馈noteID不存在"
  },
  {
    "caseNumber": "Unit_Note_NS_002_003",
    "caseDescription": "noteID为空",
    "input": {
      "request": {
        "noteID": "",
        "title": "北京旅行",
        "articleBody": "故宫半日游"
      }
    },
    "expectedResult": "返回false，反馈noteID为空"
  },
  {
    "caseNumber": "Unit_Note_NS_002_004",
    "caseDescription": "title为空",
    "input": {
      "request": {
        "noteID": "note000",
        "title": "",
        "articleBody": "故宫半日游"
      }
    },
    "expectedResult": "返回false，反馈title为空"
  },
  {
    "caseNumber": "Unit_Note_NS_002_005",
    "caseDescription": "title超过10字符",
    "input": {
      "request": {
        "noteID": "note000",
        "title": "北京旅行四天三晚自驾出行穷游",
        "articleBody": "故宫半日游"
      }
    },
    "expectedResult": "返回false，反馈title超过10字符"
  },
  {
    "caseNumber": "Unit_Note_NS_002_006",
    "caseDescription": "articleBody为空",
    "input": {
      "request": {
        "noteID": "note000",
        "title": "北京旅行",
        "articleBody": ""
      }
    },
    "expectedResult": "返回false，反馈articleBody为空"
  },
  {
    "caseNumber": "Unit_Note_NS_002_007",
    "caseDescription": "articleBody超过100字符",
    "input": {
      "request": {
        "noteID": "note000",
        "title": "北京旅行",
        "articleBody": "北京，这座古老而现代的城市，拥有着丰富的历史文化和令人惊叹的建筑景观。在这次旅行中，我游览了长城、故宫、天安门等著名景点。每一处都让我深深地感受到了中国悠久的历史和文化底蕴。在长城上，我俯瞰着险峻的山峦，感受着历史的沉淀；在故宫里，我走过了紫禁城的每一个角落，仿佛穿越到了古代帝王的时代。而在现代化的CBD区域，高楼大厦林立，繁华喧嚣，展现着北京的现代魅力。这次旅行让我收获满满，我对北京这座城市充满了敬意和向往。"
      }
    },
    "expectedResult": "返回false，反馈articleBody超过100字符"
  }
];


const testCases3 = [
  {
    "caseNumber": "Unit_Note_NS_003_001",
    "caseDescription": "noteID存在，删除随记成功",
    "input": {
      "noteID": "note000"
    },
    "expectedResult": "返回true，成功删除随记"
  },
  {
    "caseNumber": "Unit_Note_NS_003_002",
    "caseDescription": "noteID不存在",
    "input": {
      "noteID": "note001"
    },
    "expectedResult": "返回false，反馈noteID不存在"
  },
  {
    "caseNumber": "Unit_Note_NS_003_003",
    "caseDescription": "noteID为空",
    "input": {
      "noteID": ""
    },
    "expectedResult": "返回false，反馈noteID为空"
  }
];

const testCases4 = [
  {
    "caseNumber": "Unit_Note_NS_004_001",
    "caseDescription": "评论随记成功",
    "input": {
      "comment": {
        "content": "我也想去",
        "noteID": "note000"
      },
      "userID": "user000"
    },
    "expectedResult": "返回true，成功创建评论"
  },
  {
    "caseNumber": "Unit_Note_NS_004_002",
    "caseDescription": "content为空",
    "input": {
      "comment": {
        "content": "",
        "noteID": "note000"
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈content为空"
  },
  {
    "caseNumber": "Unit_Note_NS_004_003",
    "caseDescription": "content超过50字符",
    "input": {
      "comment": {
        "content": "没想到还有这么漂亮的地方，我的女朋友一定会喜欢这里。这个暑假我可以带她一起来，到时候就参照这个旅游路线！",
        "noteID": "note000"
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈content超过50字符"
  },
  {
    "caseNumber": "Unit_Note_NS_004_004",
    "caseDescription": "noteID不存在",
    "input": {
      "comment": {
        "content": "我也想去",
        "noteID": "note001"
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈noteID不存在"
  },
  {
    "caseNumber": "Unit_Note_NS_004_005",
    "caseDescription": "noteID为空",
    "input": {
      "comment": {
        "content": "我也想去",
        "noteID": ""
      },
      "userID": "user000"
    },
    "expectedResult": "返回false，反馈noteID为空"
  },
  {
    "caseNumber": "Unit_Note_NS_004_006",
    "caseDescription": "userID为空",
    "input": {
      "comment": {
        "content": "我也想去",
        "noteID": "note000"
      },
      "userID": ""
    },
    "expectedResult": "返回false，反馈userID为空"
  }
];


const testCases5 = [
  {
    "caseNumber": "Unit_Note_NS_005_001",
    "caseDescription": "收藏随记成功",
    "input": {
      "noteId": "note000",
      "userId": "user000",
      "type": 1
    },
    "expectedResult": {
      "status": "1",
      "msg": "收藏成功"
    }
  },
  {
    "caseNumber": "Unit_Note_NS_005_002",
    "caseDescription": "随记不存在",
    "input": {
      "noteId": "note002",
      "userId": "user000",
      "type": 1
    },
    "expectedResult": {
      "status": "-1",
      "msg": "该随记不存在"
    }
  },
  {
    "caseNumber": "Unit_Note_NS_005_003",
    "caseDescription": "该随记已经被收藏",
    "input": {
      "noteId": "note001",
      "userId": "user000",
      "type": 1
    },
    "expectedResult": {
      "status": "-1",
      "msg": "已经收藏过该随记"
    }
  },
  {
    "caseNumber": "Unit_Note_NS_005_004",
    "caseDescription": "取消收藏成功",
    "input": {
      "noteId": "note001",
      "userId": "user000",
      "type": 0
    },
    "expectedResult": {
      "status": "0",
      "msg": "取消收藏成功"
    }
  },
  {
    "caseNumber": "Unit_Note_NS_005_005",
    "caseDescription": "随记不存在",
    "input": {
      "noteId": "note002",
      "userId": "user000",
      "type": 0
    },
    "expectedResult": {
      "status": "-1",
      "msg": "该随记不存在"
    }
  },
  {
    "caseNumber": "Unit_Note_NS_005_006",
    "caseDescription": "该随记未被收藏",
    "input": {
      "noteId": "note000",
      "userId": "user000",
      "type": 0
    },
    "expectedResult": {
      "status": "-1",
      "msg": "未收藏过该随记，无法取消收藏"
    }
  },
  {
    "caseNumber": "Unit_Note_NS_005_007",
    "caseDescription": "无效操作 - type参数错误",
    "input": {
      "noteId": "note000",
      "userId": "user000",
      "type": 2
    },
    "expectedResult": {
      "status": "-1",
      "msg": "type参数错误"
    }
  },
  {
    "caseNumber": "Unit_Note_NS_005_008",
    "caseDescription": "无效操作 - type参数错误",
    "input": {
      "noteId": "note001",
      "userId": "user000",
      "type": -1
    },
    "expectedResult": {
      "status": "-1",
      "msg": "type参数错误"
    }
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