<template>
  <el-row style="height:95vh">
    <el-col :span="15">
      <el-row>
        <div class="telecom-question-card">
          <p class="question-title">电信收费问题</p>
          <p class="question-content">A. 每月的电话总费用=基本月租费+折扣后的实际的通话费，如果没有折扣则按实际通话费计算，基本月租费为25元，每分钟通话费为0.15元。
            B. 实际通话费是否有折扣与当月的通话时间（分钟）和本年度至本月的累计未按时缴费的次数有关。
            C. 当月的通话分钟数和折扣比例及本年度未按时缴费次数之间有直接的对应关系，如果本年度的未按时缴费的次数超过本月通话时间所对应的容许值则免于折扣，并按实际的通话费计算。
            D. 通话时间和折扣比例及未按时缴费次数的关系详见题目</p>
          <!-- <el-table :data="discountData" style="width: 100%;" max-height="120">
            <el-table-column prop="time" label="本月通话的分钟数" width="240"></el-table-column>
            <el-table-column prop="count" label="通话时间段的最大容许不按时缴费次数" width="320"></el-table-column>
            <el-table-column prop="discount" label="通话时间段的折扣率"></el-table-column>
          </el-table> -->
          <!-- <div class="discount-list">
            <div class="discount-item" v-for="item in discountData" :key="item.time">
              <div class="discount-time">本月通话的分钟数: {{ item.time }}</div>
              <div class="discount-count">通话时间段的最大容许不按时缴费次数: {{ item.count }}</div>
              <div class="discount-rate">通话时间段的折扣率: {{ item.discount }}</div>
            </div>
          </div> -->
        </div>
      </el-row>
      <el-row>
        <div class="telecom-testcase-card">
          <el-tabs v-model="activeName"  @tab-click="handleClick">
            <el-tab-pane label="最优测试用例集" name="first">
              <el-table :data="testCases" style="width: 100%;" max-height="400">
                <el-table-column prop="id" label="用例编号" width="200"></el-table-column>
                <el-table-column prop="time" label="通话时间（分钟）" width="160"></el-table-column>
                <el-table-column prop="count" label="未按时缴费次数" width="160"></el-table-column>
                <el-table-column prop="expectedDiscount" label="预期输出（折扣率％）"></el-table-column>
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
          <p>通话时间（分钟）：{{ testCase.time }}</p>
          <p>未按时缴费次数：{{ testCase.count }}</p>
          <el-button type="warning" plain class="run-button"  style="width:80%" @click="runTest">运行</el-button>
        </div>
        <div class="chart-area">
          <div v-show="chartType === 'bar'" id="barChart" class="chart-container" ref="barChartRef" style="width:100%;height:35vh;"></div>
          <div v-show="chartType === 'pie'" id="pieChart" class="chart-container" ref="pieChartRef" style="width:100%;height:35vh;"></div>
          <p>折扣率％：{{ result }}</p>
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


// const discountData = [
//   {
//     time: '0＜通话时间≤60',
//     count: '1',
//     discount: '1.0％',
//   },
//   {
//     time: '60＜通话时间≤120',
//     count: '2',
//     discount: '1.5％',
//   },
//   {
//     time: '120＜通话时间≤180',
//     count: '3',
//     discount: '2.0％',
//   },
//   {
//     time: '180＜通话时间≤300 ',
//     count: '3',
//     discount: '2.5％',
//   },
//   {
//     time: '300＜通话时间',
//     count: '6',
//     discount: '3.0％',
//   }
// ];

const testCases = [
  { id: 'TC-TC-001', time: 1, count: 0, expectedDiscount: 1.0 },
  { id: 'TC-TC-002', time: 60, count: 1, expectedDiscount: 1.0 },
  { id: 'TC-TC-003', time: 60, count: 2, expectedDiscount: 0 },
  { id: 'TC-TC-004', time: 61, count: 1, expectedDiscount: 1.5 },
  { id: 'TC-TC-005', time: 61, count: 2, expectedDiscount: 1.5 },
  { id: 'TC-TC-006', time: 61, count: 3, expectedDiscount: 0 },
  { id: 'TC-TC-007', time: 120, count: 2, expectedDiscount: 1.5 },
  { id: 'TC-TC-008', time: 120, count: 3, expectedDiscount: 0 },
  { id: 'TC-TC-009', time: 121, count: 2, expectedDiscount: 2.0 },
  { id: 'TC-TC-010', time: 121, count: 3, expectedDiscount: 2.0 },
  { id: 'TC-TC-011', time: 121, count: 4, expectedDiscount: 0 },
  { id: 'TC-TC-012', time: 180, count: 3, expectedDiscount: 2.0 },
  { id: 'TC-TC-013', time: 180, count: 4, expectedDiscount: 0 },
  { id: 'TC-TC-014', time: 181, count: 3, expectedDiscount: 2.5 },
  { id: 'TC-TC-015', time: 181, count: 4, expectedDiscount: 2.5 },
  { id: 'TC-TC-016', time: 181, count: 5, expectedDiscount: 0 },
  { id: 'TC-TC-017', time: 300, count: 3, expectedDiscount: 2.5 },
  { id: 'TC-TC-018', time: 300, count: 4, expectedDiscount: 2.5 },
  { id: 'TC-TC-019', time: 300, count: 7, expectedDiscount: 0 },
  { id: 'TC-TC-020', time: 301, count: 6, expectedDiscount: 3.0 },
  { id: 'TC-TC-021', time: 301, count: 7, expectedDiscount: 0 },
];




const activeName = ref('first')

const options = [
  {
    value: 'best',
    label: '最优测试用例集'
  },
];
const value = ref('最优测试用例集');
const caseid= ref('TC-TC-001');
const testCase = ref({ time: 1, count: 0 });
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
  axios.get('http://localhost:9092/api/telecom', {
    params: {
      time: testCase.value.time,
      count: testCase.value.count
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
.telecom-question-card{
  width: 100%;
  height: 24vh;
  background-color: #53B5B2;
  border-radius: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding:0 20px
}

.question-title{
  font-size: 20px;
  color: #ffffff;
}

.question-content{
  color: #ffffff;
  font-size: 14px;
}

.telecom-testcase-card{
  margin-top: 20px;
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

.discount-list {
  padding: 20px;
  border-radius: 10px;
  margin-top: 20px;
}

.discount-item {
  padding: 15px;
  border-bottom: 1px solid #e0e0e0;
}

.discount-item:last-child {
  border-bottom: none;
}

.discount-time, .discount-count, .discount-rate {
  margin: 5px 0;
  font-size: 16px;
  color: #333;
}

</style>
