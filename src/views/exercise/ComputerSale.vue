<template>
    <el-row style="height:95vh">
        <el-col :span="15">
            <el-row style="height:30%">
                <div class="question-card">
                    <p class="question-title">电脑销售系统</p>
                    <p class="question-content">主机（25￥单位价格，每月最多销售的数量为70），显示器（30￥单位价格，每月最多销售数量为80），外设（45￥单位价格，每月最多销售的数量为90）；每个销售员每月至少销售一台完整的机器，当系统的主机这个变量接受到-1值的时候，系统自动统计该销售员本月的销售总额。当销售额小于等于1000（包括1000）按照10%提佣金，当销售额在1000-1800之间（包括1800）的时候按照15%提佣金，当销售额大于1800时按照20%提佣金。</p>
           
                </div>
            </el-row>
            <el-row>
                <div class="testcase-card">
                    <el-tabs v-model="activeName"  @tab-click="handleClick">
                      <el-tab-pane label="边界值法" name="first">
                        <el-table :data="testCases" style="width: 100%;" max-height="450">
                          <el-table-column prop="id" label="用例编号" width="150"></el-table-column>
                          <el-table-column prop="a" label="主机数量" width="100"></el-table-column>
                          <el-table-column prop="b" label="显示器数量" width="100"></el-table-column>
                          <el-table-column prop="c" label="外设数量" width="100"></el-table-column>
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
                    <p>销售金额：{{ result[0] }}</p>
                    <p>佣金：{{ result[1] }}</p>
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

const testCases = [
  { id: 'TC-CS-001', a: 1, b: 1, c: 1, expectedOutput: '销售金额：100，佣金：10' },
  { id: 'TC-CS-002', a: 2, b: 1, c: 1, expectedOutput: '销售金额：120，佣金：12.5' },
  { id: 'TC-CS-003', a: 5, b: 5, c: 5, expectedOutput: '销售金额：500，佣金：50' },
  { id: 'TC-CS-004', a: 36, b: 1, c: 1, expectedOutput: '销售总额：975，佣金：97.5' },
  { id: 'TC-CS-005', a: 10, b: 10, c: 10, expectedOutput: '销售总额：1000，佣金：100' },
  { id: 'TC-CS-006', a: 38, b: 1, c: 1, expectedOutput: '销售总额：1025，佣金：153.75' },
  { id: 'TC-CS-007', a: 14, b: 14, c: 14, expectedOutput: '销售总额：1400，佣金：210' },
  { id: 'TC-CS-008', a: 1, b: 57, c: 1, expectedOutput: '销售总额：1780，佣金：267' },
  { id: 'TC-CS-009', a: 18, b: 18, c: 18, expectedOutput: '销售总额：1800，佣金：270' },
  { id: 'TC-CS-010', a: 1, b: 58, c: 1, expectedOutput: '销售总额：1810，佣金：362' },
  { id: 'TC-CS-011', a: 50, b: 50, c: 50, expectedOutput: '销售总额：5000，佣金：1000' },
  { id: 'TC-CS-012', a: 69, b: 80, c: 90, expectedOutput: '销售金额：8175，佣金：1635' },
  { id: 'TC-CS-013', a: 70, b: 80, c: 90, expectedOutput: '销售金额：8200，佣金：1640' },
  { id: 'TC-CS-014', a: 71, b: 80, c: 90, expectedOutput: '错误提示信息："主机的销售数量不在取值范围内（1-70）"' },
  { id: 'TC-CS-015', a: 70, b: 81, c: 90, expectedOutput: '错误提示信息："显示器的销售数量不在取值范围内（1-80）"' },
  { id: 'TC-CS-016', a: 70, b: 80, c: 91, expectedOutput: '错误提示信息："外设的销售数量不在取值范围内（1-90）"' },
  { id: 'TC-CS-017', a: 0, b: 1, c: 1, expectedOutput: '错误提示信息："主机的销售数量不在取值范围内（1-70）"' },
  { id: 'TC-CS-018', a: 1, b: 0, c: 1, expectedOutput: '错误提示信息："显示器的销售数量不在取值范围内（1-80）"' },
  { id: 'TC-CS-019', a: 1, b: 1, c: 0, expectedOutput: '错误提示信息："外设的销售数量不在取值范围内（1-90）"' },
  { id: 'TC-CS-020', a: -1, b: 1, c: 1, expectedOutput: '统计该销售员本月的销售总额' }
];


  

const activeName = ref('first')
 
const options = [
    {
      value: 'boundary',
      label: '边界值法'
    },
  ];
const value = ref('边界值法');
const caseid= ref('TC-CS-001');
const testCase = ref({ a: 1, b: 1, c: 1 });
const result = ref('')
const notFound=ref(false)

watch(caseid, (newVal) => {
  let foundTestCase = null;
  if (activeName.value === 'first') {
    foundTestCase = testCases.find(testCase => testCase.id === newVal);
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
  axios.get('http://localhost:9092/api/computer', {
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
    padding:10px
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