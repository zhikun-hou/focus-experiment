<script>
    const {ipcRenderer} = require("electron");
    import { ElMessage } from 'element-plus'
    
    export default {
        props:{
            option:Object,
            subject:Object,
            beforeStart:Function,
            afterOver:Function
        },
        data(){
            return {
                isTaskRunning:false,
                isExportRunning:false
            }
        },
        computed:{
            args(){
                const args = []
                if(this.option.args){
                    for(let arg of this.option.args){
                        if(arg.default){
                            arg.value = arg.default
                        } else {
                            arg.value = null
                        }
                        args.push(arg)
                    }
                }
                return args    
            },
            isTaskPrepared(){
                if(this.subject==null)
                    return false
                if(this.isTaskRunning===true)
                    return false;
                
                for(let arg of this.args){
                    if(arg.value==undefined || arg.value==null || arg.value=="") return false;
                }
    
                return true;
            }
        },
        methods:{
            async runTask(){
                //开启子进程并等待完成
                this.beforeStart()
                this.isTaskRunning = true

                //在experiment表中新建实验
                let experiment_exist = await ipcRenderer.invoke(
                    "table:exist",
                    "experiment"
                )
                if(experiment_exist==false){//如果没有experiment表，先创建
                    await ipcRenderer.invoke(
                        "table:create",
                        "experiment"
                    )
                }

                //检测record表是否存在
                let record_exist = await ipcRenderer.invoke(
                    "table:exist",
                    "experimentRecord"
                )
                if(record_exist==false){//如果没有experiment表，先创建
                    await ipcRenderer.invoke(
                        "table:create",
                        "experimentRecord"
                    )
                }

                await ipcRenderer.invoke("experiment:create",this.option.name,this.subject.id)
                //获取新建实验的id
                const experiment_id = await ipcRenderer.invoke(
                    "table:latest",
                    "experiment"
                )

                //运行python实验程序
                let args = this.args.map((arg)=>{
                    return arg.key+"="+arg.value
                })
                await ipcRenderer.invoke("task:run",this.option.script,["experimentId="+experiment_id,...args])
                this.isTaskRunning = false
                this.afterOver()
            },
            async exportData(){
                this.isExportRunning = true
                let success = await ipcRenderer.invoke("experiment:export","experimentName",this.option.name,"experimentId")//导出同类实验的数据，按照实验序号分表
                if(!success){                    
                    ElMessage({
                        message: '导出失败.',
                        type: 'error',
                        offset: 100
                    })
                }
                this.isExportRunning = false
            }
        },
    }
           
    </script>
    
    <template>
        <el-form label-width="92px">
            <el-form-item :label="arg.name" v-for="arg in this.args">
                <el-input v-model="arg.value" />
            </el-form-item>
            <el-form-item>
                <el-button type="success" size="large" @click="runTask" :disabled="!isTaskPrepared">开始</el-button>
                <el-button type="primary" size="large" @click="exportData" :disabled="isTaskRunning || isExportRunning">导出</el-button>
            </el-form-item>
        </el-form>
        <div v-if="subject==null">
            <el-alert title="请选择被试以开始实验" type="warning" />
        </div>
        <div v-else-if="!isTaskPrepared">
            <el-alert title="请输入实验参数，或等待进行中的实验完成" type="warning" />
        </div>
        <div v-else>
            <el-alert title="实验数据自动存入数据库，可手动导出为表格文件" type="success" />
        </div>
    </template>
    
    
    <style scoped>
        
    </style>
    