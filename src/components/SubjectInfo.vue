<script>
const path = require("path")
const fs = require("fs")
//NodeJS内置模块，在electron环境下可直接使用
//Vite环境由于是浏览器运行，需要安装插件

export default {
    props:{
        callback:Function,
    },
    data(){
        return {
            name:null,
            gender:null,
            age:null,
            contact:null,
            submited:false
        };
    },
    computed:{
        isOK(){
            return this.name!=null && this.gender!=null && this.age!=null && this.contact!=null
        },
        genderName(){
            switch(this.gender){
                case "1":
                case 1: return "男";
                case "0":
                case 0: return "女";
                default:
                    return "异常";
            }
        },
    },
    methods:{
        submit(){
            const as_info = {
                "姓名":this.name,
                "性别":this.genderName,
                "年龄":this.age,
                "联系方式":this.contact,
            }
            const as_meta = {
                "name":this.name,
                "gender":this.genderName,
                "age":this.age,
                "contact":this.contact,
            }
            this.callback(as_meta)
            this.submited = true

            //可能有重名的两个人，也可能有一个人多次测试，所以用name_contact来命名文件夹以区分重名
            const dir = path.resolve(this.config.dataRoot,this.name+"_"+this.contact)
            try{
                fs.mkdirSync(dir,{ recursive: true })
            } catch(err){
                //already exists
                //不是第一次对该被试进行测试
            }

            const data = JSON.stringify(as_info)
            fs.writeFileSync(path.resolve(dir,"被试信息.json"),data)
        },
        clear(){
            this.callback(null)
            this.submited = false

            this.name = null
            this.gender = null
            this.age = null
            this.contact = null
        }
    }
}
       
</script>

<template>
    <el-card class="box-card">

        <el-form label-width="120px">
            <el-form-item label="姓名">
                <el-input v-model="name" placeholder="姓名" />
            </el-form-item>

            <el-form-item label="性别">
                <el-radio-group v-model="gender">
                    <el-radio label="1">男</el-radio>
                    <el-radio label="2">女</el-radio>
                </el-radio-group>
            </el-form-item>

            <el-form-item label="年龄">
                <el-input v-model="age" placeholder="年龄" />
            </el-form-item>

            <el-form-item label="联系方式">
                <el-input v-model="contact" placeholder="手机号或邮箱" />
            </el-form-item>

            <el-form-item>
                <el-popconfirm title="确定无误？"
                    confirm-button-text="确定"
                    cancel-button-text="有误"
                    @confirm="submit"
                    >
                    <template #reference>
                        <el-button type="success" :disabled="!isOK || submited">提交</el-button>
                    </template>
                </el-popconfirm>
                <el-button type="warning" :disabled="!submited" @click="clear">下一位</el-button>
            </el-form-item>
        
        </el-form>
    </el-card>
</template>


<style scoped>

</style>
