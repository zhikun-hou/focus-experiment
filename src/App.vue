<script lang="ts">
import type { TabsPaneContext } from 'element-plus'
import { toRaw } from 'vue'
import SubjectSelector from './components/SubjectSelector.vue'
import TaskSelector from './components/TaskSelector.vue'
import ScaleSelector from './components/ScaleSelector.vue'
import Banner from './components/Banner.vue'
const {ipcRenderer} = require("electron")

export default {
  components:{
    "subject-selector":SubjectSelector,
    "task-selector":TaskSelector,
    "scale-selector":ScaleSelector,
    "banner":Banner,
  },
  data:function(){
    return {
      activeName:"/subject",
      subject:null,
      tasks:toRaw(this.config.taskConfig)
    }
  },
  methods:{
    switchPage:function(tab: TabsPaneContext, event: Event){
      
    },
    updateSubjectInfo(info){
      this.subject = info
    }
  },
  async mounted(){
    /*  彩蛋  */
    console.log("【开发单位】北京师范大学 - 认知神经科学与学习国家重点实验室")
    console.log("【开发者】李小俚导师课题组 - 侯志琨")
    console.log("【寄语】心事浩茫连广宇，于无声处听惊雷。")
  },
}

</script>

<template>
  <div id="main">
    <banner :pic="this.config.banner"></banner>
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="switchPage">
      <el-tab-pane label="选择被试" name="/subject">
        <subject-selector :setCurrentSubject="updateSubjectInfo"></subject-selector>
      </el-tab-pane>
      <el-tab-pane v-for="(val,key,idx) in tasks" :label="key" :name="key">
        <task-selector v-if="val.type=='task'" :options="val.options" :subject="this.subject"></task-selector>
        <scale-selector v-else-if="val.type=='scale'" :options="val.options" :subject="this.subject"></scale-selector>
      </el-tab-pane>
    </el-tabs>
  </div>


</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background-color:#e1e4e7;

}

#main {
  margin-top: 26px;
  margin-bottom:26px;
}
.demo-tabs {
  margin:0 128px;
}
.demo-tabs .el-tabs__header {
  border-radius:4px;
  padding:0 32px;
  margin-bottom:0;
  background-color: white;
}
body {
  background-color:#e1e4e7;
  margin:0;
}


* {
    user-select:none;
}
</style>
