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
      folderName:"",
    }
  },
  computed:{
    tasks(){
      const tasks = JSON.parse(JSON.stringify(this.config.tasks))//深拷贝
      const common_args = [this.config.dataRoot,this.folderName]
      for(let collection_name in tasks){
        const collection = tasks[collection_name]
        for(let task_id in collection){
          const task = collection[task_id]
          const task_name = task["name"]
          if("args" in task){
            task["args"] = [collection_name+"_"+task_name,...common_args,...task["args"]]
          } else {
            task["args"] = [collection_name+"_"+task_name,...common_args]
          }
        }
      }
      return tasks;
    }
  },
  methods:{
    switchPage:function(tab: TabsPaneContext, event: Event){
      
    },
    updateSubjectInfo(info){
      if(info==null){
        this.subject = null
        this.folderName = ""
      } else {
        this.subject = info
        this.folderName = info.name  +  "_"  +  info.contact
      }
    }
  },
  mounted(){
    /*  彩蛋  */
    console.log("【开发单位】北京师范大学 - 认知神经科学与学习国家重点实验室");
    console.log("【开发者】李小俚导师课题组 - 侯志琨");
    console.log("【寄语】心事浩茫连广宇，于无声处听惊雷。");
  }
}

</script>

<template>
  <div id="header">
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="switchPage">
      <el-tab-pane label="被试信息" name="/subject">
        <subject-info :callback="updateSubjectInfo"></subject-info>
      </el-tab-pane>
      <el-tab-pane v-for="(val,key,idx) in tasks" :label="key" :name="key">
        <task-panel :options="val" :subject="this.subject"></task-panel>
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
