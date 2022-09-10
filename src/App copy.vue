<script lang="ts">
import type { TabsPaneContext } from 'element-plus'
import SubjectInfo from './components/SubjectInfo.vue'
import TaskPanel from './components/TaskPanel.vue'

const path = require('path')

export default {
  components:{
    "subject-info":SubjectInfo,
    "task-panel":TaskPanel,
  },
  data:function(){
    return {
      activeName:"/subject",
      subject:null,
      subjectName:"",
      subjectContact:""
    }
  },
  computed:{
    folderName(){
      return this.subjectName  +  "_"  +  this.subjectContact
    },
    eeg(){
      const args = [this.config.dataRoot,this.folderName,{name:"block数目"},{name:"trails数目"}]//prop时需要使用json来深拷贝，避免丢失为null
      return [
        {name:"选择性注意",script:"./vs_eeg.py",args:["任务脑电_选择性注意",...args]},
        {name:"持续性注意",script:"./cpt_eeg.py",args:["任务脑电_持续性注意",...args,{name:"目标刺激数"}]},
        {name:"执行控制",script:"./oct_eeg.py",args:["任务脑电_执行控制",...args]},
      ]
    },
    cognitive(){
      const args = [this.config.dataRoot,this.folderName]
      return [
        {name:"选择性注意",script:"./vs.py",args:["认知范式_选择性注意",...args]},
        {name:"持续性注意",script:"./cpt.py",args:["认知范式_持续性注意",...args]},
        {name:"执行控制",script:"./oct.py",args:["认知范式_执行控制",...args]},
      ]
    }
  },
  methods:{
    switchPage:function(tab: TabsPaneContext, event: Event){
      
    },
    updateSubjectInfo(info){
      if(info==null){
        this.subjectName = null
        this.subjectContact = null
      } else {
        this.subject = info
        this.subjectName = info.name
        this.subjectContact = info.contact
      }
    }
  },
  mounted(){
    
  }
}

</script>

<template>
  <div id="header">
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="switchPage">
      <el-tab-pane label="被试信息" name="/subject">
        <subject-info :callback="updateSubjectInfo"></subject-info>
      </el-tab-pane>
      <el-tab-pane label="任务脑电" name="/eeg">
        <task-panel :options="eeg" :subject="this.subject"></task-panel>
      </el-tab-pane>
      <el-tab-pane label="认知范式" name="/cognitive">
        <task-panel :options="cognitive" :subject="this.subject"></task-panel>
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

#header {
}
.demo-tabs {
  margin:0 128px;
}
.demo-tabs .el-tabs__header {
  border-radius:4px;
  padding:0 32px;
  margin-top: 14px;
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
