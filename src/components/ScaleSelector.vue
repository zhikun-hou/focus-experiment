<script>
    const {ipcRenderer} = require("electron");
    import ScaleForm from './ScaleForm.vue'
    
    export default {
        props:{
            options:Array,//scale的列表
            subject:Object
        },
        components:{
            "scale-form":ScaleForm,
        },
        data(){
            return {
                form:[],
                currentIdx:-1,
                currentScale:null,
            }
        },
        methods:{
            async selectScale(idx){
                this.currentIdx = idx
                this.currentScale = this.options[idx]
                this.form = await ipcRenderer.invoke("scale:load",this.currentScale.script)
            },
        }
    }
           
    </script>
    
    <template>
        <el-card class="box-card" >
            <div class="scale-list">
                <a class="scale-tag" @click="selectScale(idx)" v-for="(scale,idx) in options">
                    <el-tag
                        :key="scale.name"
                        class="mx-1"
                        :effect="idx==currentIdx ? 'dark':'plain'"
                    >{{scale.name}}
                    </el-tag>
                </a>
            </div>
            <div class="line"></div>
            <div v-if="currentScale==null">
                <h2>点击标签选择行为量表</h2>
            </div>
            <div v-else-if="subject==null">
                <h2>请选择被试以填写量表</h2>
            </div>
            <div v-else>
                <h2 class="scale-name">{{currentScale.name}}</h2>
                <scale-form :form="this.form" :subject="this.subject" :name="this.currentScale.name"></scale-form>
            </div>
        </el-card>
    </template>
    
    
    <style scoped>
    .scale-list {
        margin-bottom:12px;
    }
    .scale-tag{
        margin:6px 3px;
    }
    .scale-tag:hover {
        cursor:pointer;
    }
    .line{
        border-top: 1px solid var(--el-border-color);
        margin-bottom:18px;
    }
    
    .scale-name {
        margin-bottom:18px;
    }
    </style>
    