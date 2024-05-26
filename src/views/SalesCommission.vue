<template>
  <el-row style="height:95vh">
    <el-col :span="15">
      <el-row style="height:30%">
        <div class="question-card">
          <p class="question-title">销售问题</p>
          <p class="question-content">一销售系统，如果销售员的年销售额大于200万RMB且请假天数不超过10天的情况下，现金到帐大于等于60%，则佣金（提成）系数为7，即佣金值为销售额除以佣金系数；现金到帐小于60%，佣金不予计算。所有其他情况且现金到帐小于等于85%，则按佣金系数均为6计算佣金，现金到账大于85%，佣金系数按5处理。</p>
        </div>
      </el-row>
      <el-row>
        <div class="testcase-card">
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane
              v-for="option in options"
              :key="option.value"
              :label="option.label"
              :name="option.value"
            >
              <el-table :data="getTestCasesForMethod(option.value)" style="width: 100%;" max-height="450">
                <el-table-column prop="no" label="用例编号" width="130" ></el-table-column>
                <el-table-column prop="AS" label="销售额" width="130" align="center"></el-table-column>
                <el-table-column prop="LD" label="请假天数" width="130" align="center"></el-table-column>
                <el-table-column prop="CCR" label="现金到账率" width="160" align="center"></el-table-column>
                <el-table-column prop="expectedOutput" label="预期输出" align="center"></el-table-column>
              </el-table>
            </el-tab-pane>
          </el-tabs>
        </div>
      </el-row>
    </el-col>
    <el-col :span="9">
      <div class="run-chart">
        <div class="input-area">
          <p style="font-weight: bold;">测试输入</p>
          <el-select v-model="selectedMethod" placeholder="请选择设计方法" style="width: 80%;margin-bottom:20px">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
            <el-select v-model="selectedId" placeholder="请选择测试用例" style="width: 80%;margin-bottom:20px">
              <el-option
                v-for="item in filteredTestCases"
                :key="item.id"
                :label="item.no"
                :value="item.id"
              />
            </el-select>
            <p>年销售额：{{ TestCases[selectedId].AS }} 万元</p>
            <p>请假天数：{{ TestCases[selectedId].LD }} 天</p>
            <p>现金到账率：{{ TestCases[selectedId].CCR }}</p>
          <el-button type="warning" plain class="run-button" style="width:80%" @click="runTest">运行</el-button>
        </div>
        <div class="chart-area">
          <div v-show="chartType === 'bar'" id="barChart" class="chart-container" ref="barChartRef"
            style="width:100%;height:35vh;"></div>
          <div v-show="chartType === 'pie'" id="pieChart" class="chart-container" ref="pieChartRef"
            style="width:100%;height:35vh;"></div>
            <p>{{ result }}</p>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script setup>
//import * as echarts from 'echarts';
import {computed, ref} from 'vue';
import axios from 'axios';
// import { ElMessage } from 'element-plus';

// const chartType = ref('bar');
// const noData = ref(false);
// const commonData = {
//   '待办': 3,
//   '进行中': 4,
//   '已完成': 2,
// };

// const barChartRef = ref(null);
// const pieChartRef = ref(null);


// const getBarOption = () => ({
//   title: {
//     text: '',
//     left: 'center'
//   },
//   tooltip: {},
//   xAxis: {
//     data: Object.keys(commonData)
//   },
//   yAxis: {},
//   series: [{
//     name: '数量',
//     type: 'bar',
//     data: Object.values(commonData).map((value, index) => {
//       return {
//         value: value,
//         itemStyle: {
//           color: index === 0 ? '#D8E5F9' : (index === 1 ? '#F2DABD' : '#DFF3DF') // 浅蓝, 浅橙, 浅绿
//         }
//       };
//     })
//   }]
// });

// const getPieOption = () => ({
//   title: {
//     text: '',
//     left: 'center'
//   },
//   tooltip: {
//     trigger: 'item'
//   },
//   series: [
//     {
//       name: '任务统计',
//       type: 'pie',
//       radius: '55%',
//       data: Object.entries(commonData).map(([name, value]) => {
//         let color;
//         switch (name) {
//           case '待办任务':
//             color = '#D8E5F9'; // 浅蓝
//             break;
//           case '进行中':
//             color = '#F2DABD'; // 浅橙
//             break;
//           case '已完成':
//             color = '#DFF3DF'; // 浅绿
//             break;
//           default:
//             color = '#D3D3D3';
//         }
//         return {
//           name: name,
//           value: value,
//           itemStyle: {
//             color: color
//           }
//         };
//       }),
//       emphasis: {
//         itemStyle: {
//           shadowBlur: 10,
//           shadowOffsetX: 0,
//           shadowColor: 'rgba(0, 0, 0, 0.5)'
//         }
//       }
//     }
//   ]
// });

// const initChart = (type) => {
//   // 确保图表数据存在
//   if (Object.keys(commonData).length === 0) {
//     noData.value = true;
//     return;
//   }
//   noData.value = false;

//   let chartDom;
//   let option;

//   if (type === 'bar' && barChartRef.value) {
//     chartDom = barChartRef.value;
//     option = getBarOption();
//   } else if (type === 'pie' && pieChartRef.value) {
//     chartDom = pieChartRef.value;
//     option = getPieOption();
//   } else {
//     // 如果没有找到对应的 DOM 元素，直接返回
//     return;
//   }

//   // 初始化 ECharts 图表
//   if (chartDom) {
//     const chartInstance = echarts.init(chartDom);
//     chartInstance.setOption(option);
//   }
// };


const activeName = ref('statementTesting')
const TestCases = [
  { id: 0, no: 'case1', AS: -1, LD: -1, CCR: 2, expectedOutput: -1 },
  { id: 1, no: 'case2', AS: 201, LD: 10, CCR: 0.6, expectedOutput: 28.71 },
  { id: 2, no: 'case3', AS: 200, LD: 11, CCR: 0.85, expectedOutput: 33.33 },
  { id: 3, no: 'case4', AS: 0, LD: 0, CCR: 1, expectedOutput: 0 },
  { id: 4, no: 'case5', AS: 1000, LD: 0, CCR: 0.59, expectedOutput: 0 },
  { id: 5, no: 'case6', AS: 0, LD: 365, CCR: 1, expectedOutput: 0 },
  { id: 6, no: 'case7', AS: 201, LD: -1, CCR: -1, expectedOutput: -1 },
  { id: 7, no: 'case8', AS: -1, LD: 366, CCR: 2, expectedOutput: -1 },
  { id: 8, no: 'case9', AS: 201, LD: 11, CCR: 1, expectedOutput: 33.5 },
];

const options = [
    {value: 'statementTesting', label: '语句覆盖'},
    {value: 'decisionTesting', label: '判断覆盖'},
    {value: 'conditionTesting', label: '条件覆盖'},
    {value: 'conditionDeterminationTesting', label: '判定-条件覆盖'},
    {value: 'conditionCombinationTesting', label: '条件组合覆盖'},
  ];

const testCaseMapping = {
  statementTesting: [0, 1, 2, 3],
  decisionTesting: [0, 1, 2, 4, 5],
  conditionTesting: [6, 7],
  conditionDeterminationTesting: [1,4,2,8,6,7],
  conditionCombinationTesting: [0, 1, 2, 3, 4, 5, 6, 7, 8],
};

const selectedMethod = ref('statementTesting');
const selectedId= ref(0);
const result = ref('')

const filteredTestCases = computed(() => {
  return TestCases.filter(testCase => testCaseMapping[selectedMethod.value].includes(testCase.id));
});

const getTestCasesForMethod = (method) => {
  return TestCases.filter(testCase =>
    testCaseMapping[method].includes(testCase.id)
  );
};

// const selectedTestCase = computed(() => statementTestCases[selectedId.value]);
const runTest = () => {
  console.log("当前测试用例：",TestCases[selectedId.value])
  axios.get('http://localhost:9092/api/salesCommission', {
    params: {
      // AS: statementTestCases[selectedTestCase].AS,
      // LD: statementTestCases[selectedTestCase].LD,
      // CCR: statementTestCases[selectedTestCase].CCR
      AS: parseInt(TestCases[selectedId.value].AS),
      LD: parseInt(TestCases[selectedId.value].LD),
      CCR: parseFloat(TestCases[selectedId.value].CCR)
    }
  })
  .then(response => {
    console.log(response.data);
    result.value = response.data.result;
    if (result.value!='-1'){
      result.value=result.value+"万元";
    }
  })
  .catch(error => {
    console.error("请求出错：", error)
  });
};
</script>

<style>
.question-card {
  width: 100%;
  height: 24vh;
  background-color: #53B5B2;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 10px
}

.question-title {
  font-size: 20px;
  color: #ffffff;
  font-weight: bold
}

.question-content {
  color: #ffffff;
  font-size: 14px;
}

.testcase-card {
  width: 100%;
  height: 65vh;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 10px
}

.run-chart {
  width: 90%;
  height: 93.5vh;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-left: 5%;
  padding: 10px
}

.input-area {
  height: 50%
}

.chart-area {
  height: 50%
}

.run-button {
  width: 90%;

}
</style>