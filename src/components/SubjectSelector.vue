<script>
import SubjectSearch from './SubjectSearch.vue'
import SubjectDetail from './SubjectDetail.vue'
import SubjectInput from './SubjectInput.vue'
const {ipcRenderer} = require("electron");
import { ElMessage } from 'element-plus'

export default {
    props:{
        "setCurrentSubject":Function
    },
    components:{
        "subject-detail":SubjectDetail,
        "subject-search":SubjectSearch,
        "subject-input":SubjectInput
    },
    data(){
        return {
            //如果当前被试为null，返回search
            //如果当前被试为null且在search界面点击了添加被试，返回create
            //已经选中了某个被试，返回detail
            mode : "search",
            detail:null,
            isExportRunning:false
        }
    },
    methods:{
        openCreate(){
            this.mode = "create"
            this.detail = null
            this.setCurrentSubject(null)
        },
        openDetail(info){
            this.mode = "detail"
            this.detail = info
            this.setCurrentSubject(info)
        },
        backToDetail(){
            //编辑信息时放弃，返回详情界面
            this.mode = "detail"
        },
        openSearch(){
            this.mode = "search"
            this.detail = null
            this.setCurrentSubject(null)
        },
        openEdit(){
            this.mode = "edit"
        },
        async exportRecord(command){
            this.isExportRunning = true
            let result = false
            switch(command){
                case "experiment":
                    result = await ipcRenderer.invoke("experiment:exportAll","experimentId")
                    break
                case "scale":
                    result = await ipcRenderer.invoke("scale:exportAll","scaleId")
                    break
                default:
                    console.log("Unknown command")
            }
            if(!result){
                ElMessage({
                        message: '部分文件导出失败.',
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
    <el-card class="box-card">
        <div v-if="mode=='search'">
            <subject-search :selectSubject="openDetail" ></subject-search>
            <div id="bottom-bar">
                <el-button id="btn-signup" @click="openCreate" type="success">登记被试</el-button>
                <el-dropdown @command="exportRecord">
                    <el-button type="primary" :disabled="isExportRunning">
                        全部导出<el-icon class="el-icon--right"><arrow-down /></el-icon>
                    </el-button>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item command="scale">量表记录</el-dropdown-item>
                            <el-dropdown-item command="experiment">实验数据</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </div>
        </div>

        <subject-detail v-else-if="mode=='detail'" :info="detail" :back="openSearch" :edit="openEdit"></subject-detail>

        <subject-input v-else-if="mode=='edit'" :back="backToDetail" :info="detail" :submit="openDetail" mode="edit"></subject-input>
        <subject-input v-else-if="mode=='create'" :back="openSearch" :submit="openDetail" mode="create"></subject-input>
    </el-card>
</template>


<style scoped>
    #bottom-bar {
        margin-top:16px;
    }
    #btn-signup {
        margin-right:16px;
    }
</style>
