<template>
    <el-row style="height:95vh">
        <el-col :span="15">
            <el-row style="height:30%">
                <div class="question-card">
                    <p class="question-title">判断三角形</p>
                    <p class="question-content">输入三个数a,b,c,作为三角形三条边，输出三条边构成的三角形类型：</p>
                    <p class="question-content">普通三角形，等边三角形，等腰三角形或不构成三角形。</p>
                    <p class="question-content">其中，三条边都不超过1000.</p>
                </div>
            </el-row>
            <el-row>
                <div class="testcase-card">
                    <el-tabs v-model="activeName"  @tab-click="handleClick">
                        <el-tab-pane label="边界值法" name="first">
                          <el-table :data="testCases" style="width: 100%;" max-height="450">
                            <el-table-column prop="id" label="用例编号" width="150"></el-table-column>
                            <el-table-column prop="a" label="a" width="100"></el-table-column>
                            <el-table-column prop="b" label="b" width="100"></el-table-column>
                            <el-table-column prop="c" label="c" width="100"></el-table-column>
                            <el-table-column prop="expectedOutput" label="预期输出"></el-table-column>
                          </el-table>
                        </el-tab-pane>
                        <el-tab-pane label="等价类法" name="second">
                          <el-table :data="testCases2" style="width: 100%;" max-height="450">
                            <el-table-column prop="id" label="用例编号" width="150"></el-table-column>
                            <el-table-column prop="a" label="a" width="100"></el-table-column>
                            <el-table-column prop="b" label="b" width="100"></el-table-column>
                            <el-table-column prop="c" label="c" width="100"></el-table-column>
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
                    <el-button type="warning" plain class="run-button"  style="width:80%" @click="runTest">运行</el-button>
                </div>
                <div class="chart-area">
                    <div v-show="chartType === 'bar'" id="barChart" class="chart-container" ref="barChartRef" style="width:100%;height:35vh;"></div>
                    <div v-show="chartType === 'pie'" id="pieChart" class="chart-container" ref="pieChartRef" style="width:100%;height:35vh;"></div>
                    <p>{{ result }}</p>
                    <p>{{ result[0] }}</p>
                </div>
            </div>
        </el-col>
    </el-row>
</template>

<script setup>
//import * as echarts from 'echarts';
import { ref ,watch} from 'vue';
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
//     title: {
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
//             return {
//                 value: value,
//                 itemStyle: {
//                     color: index === 0 ? '#D8E5F9' : (index === 1 ? '#F2DABD' : '#DFF3DF') // 浅蓝, 浅橙, 浅绿
//                 }
//             };
//         })
//   }]
// });

// const getPieOption = () => ({
//     title: {
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
//                 let color;
//                 switch (name) {
//                     case '待办任务':
//                         color = '#D8E5F9'; // 浅蓝
//                         break;
//                     case '进行中':
//                         color = '#F2DABD'; // 浅橙
//                         break;
//                     case '已完成':
//                         color = '#DFF3DF'; // 浅绿
//                         break;
//                     default:
//                         color = '#D3D3D3';
//                 }
//                 return { 
//                     name: name, 
//                     value: value,
//                     itemStyle: {
//                         color: color
//                     }
//                 };
//             }),
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

// onMounted(() => {
//   initChart(chartType.value);
// });
const   testCases= [
        { id: 'TC-SJX-001', a: 0, b: 500, c: 500, expectedOutput: 'a不在取值范围内' },
        { id: 'TC-SJX-002', a: 1, b: 500, c: 500, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-003', a: 2, b: 500, c: 500, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-004', a: 500, b: 500, c: 500, expectedOutput: '等边三角形' },
        { id: 'TC-SJX-005', a: 999, b: 500, c: 500, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-006', a: 1000, b: 500, c: 500, expectedOutput: '不构成三角形' },
        { id: 'TC-SJX-007', a: 1001, b: 500, c: 500, expectedOutput: 'a不在取值范围内' },
        { id: 'TC-SJX-008', a: 500, b: 0, c: 500, expectedOutput: 'b不在取值范围内' },
        { id: 'TC-SJX-009', a: 500, b: 1, c: 500, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-010', a: 500, b: 2, c: 500, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-011', a: 500, b: 999, c: 500, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-012', a: 500, b: 1000, c: 500, expectedOutput: '不构成三角形' },
        { id: 'TC-SJX-013', a: 500, b: 1001, c: 500, expectedOutput: 'b不在取值范围内' },
        { id: 'TC-SJX-014', a: 500, b: 500, c: 0, expectedOutput: 'c不在取值范围内' },
        { id: 'TC-SJX-015', a: 500, b: 500, c: 1, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-016', a: 500, b: 500, c: 2, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-017', a: 500, b: 500, c: 999, expectedOutput: '等腰三角形' },
        { id: 'TC-SJX-018', a: 500, b: 500, c: 1000, expectedOutput: '不构成三角形' },
        { id: 'TC-SJX-019', a: 500, b: 500, c: 1001, expectedOutput: 'c不在取值范围内' },
      ]
    
const testCases2 = [
  { id: 'TC-SJX-001', a: 6, b: 6, c: 6, expectedOutput: '等边三角形' },
  { id: 'TC-SJX-002', a: 3, b: 3, c: 4, expectedOutput: '等腰三角形' },
  { id: 'TC-SJX-003', a: 3, b: 4, c: 5, expectedOutput: '普通三角形' },
  { id: 'TC-SJX-004', a: 10, b: 5, c: 5, expectedOutput: '不构成三角形' },
  { id: 'TC-SJX-005', a: -1, b: 5, c: 5, expectedOutput: 'a取值不在范围内' },
  { id: 'TC-SJX-006', a: 1001, b: 5, c: 5, expectedOutput: 'a取值不在范围内' },
  { id: 'TC-SJX-007', a: 0, b: 5, c: 5, expectedOutput: 'a不能为0' },
  { id: 'TC-SJX-008', a: 5, b: -1, c: 5, expectedOutput: 'b取值不在范围内' },
  { id: 'TC-SJX-009', a: 5, b: 1001, c: 5, expectedOutput: 'b取值不在范围内' },
  { id: 'TC-SJX-010', a: 5, b: 0, c: 5, expectedOutput: 'b不能为0' },
  { id: 'TC-SJX-011', a: 5, b: 5, c: -1, expectedOutput: 'c取值不在范围内' },
  { id: 'TC-SJX-012', a: 5, b: 5, c: 1001, expectedOutput: 'c取值不在范围内' },
  { id: 'TC-SJX-013', a: 5, b: 5, c: 0, expectedOutput: 'c不能为0' }
];

const options = [
    {
      value: 'boundary',
      label: '边界值法'
    },
    {
      value: 'equivalence',
      label: '等价类法'
    }
  ];
  
const value = ref('边界值法');
const caseid= ref('TC-SJX-001');
const testCase = ref({ a: 0, b: 500, c: 500 });
const activeName = ref('first')
const result = ref('')
const notFound=ref(false)

watch(caseid, (newVal) => {
  let foundTestCase = null;
  if (activeName.value === 'first') {
    foundTestCase = testCases.find(testCase => testCase.id === newVal);
  } else if (activeName.value === 'second') {
    foundTestCase = testCases2.find(testCase => testCase.id === newVal);
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
  axios.get('http://localhost:9092/api/triangle', {
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
.question-card{
    width: 100%;
    height: 24vh;
    background-color: #53B5B2;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding:10px
}

.question-title{
    font-size: 20px;
    color: #ffffff;
}

.question-content{
    color: #ffffff;
    font-size: 14px;
}

.testcase-card{
    width: 100%;
    height: 65vh;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding:20px
}

.run-chart{
    width: 90%;
    height: 93.5vh;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-left:5%;
    padding:10px
}

.input-area{
    height:50%
}

.chart-area{
    height:50%
}

.run-button{
    width:90%;
    
}
</style>