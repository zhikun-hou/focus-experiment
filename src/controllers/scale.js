const fs = require("fs").promises
const { submit,fetchBySubjectId,fetchAll } = require("../sqlite/scaleRecord")
const CONFIG = require("../../experiment.config")
const { create } = require("../sqlite/scale")
const {exportData,selectSavePath,groupBy,selectSaveRoot} = require("./common")

module.exports = {
    "load":async function(event,name){
        return await JSON.parse(await fs.readFile(CONFIG.scaleRoot+"/"+name+".json"))
    },
    "create":async function(event,name,subject_id){
        return await create({
            "subjectId":subject_id,
            "scaleName":name
        })
    },
    "submit":async function(event,scale_id,items){
        for(let item of items){
            item["scaleId"] = scale_id
        }
        return await submit(items)
    },
    "export":async function(event,selector,split=false){
        const save_path = await selectSavePath()
        if(!save_path) return
        
        let raw_data = await fetchBySubjectId(selector)
          
        if(!split){
            data = {
                "Sheet1":raw_data
            }
        } else {
            data = groupBy(raw_data,split)//subjectId 按被试分表   scaleId 每份量表都是一张表  scaleName 按量表种类分表
        }
        return await exportData(save_path,data)
    },
    "exportAll":async function(event,split=false){
        const save_root = await selectSaveRoot()
        if(!save_root) return
        
        let raw_data = await fetchAll()
        let data = groupBy(raw_data,"subjectId")

        const promises = []
        for(let subject_id in data){
            let info = data[subject_id]
            if(!split){
                info = {
                    [subject_id]:info
                }
            } else {
                info = groupBy(info,split)
            }
            const promise = exportData(save_root+"\\"+subject_id+".xlsx",info)
            promises.push(promise)
        }
        
        await Promise.all(promises)
    },


}