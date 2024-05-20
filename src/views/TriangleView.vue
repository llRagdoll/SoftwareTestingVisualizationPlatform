<template>
    <el-row style="height:95vh">
        <el-col :span="15">
            <el-row style="height:30%">
                <div class="question-card">
                    <p class="question-title">判断三角形</p>
                    <p class="question-content">输入三个整数a,b,c,作为三角形三条边，输出三条边构成的三角形类型：</p>
                    <p class="question-content">普通三角形，等边三角形，等腰三角形或不构成三角形。</p>
                    <p class="question-content">其中，三条边都不超过1000.</p>
                </div>
            </el-row>
            <el-row>
                <div class="testcase-card">
                    <el-tabs v-model="activeName"  @tab-click="handleClick">
                        <el-tab-pane label="边界值法" name="first">
                            <el-table :data="tableData" height="250" style="width: 100%">
                                <el-table-column prop="date" label="Date" width="180" />
                                <el-table-column prop="name" label="Name" width="180" />
                                <el-table-column prop="address" label="Address" />
                            </el-table>
                        </el-tab-pane>
                        <el-tab-pane label="等价类法" name="second">
                            <el-table :data="tableData" height="250" style="width: 100%">
                                <el-table-column prop="date" label="Date" width="180" />
                                <el-table-column prop="name" label="Name" width="180" />
                                <el-table-column prop="address" label="Address" />
                            </el-table>
                        </el-tab-pane>
                        <el-tab-pane label="决策表法" name="third">
                            <el-table :data="tableData" height="250" style="width: 100%">
                                <el-table-column prop="date" label="Date" width="180" />
                                <el-table-column prop="name" label="Name" width="180" />
                                <el-table-column prop="address" label="Address" />
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
                    <el-input placeholder="请输入测试用例编号" style="width:80%"></el-input>
                    <p>a：12</p>
                    <p>b：12</p>
                    <p>c：12</p>
                    <el-button type="warning" plain class="run-button"  style="width:80%">运行</el-button>
                </div>
                <div class="chart-area">
                    <div v-show="chartType === 'bar'" id="barChart" class="chart-container" ref="barChartRef" style="width:100%;height:35vh;"></div>
                    <div v-show="chartType === 'pie'" id="pieChart" class="chart-container" ref="pieChartRef" style="width:100%;height:35vh;"></div>
                </div>
            </div>
        </el-col>
    </el-row>
</template>

<script setup>
import * as echarts from 'echarts';
import { ref ,onMounted} from 'vue';

const chartType = ref('bar');
const noData = ref(false); 
const commonData = {
  '待办': 3,
  '进行中': 4,
  '已完成': 2,
};

const barChartRef = ref(null);
const pieChartRef = ref(null);

const getBarOption = () => ({
    title: {
    text: '',
    left: 'center'
  },
  tooltip: {},
  xAxis: {
    data: Object.keys(commonData)
  },
  yAxis: {},
  series: [{
    name: '数量',
    type: 'bar',
    data: Object.values(commonData).map((value, index) => {
            return {
                value: value,
                itemStyle: {
                    color: index === 0 ? '#D8E5F9' : (index === 1 ? '#F2DABD' : '#DFF3DF') // 浅蓝, 浅橙, 浅绿
                }
            };
        })
  }]
});

const getPieOption = () => ({
    title: {
    text: '',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  series: [
    {
      name: '任务统计',
      type: 'pie',
      radius: '55%',
      data: Object.entries(commonData).map(([name, value]) => {
                let color;
                switch (name) {
                    case '待办任务':
                        color = '#D8E5F9'; // 浅蓝
                        break;
                    case '进行中':
                        color = '#F2DABD'; // 浅橙
                        break;
                    case '已完成':
                        color = '#DFF3DF'; // 浅绿
                        break;
                    default:
                        color = '#D3D3D3';
                }
                return { 
                    name: name, 
                    value: value,
                    itemStyle: {
                        color: color
                    }
                };
            }),
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
});

const initChart = (type) => {
  // 确保图表数据存在
  if (Object.keys(commonData).length === 0) {
    noData.value = true;
    return;
  }
  noData.value = false;

  let chartDom;
  let option;

  if (type === 'bar' && barChartRef.value) {
    chartDom = barChartRef.value;
    option = getBarOption();
  } else if (type === 'pie' && pieChartRef.value) {
    chartDom = pieChartRef.value;
    option = getPieOption();
  } else {
    // 如果没有找到对应的 DOM 元素，直接返回
    return;
  }

  // 初始化 ECharts 图表
  if (chartDom) {
    const chartInstance = echarts.init(chartDom);
    chartInstance.setOption(option);
  }
};

onMounted(() => {
  initChart(chartType.value);
});
const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-08',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-06',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-07',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
]

const activeName = ref('first')
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