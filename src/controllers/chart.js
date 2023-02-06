
const CONFIG = require("../../experiment.config")
const path = require("path")
const {waitScript,getArgsList} = require("./common")

//绘图模块
//用来在report中插入图表
//原本打算用canvas实现的，但是node-canvas兼容性太jb差了，还是用python来吧
//用合适的工具干合适的事


module.exports = {
    "paint":async function(event,painter_name,painter_args){
        const script_path = path.resolve(CONFIG.chartPainterRoot,painter_name+".py")
        return "data:image/png;base64,"+await waitScript(script_path,getArgsList(painter_args))
    },
}