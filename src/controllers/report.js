const fs = require("fs").promises
const pdf = require("html-pdf")
const CONFIG = require("../../experiment.config")



module.exports = {
    "pdf":async function(event,save_path,template_name,template_args){
        let html = await fs.readFile(CONFIG.reportTemplateRoot+"\\"+template_name+".html",encoding="utf-8")
        let params = html.matchAll(/{{(\s*\w*\s*)}}/g)//惰性模式下全局匹配
        for(let param_info of params){
            let param_target = param_info[0]
            let param_key = param_info[1].trim()
            let param_value = template_args[param_key]// bind
            if(param_value){
                html = html.replace(param_target,param_value)
            }
        }

        let is_running = new Promise((resolve,reject)=>{
            pdf.create(
                html,
                {
                    format:"A4",
                    "border": {
                        "top": "2.8cm",
                        "right": "2.5cm",
                        "bottom": "2.5cm",
                        "left": "3.0cm"
                    },
                },
            ).toFile(save_path,(err,res)=>{
                if(err){
                    reject(err)            
                    if(CONFIG.mode=="DEBUG")
                        console.log("[report:pdf]"+err)
                } else {
                    resolve(res)
                    if(CONFIG.mode=="DEBUG")
                        console.log("[report:pdf]"+res)
                }
            })
        })

        return await is_running
    },
}