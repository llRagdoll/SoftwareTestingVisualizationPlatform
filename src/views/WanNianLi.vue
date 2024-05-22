<template>
  <el-row style="height:95vh">
    <el-col :span="15">
      <el-row style="height:30%">
        <div class="question-card">
          <p class="question-title">万年历问题</p>
          <p class="question-content">输入三个整数y,m,d，分别表示年、月、日，输出它的下一天日期。</p>
          <p class="question-content">其中，年份的取值范围在1900和2100之间。</p>
        </div>
      </el-row>
      <el-row>
        <div class="testcase-card">
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="边界值法" name="first">
              <el-table :data="testCases" style="width: 100%;" max-height="450">
                <el-table-column prop="id" label="用例编号" width="150"></el-table-column>
                <el-table-column prop="a" label="年" width="100"></el-table-column>
                <el-table-column prop="b" label="月" width="100"></el-table-column>
                <el-table-column prop="c" label="日" width="100"></el-table-column>
                <el-table-column prop="expectedOutput" label="预期输出"></el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane label="等价类法" name="second">
              <el-table :data="testCases2" style="width: 100%;" max-height="450">
                <el-table-column prop="id" label="用例编号" width="150"></el-table-column>
                <el-table-column prop="a" label="年" width="100"></el-table-column>
                <el-table-column prop="b" label="月" width="100"></el-table-column>
                <el-table-column prop="c" label="日" width="100"></el-table-column>
                <el-table-column prop="expectedOutput" label="预期输出"></el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane label="决策表法" name="third">
              <el-table :data="testCases2" style="width: 100%;" max-height="450">
                <el-table-column prop="id" label="用例编号" width="150"></el-table-column>
                <el-table-column prop="a" label="年" width="100"></el-table-column>
                <el-table-column prop="b" label="月" width="100"></el-table-column>
                <el-table-column prop="c" label="日" width="100"></el-table-column>
                <el-table-column prop="expectedOutput" label="预期输出"></el-table-column>
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
          <el-select v-model="value" placeholder="请选择设计方法" style="width: 80%;margin-bottom:20px">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
            <el-input v-model="caseid" placeholder="请输入测试用例编号" style="width:80%"></el-input>
            <p>a：{{ testCase.a }}</p>
            <p>b：{{ testCase.b }}</p>
            <p>c：{{ testCase.c }}</p>
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
import { ref, watch } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';

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


const activeName = ref('first')
const testCases = [
  { id: 'TC-RL-001', a: 1989, b: 6, c: 15, expectedOutput: '年份不在取值范围内' },
  { id: 'TC-RL-002', a: 1900, b: 6, c: 15, expectedOutput: '1900-6-16' },
  { id: 'TC-RL-003', a: 1901, b: 6, c: 15, expectedOutput: '1901-6-16' },
  { id: 'TC-RL-004', a: 2002, b: 6, c: 15, expectedOutput: '2002-6-16' },
  { id: 'TC-RL-005', a: 2099, b: 6, c: 15, expectedOutput: '2099-6-16' },
  { id: 'TC-RL-006', a: 2100, b: 6, c: 15, expectedOutput: '2100-6-16' },
  { id: 'TC-RL-007', a: 2101, b: 6, c: 15, expectedOutput: '年份不在取值范围内' },
  { id: 'TC-RL-008', a: 2002, b: 0, c: 15, expectedOutput: '月份不在取值范围内' },
  { id: 'TC-RL-009', a: 2002, b: 1, c: 15, expectedOutput: '2002-1-16' },
  { id: 'TC-RL-010', a: 2002, b: 2, c: 15, expectedOutput: '2002-2-16' },
  { id: 'TC-RL-011', a: 2002, b: 11, c: 15, expectedOutput: '2002-11-16' },
  { id: 'TC-RL-012', a: 2002, b: 12, c: 15, expectedOutput: '2002-12-16' },
  { id: 'TC-RL-013', a: 2002, b: 13, c: 15, expectedOutput: '月份不在取值范围内' },
  { id: 'TC-RL-014', a: 2002, b: 6, c: 0, expectedOutput: '日期不在取值范围内' },
  { id: 'TC-RL-015', a: 2002, b: 6, c: 1, expectedOutput: '2002-6-2' },
  { id: 'TC-RL-016', a: 2002, b: 6, c: 2, expectedOutput: '2002-6-3' },
  { id: 'TC-RL-017', a: 2000, b: 2, c: 28, expectedOutput: '2000-2-29' },
  { id: 'TC-RL-018', a: 2000, b: 2, c: 29, expectedOutput: '2000-3-1' },
  { id: 'TC-RL-019', a: 2000, b: 2, c: 30, expectedOutput: '日期不在取值范围内' },
  { id: 'TC-RL-020', a: 2002, b: 2, c: 27, expectedOutput: '2002-2-28' },
  { id: 'TC-RL-021', a: 2002, b: 2, c: 28, expectedOutput: '2002-3-1' },
  { id: 'TC-RL-022', a: 2002, b: 2, c: 29, expectedOutput: '日期不在取值范围内' },
  { id: 'TC-RL-023', a: 2002, b: 6, c: 29, expectedOutput: '2002-6-30' },
  { id: 'TC-RL-024', a: 2002, b: 6, c: 30, expectedOutput: '2002-7-1' },
  { id: 'TC-RL-025', a: 2002, b: 6, c: 31, expectedOutput: '日期不在取值范围内' },
  { id: 'TC-RL-026', a: 2002, b: 7, c: 30, expectedOutput: '2002-7-31' },
  { id: 'TC-RL-027', a: 2002, b: 7, c: 31, expectedOutput: '2002-8-1' },
  { id: 'TC-RL-028', a: 2002, b: 7, c: 32, expectedOutput: '日期不在取值范围内' },
  { id: 'TC-RL-029', a: 2002, b: 12, c: 31, expectedOutput: '2003-1-1' },
  { id: 'TC-RL-030', a: 2100, b: 12, c: 31, expectedOutput: '2101-1-1' }
];

    
const testCases2 = [
  { id: 'TC-RL-001', a: 2002, b: 1, c: 1, expectedOutput: '2002-1-2' },
  { id: 'TC-RL-002', a: 2002, b: 1, c: 31, expectedOutput: '2002-2-1' },
  { id: 'TC-RL-003', a: 2002, b: 4, c: 1, expectedOutput: '2002-4-2' },
  { id: 'TC-RL-004', a: 2002, b: 4, c: 30, expectedOutput: '2002-5-1' },
  { id: 'TC-RL-005', a: 2002, b: 4, c: 31, expectedOutput: '非法日期' },
  { id: 'TC-RL-006', a: 2002, b: 12, c: 30, expectedOutput: '2002-12-31' },
  { id: 'TC-RL-007', a: 2002, b: 12, c: 31, expectedOutput: '2003-1-1' },
  { id: 'TC-RL-008', a: 2002, b: 2, c: 27, expectedOutput: '2002-2-28' },
  { id: 'TC-RL-009', a: 2002, b: 2, c: 28, expectedOutput: '2002-3-1' },
  { id: 'TC-RL-010', a: 2002, b: 2, c: 29, expectedOutput: '非法日期' },
  { id: 'TC-RL-011', a: 2000, b: 2, c: 28, expectedOutput: '2000-2-29' },
  { id: 'TC-RL-012', a: 2000, b: 2, c: 29, expectedOutput: '2000-3-1' },
  { id: 'TC-RL-013', a: 2000, b: 2, c: 30, expectedOutput: '非法日期' }
];

const testCases3 = [
  { id: 'TC-RL-001', a: 2002, b: 1, c: 1, expectedOutput: '2002-1-2' },
  { id: 'TC-RL-002', a: 2002, b: 1, c: 31, expectedOutput: '2002-2-1' },
  { id: 'TC-RL-003', a: 2002, b: 4, c: 1, expectedOutput: '2002-4-2' },
  { id: 'TC-RL-004', a: 2002, b: 4, c: 30, expectedOutput: '2002-5-1' },
  { id: 'TC-RL-005', a: 2002, b: 4, c: 31, expectedOutput: '非法日期' },
  { id: 'TC-RL-006', a: 2002, b: 12, c: 30, expectedOutput: '2002-12-31' },
  { id: 'TC-RL-007', a: 2002, b: 12, c: 31, expectedOutput: '2003-1-1' },
  { id: 'TC-RL-008', a: 2002, b: 2, c: 27, expectedOutput: '2002-2-28' },
  { id: 'TC-RL-009', a: 2002, b: 2, c: 28, expectedOutput: '2002-3-1' },
  { id: 'TC-RL-010', a: 2002, b: 2, c: 29, expectedOutput: '非法日期' },
  { id: 'TC-RL-011', a: 2000, b: 2, c: 28, expectedOutput: '2000-2-29' },
  { id: 'TC-RL-012', a: 2000, b: 2, c: 29, expectedOutput: '2000-3-1' },
  { id: 'TC-RL-013', a: 2000, b: 2, c: 30, expectedOutput: '非法日期' }
];

const options = [
    {
      value: 'boundary',
      label: '边界值法'
    },
    {
      value: 'equivalence',
      label: '等价类法'
    },
    {
      value: 'decision',
      label: '决策表法'
    }
  ];
  
const value = ref('边界值法');
const caseid= ref('TC-RL-001');
const testCase = ref({ a: 1989, b: 6, c: 15 });
const result = ref('')
const notFound=ref(false)

watch(caseid, (newVal) => {
  let foundTestCase = null;
  if (activeName.value === 'first') {
    foundTestCase = testCases.find(testCase => testCase.id === newVal);
  } else if (activeName.value === 'second') {
    foundTestCase = testCases2.find(testCase => testCase.id === newVal);
  }else if (activeName.value === 'third') {
    foundTestCase = testCases3.find(testCase => testCase.id === newVal);
  }

  if (foundTestCase) {
    testCase.value = foundTestCase;
    notFound.value=false;
  } else {
    notFound.value=true;
  }
});
const runTest = () => {
  if (notFound.value) {
    ElMessage.error('请输入正确的测试用例！');
    return;
  }
  axios.get('http://localhost:9092/api/calendar', {
    params: {
      a: testCase.value.a,
      b: testCase.value.b,
      c: testCase.value.c
    }
  })
  .then(response => {
    console.log(response.data);
    result.value = response.data.result;
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