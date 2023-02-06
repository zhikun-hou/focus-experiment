<script>
    
    const {ipcRenderer} = require("electron");


    export default {
        props:{
            selectSubject:Function
        },
        data(){
            return {
                name:"",
                result:[]
            };
        },
        computed:{

        },
        methods:{
            async search(str){
                this.result.length = 0
                const list = await ipcRenderer.invoke(
                    "subject:match",
                    str
                )
                for(let item of list){
                    this.result.push(item)//响应式修改数组
                }
            },
            select(row,column,event){
                this.selectSubject(row)
            }
        },
        async mounted(){
            let table_exist = await ipcRenderer.invoke(
                "table:exist",
                "subject"
            )
            if(table_exist==false){
                await ipcRenderer.invoke(
                    "table:create",
                    "subject"
                )
            }
            this.result = await ipcRenderer.invoke("subject:all")
        }
    }
           
    </script>
    
    <template>
        
        <el-input v-model="name" @input="search" placeholder="检索被试库..." />
        
        <el-table :data="result" :default-sort="{ prop: 'createdAt', order: 'descending' }"
            @row-click="select" max-height="512" table-layout="auto">
            <el-table-column prop="id" label="ID" sortable width="64"/>
            <el-table-column prop="name" label="姓名" sortable width="128" />
            <el-table-column prop="gender" label="性别" width="64" />
            <el-table-column prop="age" label="年龄" sortable width="81" />
            <el-table-column prop="contact" label="联系方式" />
            <el-table-column prop="createdAt" label="登记时间" sortable />
        </el-table>

            
    </template>
    
    
    <style scoped>
        .el-table >>> tr.el-table__row:hover {
            cursor:pointer;
        }
    </style>
    