<script>
const {ipcRenderer} = require("electron");
import TaskLauncher from './TaskLauncher.vue'

export default {
    props:{
        options:Array,//task的列表
        subject:Object
    },
    components:{
        "task-launcher":TaskLauncher,
    },
    data(){
        return {
            currentIdx:-1,
            currentTask:null,
            isRunning:false
        }
    },
    methods:{
        selectTask(idx){
            this.currentIdx = idx
            this.currentTask = this.options[idx]
        },
        onTaskStart(){
            this.isRunning = true
        },
        onTaskOver(){
            this.isRunning = false
        }
    },
}
       
</script>

<template>
    <el-card class="box-card" v-loading="isRunning">
        <div class="task-list">
            <a class="task-tag" @click="selectTask(idx)" v-for="(task,idx) in options">
                <el-tag
                    :key="task.name"
                    class="mx-1"
                    :effect="idx==currentIdx ? 'dark':'plain'"
                >{{task.name}}
                </el-tag>
            </a>
        </div>
        <div class="line"></div>
        <div v-if="currentTask==null">
            <h2>点击标签选择目标任务</h2>
        </div>
        <div v-else>
            <div class="task-name">{{currentTask.name}}</div>
            <task-launcher :subject="subject" :option="currentTask" :beforeStart="onTaskStart" :afterOver="onTaskOver"></task-launcher>
        </div>
    </el-card>
</template>


<style scoped>
.task-list {
    margin-bottom:12px;
}
.task-tag{
    margin:6px;
}
.task-tag >>> .el-tag{
    margin-bottom:6px;
}
.task-tag:hover {
    cursor:pointer;
}
.line{
    border-top: 1px solid var(--el-border-color);
    margin-bottom:18px;
}

.task-name {
    margin-bottom:18px;
    font-weight:bolder;
}
</style>
