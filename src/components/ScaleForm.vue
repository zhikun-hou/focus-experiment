<script>
    const {ipcRenderer} = require("electron")
    import { ElMessage } from 'element-plus'

    export default {
        props:{
            name:String,
            form:Array,//量表
            subject:Object
        },
        computed:{
            isOK(){
                for(let item of this.form){
                    if(item.selection==undefined || item.selection==null || item.selection==-1)
                        return false
                }
                return true
            },
            results(){
                return this.form.map((item)=>{
                    let selection = item.answer[item.selection]
                    return {
                        "question":item.question,
                        "answer":selection.text,
                        "score":selection.score
                    }
                })
            }
        },
        methods:{
            async submit(){
                let meta_exist = await ipcRenderer.invoke(
                    "table:exist",
                    "scale"
                )
                if(meta_exist==false){
                    await ipcRenderer.invoke(
                        "table:create",
                        "scale"
                    )
                }
                let record_exist = await ipcRenderer.invoke(
                    "table:exist",
                    "scaleRecord"
                )
                if(record_exist==false){
                    await ipcRenderer.invoke(
                        "table:create",
                        "scaleRecord"
                    )
                }

                await ipcRenderer.invoke("scale:create",this.name,this.subject.id)
                const scale_id = await ipcRenderer.invoke(
                    "table:latest",
                    "scale"
                )

                await ipcRenderer.invoke("scale:submit",scale_id,this.results)
                for(let item of this.form){//清空表单
                    item.selection = -1
                }
                ElMessage({
                    message: '提交成功.',
                    type: 'success',
                    offset: 100
                })
            }
        },
    }
           
    </script>
    
    <template>
        <p v-for="item in form"> 
            <h3>{{item.question}}</h3>
            <el-radio-group  v-model="item.selection">
                <el-radio v-for="(answer,idx) in item.answer" :label="idx">{{answer.text}}</el-radio>
            </el-radio-group>
        </p>

        <el-button type="success" :disabled="!isOK" @click="submit">提交</el-button>

    </template>
    
    
    <style scoped>
    </style>
    