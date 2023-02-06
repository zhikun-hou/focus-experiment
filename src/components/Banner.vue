<script>
    const path = require("path")
    
    export default {
        props:{
            pic:String,
        },
        data:function(){
            return {
                src: path.resolve(this.pic)
            }
        }
    }
    </script>
    
    <template>

        <div class="banner">
            <img :src="this.src" />
        </div>
    </template>
    
    
    <style scoped>

    .banner {
        margin:0 128px;
        margin-bottom:12px;
    }
    .banner img {
        display: block;
        margin:0 auto;
        max-width:100%;
        border-radius:8px;
    }
    </style>
    