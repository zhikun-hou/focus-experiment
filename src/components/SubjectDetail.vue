<script>
    const {ipcRenderer} = require("electron");
    import { ElMessage } from 'element-plus'
    

    export default {
        props:{
            info:Object,
            edit:Function,
            back:Function
        },
        data(){
            return {
                isExportRunning:false,
                name:this.info.name,
                gender:this.info.gender,
                age:this.info.age,
                contact:this.info.contact,
                createdAt:this.info.createdAt
            }
        },
        methods:{
            async exportRecord(command){
                this.isExportRunning = true
                let success = false
                switch(command){
                    case "experiment":
                        success = await ipcRenderer.invoke("experiment:export","subjectId",[this.info.id],"experimentId")//导出同类实验的数据，按照实验号分表
                        break
                    case "scale":
                        success = await ipcRenderer.invoke("scale:export",[this.info.id],"scaleId")
                        break
                    default:
                        console.log("Unknown command")
                }
                
                if(!success){
                    ElMessage({
                        message: '导出失败.',
                        type: 'error',
                        offset: 100
                    })
                }

                this.isExportRunning = false
            }
        }
    }
           
</script>
    
<template>
    <el-descriptions title="被试详情" direction="vertical" :column="4" size="large" border >
        <el-descriptions-item label="姓名">{{name}}</el-descriptions-item>
        <el-descriptions-item label="性别">{{gender}}</el-descriptions-item>
        <el-descriptions-item label="年龄">{{age}}</el-descriptions-item>
        <el-descriptions-item label="联系方式">{{contact}}</el-descriptions-item>
    </el-descriptions>

    <div id="bottom-bar">
        <el-button @click="back">返回选择</el-button>
        <el-button type="success" @click="edit">修改信息</el-button>

        <el-dropdown @command="exportRecord" id="btn-export">
            <el-button type="primary" :disabled="isExportRunning">
                导出<el-icon class="el-icon--right"><arrow-down /></el-icon>
            </el-button>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item command="experiment">实验数据</el-dropdown-item>
                    <el-dropdown-item command="scale">量表记录</el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
    </div>
</template>

    
<style scoped>
#bottom-bar {
    margin-top: 16px;
}

#btn-export {
    margin-left:14px;
}
</style>
