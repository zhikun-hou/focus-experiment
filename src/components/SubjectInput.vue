<script>
    const {ipcRenderer} = require("electron");
    import {toRaw} from "vue"

    export default {
        props:{
            back:Function,
            info:{
                type:Object,
                default:{}
            },
            submit:Function,
            mode:String
        },
        data(){
            if(this.mode=="create"){ 
                return {
                    name:"",
                    gender:-1,
                    age:"",
                    contact:"",
                }
            } else if(this.mode=="edit"){    
                return {
                    name:this.info.name,
                    gender:this.getGenderIndexByName(this.info.gender),
                    age:this.info.age,
                    contact:this.info.contact,
                }
            }
        },
        computed:{
            isOK(){
                return this.name.length>0 && this.gender>-1 && typeof this.age=="number" && this.age>0 && this.contact.length>0
            },
        },
        methods:{
            async submit(){
                this.info.name = this.name
                this.info.gender = this.getGenderNameByIndex(this.gender)
                this.info.age = this.age
                this.info.contact = this.contact
                
                if(this.mode=="create"){
                    await this.create()
                    this.info.id = await ipcRenderer.invoke(
                        "table:latest",
                        "subject"
                    )
                } else if(this.mode=="edit"){
                    await this.edit()
                }
                this.submit(this.info)
            },
            async create(){
                return await ipcRenderer.invoke(
                    "subject:insert",
                    toRaw(this.info)
                )
            },
            async edit(){
                return await ipcRenderer.invoke(
                    "subject:edit",
                    toRaw(this.info)
                )
            },
            getGenderNameByIndex(idx){
                switch(idx){
                    case "1":
                    case 1: return "男"
                    case "0":
                    case 0: return "女"
                    default:
                        return "?"
                }
            },
            getGenderIndexByName(name){
                switch(name){
                    case "男":
                        return "1"
                    case "女":
                        return "0"
                    default:
                        return "-1"
                }
            }
        }
    }
           
    </script>
    
    <template>
        <el-form label-width="120px">
            <el-form-item label="姓名">
                <el-input v-model="name" placeholder="姓名" />
            </el-form-item>

            <el-form-item label="性别">
                <el-radio-group v-model="gender">
                    <el-radio label="1">男</el-radio>
                    <el-radio label="0">女</el-radio>
                </el-radio-group>
            </el-form-item>

            <el-form-item label="年龄">
                <el-input v-model.number="age" placeholder="年龄" />
            </el-form-item>

            <el-form-item label="联系方式">
                <el-input v-model="contact" placeholder="手机号或邮箱" />
            </el-form-item>

            <el-form-item>
                <el-button @click="back">返回</el-button>
                <el-popconfirm title="确定无误？"
                    confirm-button-text="确定"
                    cancel-button-text="有误"
                    @confirm="submit"
                    >
                    <template #reference>
                        <el-button type="success" :disabled="!isOK">提交</el-button>
                    </template>
                </el-popconfirm>
            </el-form-item>
        
        </el-form>
    </template>
    
    
    <style scoped>
    
    </style>
    