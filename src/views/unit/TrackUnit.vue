<template>
    <div v-if="!showReport">
    <el-card class="unit-card">
       <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
       <el-tab-pane label="创建地图" name="first">
           <el-table :data="testCases1" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="设置公开" name="second">
           <el-table :data="testCases2" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="创建地点" name="third">
           <el-table :data="testCases3" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="删除地点" name="fourth">
           <el-table :data="testCases4" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="创建路线" name="fifth">
           <el-table :data="testCases5" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="修改路线" name="sixth">
           <el-table :data="testCases6" border style="width: 100%" max-height="600">
               <el-table-column prop="caseNumber" label="测试项编号"></el-table-column>
               <el-table-column prop="caseDescription" label="用例描述"></el-table-column>
               <el-table-column prop="input" label="输入"></el-table-column>
               <el-table-column prop="expectedResult" label="期望结果"></el-table-column>
           </el-table>
       </el-tab-pane>
       <el-tab-pane label="删除路线" name="seventh">
           <el-table :data="testCases7" border style="width: 100%" max-height="600">
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
        <iframe src="http://localhost:12340" frameborder="0" style="width:100%;height:100vh"></iframe>
        </div>
</template>

<script setup>
import { ref } from 'vue'
// import axios from 'axios';

const showReport = ref(false)

const activeName = ref('first') 
const handleClick = (tab, event) => {
   console.log(tab, event)
}
const testCases1 = [
  { caseNumber: 'Unit_Track_MS_001_001', caseDescription: '成功创建地图', input: 'ownerid="user000000000000000001" ownername="user01" type=0', expectedResult: '成功创建个人地图' },
  { caseNumber: 'Unit_Track_MS_001_001', caseDescription: '成功创建地图', input: 'ownerid="group00000000000000001" ownername="group01" type=1', expectedResult: '成功创建小队地图' },
  { caseNumber: 'Unit_Track_MS_001_002', caseDescription: '创建地图时任意参数为空', input: 'ownerid="" ownername="user" type=0', expectedResult: '返回false，提示拥有人ID不能为空' },
  { caseNumber: 'Unit_Track_MS_001_002', caseDescription: '创建地图时任意参数为空', input: 'ownerid="group00000000000000001" ownername="" type=1', expectedResult: '返回false，提示拥有人名称不能为空' },
  { caseNumber: 'Unit_Track_MS_001_003', caseDescription: '创建地图时拥有人已经创建过地图', input: 'ownerid="user000000000000000000" ownername="user01" type=0', expectedResult: '返回false，提示拥有人已经创建过地图' },
  { caseNumber: 'Unit_Track_MS_001_004', caseDescription: '创建地图时type为规定外的其他类型', input: 'ownerid="user000000000000000001" ownername="user01" type=2', expectedResult: '返回false，提示地图类型无效' }
];


const testCases2 = [
  { caseNumber: 'Unit_Track_MS_002_001', caseDescription: '成功修改地图公开状态', input: 'groupid="" userid="user000000000000000001" type=0', expectedResult: '"status": 0, "isPublic": false' },
  { caseNumber: 'Unit_Track_MS_002_001', caseDescription: '成功修改地图公开状态', input: 'groupid="group00000000000000001" userid="user000000000000000001" type=1', expectedResult: '"status": 0, "isPublic": true' },
  { caseNumber: 'Unit_Track_MS_002_002', caseDescription: '修改地图状态时找不到拥有者对应地图', input: 'groupid="" userid="" type=0', expectedResult: '"status": -1, "isPublic": false 提示找不到对应地图' },
  { caseNumber: 'Unit_Track_MS_002_002', caseDescription: '修改地图状态时找不到拥有者对应地图', input: 'groupid="group000000000000000-1" userid="user000000000000000001" type=0', expectedResult: '"status": -1, "isPublic": false 提示找不到对应地图' },
  { caseNumber: 'Unit_Track_MS_002_002', caseDescription: '修改地图状态时找不到拥有者对应地图', input: 'groupid="" userid="user0000000000000000-1" type=1', expectedResult: '"status": -1, "isPublic": false 提示找不到对应地图' },
  { caseNumber: 'Unit_Track_MS_002_003', caseDescription: '修改地图状态时类型非法', input: 'groupid="group00000000000000001" userid="user000000000000000001" type=2', expectedResult: '"status": -1, "isPublic": false 提示修改类型无效' }
];


const testCases3 = [
  { caseNumber: 'Unit_Track_MS_001_001', caseDescription: '创建地点中任意参数为空', input: 'newPoints={"groupID": "", "points": []} userID="user000000000000000001" status=false num=0', expectedResult: '提示points为空' },
  { caseNumber: 'Unit_Track_MS_001_001', caseDescription: '创建地点中任意参数为空', input: 'newPoints={"groupID": "group00000000000000001", "points": [{"name": "", "address": "testAddress", "lat": 0, "lng": 0}]} userID="user000000000000000001" status=false num=0', expectedResult: '提示地点名为空' },
  { caseNumber: 'Unit_Track_MS_001_002', caseDescription: 'userid非空但不存在', input: 'newPoints={"groupID": "", "points": [{"name": "testPointName", "address": "testAddress", "lat": 0, "lng": 0}]} userID="user0000000000000000-1" status=false num=0', expectedResult: '提示用户不存在' },
  { caseNumber: 'Unit_Track_MS_001_003', caseDescription: 'newPoints中的groupid非空但不存在', input: 'newPoints={"groupID": "group000000000000000-1", "points": [{"name": "testPointName", "address": "testAddress", "lat": 0, "lng": 0}]} userID="user000000000000000001" status=false num=0', expectedResult: '提示小队不存在' },
  { caseNumber: 'Unit_Track_MS_001_004', caseDescription: '添加的地点经纬度非法', input: 'newPoints={"groupID": "", "points": [{"name": "testPointName", "address": "testAddress", "lat": -1, "lng": 0}]} userID="user000000000000000001" status=false num=0', expectedResult: '提示经纬度非法' },
  { caseNumber: 'Unit_Track_MS_001_004', caseDescription: '添加的地点经纬度非法', input: 'newPoints={"groupID": "group00000000000000001", "points": [{"name": "testPointName", "address": "", "lat": 0, "lng": -1}]} userID="user000000000000000001" status=false num=0', expectedResult: '提示经纬度非法' },
  { caseNumber: 'Unit_Track_MS_001_005', caseDescription: '所有参数合法，添加成功', input: 'newPoints={"groupID": "", "points": [{"name": "testPointName", "address": "testAddress", "lat": 0, "lng": 0}]} userID="user000000000000000001" status=true num=1', expectedResult: '' },
  { caseNumber: 'Unit_Track_MS_001_005', caseDescription: '所有参数合法，添加成功', input: 'newPoints={"groupID": "group00000000000000001", "points": [{"name": "testPointName", "address": "", "lat": 0, "lng": 0}]} userID="user000000000000000001" status=true num=1', expectedResult: '' }
];

const testCases4 = [
  { caseNumber: 'Unit_Track_MS_002_001', caseDescription: '删除地点中pointID为空', input: 'pointID=""', expectedResult: '返回false，提示点ID不能为空' },
  { caseNumber: 'Unit_Track_MS_002_002', caseDescription: '删除地点中pointID非空但不存在', input: 'pointID="point000000000000000-1"', expectedResult: '返回false，提示点ID不存在' },
  { caseNumber: 'Unit_Track_MS_002_003', caseDescription: '删除地点中pointID存在但在轨迹中', input: 'pointID="point00000000000000002"', expectedResult: '返回false，提示点在轨迹途径点列表中' },
  { caseNumber: 'Unit_Track_MS_002_004', caseDescription: 'pointID合法，删除成功', input: 'pointID="point00000000000000001"', expectedResult: '返回true，删除成功' }
];


const testCases5 = [
  { caseNumber: 'Unit_Track_TS_001_001', caseDescription: '创建路线中任意参数为空', input: '"userId":"", "trackName": "track1", "tag": [], "pointLists": [{"pointID": "point00000000000000001","segment": 0}], "groupID": ""', expectedResult: '返回false，trackID=""；提示用户ID为空' },
  { caseNumber: 'Unit_Track_TS_001_001', caseDescription: '创建路线中任意参数为空', input: '"userId":"user000000000000000001", "trackName": "", "tag": ["tag"], "pointLists": [{"pointID": "point00000000000000001","segment": 0}], "groupID": "group00000000000000001"', expectedResult: '返回false，trackID=""；提示路线名为空' },
  { caseNumber: 'Unit_Track_TS_001_001', caseDescription: '创建路线中任意参数为空', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": ["tag"], "pointLists": [], "groupID": ""', expectedResult: '返回false，trackID=""；提示途经点列表为空' },
  { caseNumber: 'Unit_Track_TS_001_001', caseDescription: '创建路线中任意参数为空', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": [], "pointLists": [{"pointID": "","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": "group00000000000000001"', expectedResult: '返回false，trackID=""；提示途经点中地点ID为空' },
  
  { caseNumber: 'Unit_Track_TS_001_002', caseDescription: 'trackname重复', input: '"userId":"user000000000000000001", "trackName": "track0", "tag": [], "pointLists": [{"pointID": "","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": "group00000000000000001"', expectedResult: '返回false，trackID=""；提示路线名重复' },
  
  { caseNumber: 'Unit_Track_TS_001_003', caseDescription: '参数超过规定区间', input: '"userId":"user000000000000000001", "trackName": "test-track1", "tag": ["tag"], "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": ""', expectedResult: '返回false，trackID=""；提示路线名超出规定长度' },
  { caseNumber: 'Unit_Track_TS_001_003', caseDescription: '参数超过规定区间', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": ["science"], "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": "group00000000000000001"', expectedResult: '返回false，trackID=""；提示标签超出规定长度' },
  { caseNumber: 'Unit_Track_TS_001_003', caseDescription: '参数超过规定区间', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": [], "pointLists": [{"pointID": "point00000000000000001","segment": -1}, {"pointID": "point00000000000000002","segment": 1}], "groupID": ""', expectedResult: '返回false，trackID=""；提示途经点顺序非法' },
  
  { caseNumber: 'Unit_Track_TS_001_004', caseDescription: '参数在数据库不存在', input: '"userId":"user0000000000000000-1", "trackName": "track1", "tag": [], "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": ""', expectedResult: '返回false，trackID=""；提示该用户无对应地图' },
  { caseNumber: 'Unit_Track_TS_001_004', caseDescription: '参数在数据库不存在', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": ["tag"], "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": "group000000000000000-1"', expectedResult: '返回false，trackID=""；提示该小队无对应地图' },
  { caseNumber: 'Unit_Track_TS_001_004', caseDescription: '参数在数据库不存在', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": [], "pointLists": [{"pointID": "point000000000000000-1","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": ""', expectedResult: '返回false，trackID=""；提示途经点不存在' },
  
  { caseNumber: 'Unit_Track_TS_001_005', caseDescription: '所有参数合法，创建成功', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": [], "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": ""', expectedResult: '返回true，及非空的trackID' },
  { caseNumber: 'Unit_Track_TS_001_005', caseDescription: '所有参数合法，创建成功', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": [""], "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "groupID": "group00000000000000001"', expectedResult: '返回true，及非空的trackID' },
  { caseNumber: 'Unit_Track_TS_001_005', caseDescription: '所有参数合法，创建成功', input: '"userId":"user000000000000000001", "trackName": "track1", "tag": ["tag"], "pointLists": [{"pointID": "point00000000000000001","segment": 0}], "groupID": ""', expectedResult: '返回true，及非空的trackID' }
];


const testCases6 = [
  { caseNumber: 'Unit_Track_TS_002_001', caseDescription: '修改路线中任意参数为空', input: '{"trackID": "", "pointLists": [{"pointID": "point00000000000000001","segment": 0}], "tag": [], "trackName": "track1"}', expectedResult: '返回false，提示路线ID为空' },
  { caseNumber: 'Unit_Track_TS_002_001', caseDescription: '修改路线中任意参数为空', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": 0}], "tag": ["tag"], "trackName": ""}', expectedResult: '返回false，提示路线名为空' },
  { caseNumber: 'Unit_Track_TS_002_001', caseDescription: '修改路线中任意参数为空', input: '{"trackID": "track00000000000000001", "pointLists": [], "tag": [], "trackName": "track1"}', expectedResult: '返回false，提示途经点列表为空' },
  { caseNumber: 'Unit_Track_TS_002_001', caseDescription: '修改路线中任意参数为空', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": ["tag"], "trackName": "track1"}', expectedResult: '返回false，提示途经点中地点ID为空' },
  
  { caseNumber: 'Unit_Track_TS_002_002', caseDescription: 'trackname重复', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": ["tag"], "trackName": "track0"}', expectedResult: '返回false，提示路线名重复' },
  
  { caseNumber: 'Unit_Track_TS_002_003', caseDescription: '参数超过规定区间', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": [], "trackName": "test-track1"}', expectedResult: '返回false，提示路线名超出规定长度' },
  { caseNumber: 'Unit_Track_TS_002_003', caseDescription: '参数超过规定区间', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": ["science"], "trackName": "track1"}', expectedResult: '返回false，提示标签超出规定长度' },
  { caseNumber: 'Unit_Track_TS_002_003', caseDescription: '参数超过规定区间', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": -1}, {"pointID": "point00000000000000002","segment": 1}], "tag": ["tag"], "trackName": "track1"}', expectedResult: '返回false，提示途经点顺序超出规定范围' },
  
  { caseNumber: 'Unit_Track_TS_002_004', caseDescription: '参数在数据库不存在', input: '{"trackID": "track000000000000000-1", "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": ["tag"], "trackName": "track1"}', expectedResult: '返回false，提示路线ID不存在' },
  { caseNumber: 'Unit_Track_TS_002_004', caseDescription: '参数在数据库不存在', input: '{"trackID": "track000000000000000-1", "pointLists": [{"pointID": "point000000000000000-1","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": ["tag"], "trackName": "track1"}', expectedResult: '返回false，提示途经点不存在' },
  
  { caseNumber: 'Unit_Track_TS_002_005', caseDescription: '所有参数合法，修改成功', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": [], "trackName": "track1"}', expectedResult: '返回true' },
  { caseNumber: 'Unit_Track_TS_002_005', caseDescription: '所有参数合法，修改成功', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": [""], "trackName": "track1"}', expectedResult: '返回true' },
  { caseNumber: 'Unit_Track_TS_002_005', caseDescription: '所有参数合法，修改成功', input: '{"trackID": "track00000000000000001", "pointLists": [{"pointID": "point00000000000000001","segment": 0}, {"pointID": "point00000000000000002","segment": 1}], "tag": ["tag"], "trackName": "track1"}', expectedResult: '返回true' }
];

const testCases7 = [
  { caseNumber: 'Unit_Track_TS_003_001', caseDescription: '删除地点中trackID为空', input: 'trackID=""', expectedResult: '返回false，提示轨迹ID不能为空' },
  { caseNumber: 'Unit_Track_TS_003_002', caseDescription: '删除地点中trackID非空但不存在', input: 'trackID="track000000000000000-1"', expectedResult: '返回false，提示轨迹ID不存在' },
  { caseNumber: 'Unit_Track_TS_003_003', caseDescription: 'trackID合法，删除成功', input: 'trackID="track00000000000000001"', expectedResult: '返回true，删除成功' }
];


const runTest = () => {
 showReport.value = true
}
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