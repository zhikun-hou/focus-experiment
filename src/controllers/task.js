
const CONFIG = require("../../experiment.config")
const {runScript} = require("./common")
const { record } = require("./experiment")
const path = require("path")


module.exports = {
    "run":async function(event,task_name,task_args){
        const task_path = path.resolve(CONFIG.taskScriptRoot,task_name+".py")
        return await runScript(task_path,task_args,(buffer)=>{
            pip_info = buffer.toString().trim()
            requests = pip_info.split("\n")
            for(let request of requests){
                if(!request.startsWith('{"experimentId')){
                    //不是以{开头，说明不是json，而是PsychoPy或pygame自带的一些输出
                    continue;
                }
                data = JSON.parse(request)
                
                if(CONFIG.mode=="DEBUG"){
                    console.log(data)
                }
                //原本是要在主线程中ipcMain.use的，在渲染线程使用ipcRenderer.invoke时会自动加一个event参数
                //这里是在主线程手动调用，所以要补一个null
                record(null,data)
    
            }
        })
    },
}