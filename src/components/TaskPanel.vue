<script>
const path = require('path')
const child_process = require('child_process')

export default {
    props:{
        options:Array,//task的列表
        subject:Object
    },
    data(){
        return {
            current:null,
            args:[],
            argsInputer:[],
            isRunning:false
        }
    },
    computed:{
        tasks(){
            this.args = this.options.map((task,task_idx)=>{
                task.selected = false;
                this.argsInputer[task_idx] = []
                const args = []
                for(let arg_idx in task.args){
                    const arg = task.args[arg_idx]
                    if(typeof arg === "object"){//需要手动输入的参数
                        //创建inputer
                        this.argsInputer[task_idx].push({
                            name:arg.name,
                            arg_idx,
                            task_idx
                        })
                        //设定默认值
                        args.push(null)
                    } else {
                        args.push(arg)
                    }
                }
                return args;
            })

            return this.options
        },
        isOK(){
            if(this.subject==null)
                return false
            if(this.current===null)
                return false;
            
            for(let arg_idx in this.args[this.current]){
                const arg = this.args[this.current][arg_idx]
                if(arg==null) return false;
            }

            return true;
        }
    },
    methods:{
        select(idx){
            if(this.current!=null){
                this.tasks[this.current].selected = false;
            }
            this.tasks[idx].selected = true;
            this.current = idx;
        },    
        start(){
            const script_path = path.resolve(this.config.taskScriptRoot,this.tasks[this.current].script)
            const argv = [
                script_path,
                ...this.args[this.current]
            ]
            //开启子进程
            this.isRunning = true
            const task_process = child_process.spawn(this.config.env,argv)
            task_process.on("exit",(code,signal)=>{
                this.isRunning = false
            })
            task_process.stdout.on("data",(buffer)=>{
                console.log(buffer.toString)
            })
        },
    },
}
       
</script>

<template>
    <el-card class="box-card" v-loading="isRunning">
        <div class="task-list">
            <a class="task-tag" @click="select(idx)" v-for="(task,idx) in tasks">
                <el-tag
                    :key="task.name"
                    class="mx-1"
                    :effect="task.selected ? 'dark':'plain'"
                >{{task.name}}
                </el-tag>
            </a>
        </div>
        <div class="line"></div>
        <div v-if="current==null">
            <h2>点击标签选择目标任务</h2>
        </div>
        <div v-else>
            <div class="task-name">{{this.tasks[this.current].name}}</div>
            <el-form label-width="92px">
                <el-form-item :label="inputer.name" v-for="inputer in this.argsInputer[this.current]">
                    <el-input v-model="this.args[inputer.task_idx][inputer.arg_idx]" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" size="large" @click="start" :disabled="!isOK || isRunning">开始</el-button>
                </el-form-item>
            </el-form>
        </div>
    </el-card>
</template>


<style scoped>
.task-list {
    margin-bottom:12px;
}
.task-tag{
    margin:6px 3px;
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
