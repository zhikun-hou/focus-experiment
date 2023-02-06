
const { create } = require("../sqlite/experiment")
const { record,fetchByExperimentName,fetchBySubjectId,fetchAll } = require("../sqlite/experimentRecord")
const { selectSavePath, exportData,groupBy,selectSaveRoot } = require("./common")
const {shell} = require("electron")


//虽然invoke的时候时按先后顺序提交的，但sqlite数据库在处理record时可能会导致失去顺序，比如trial 1先提交，但是在数据库里trial 2却被先保存了
const mergeTrialData = function(raw_data){
    const dataObj = raw_data.reduce((result,row)=>{
        if(!result[row["experimentId"]])
            result[row["experimentId"]] = {}
        const current_experiment = result[row["experimentId"]]

        if(!current_experiment[row["blockId"]])
            current_experiment[row["blockId"]] = {}
        const current_block = current_experiment[row["blockId"]]

        if(!current_block[row["trialId"]])
            current_block[row["trialId"]] = {//Base Info
                experimentName:row["experimentName"],
                subjectId:row["subjectId"],
                experimentId:row["experimentId"],
                blockId:row["blockId"],
                trialId:row["trialId"],
            }
        const current_trial = current_block[row["trialId"]]

        current_trial[row["dataName"]] = convertDataType(row["dataValue"],row["dataType"])//Merge Info
        return result
    },{})
    
    const rows = []
    for(const experiment_id in dataObj){
        const experiment = dataObj[experiment_id]
        for(const block_id in experiment){
            const block = experiment[block_id]
            for(const trial_id in block){
                rows.push(
                    block[trial_id]
                )
            }
        }
    }
    return rows
}
const convertDataType = function(val,type){
    switch(type){
        case "float":
        case "int":
            return Number(val)
        case "str":
            return String(val)
        case "NoneType":
            return null
        case "bool"://Boolean(x)只要字符串非空都返回true，只能用JSON.parse来转换
            val = val.toLowerCase()
        case "dict":
        case "list":
        case "set":
            return String(val)
        default:
            throw new Error("Unknown DataType")
    }
}

module.exports = {
    "create":async function(event,name,subject_id){
        return await create({
            "subjectId":subject_id,
            "experimentName":name
        })
    },
    "record":async function(event,info){
        return await record({
            "experimentId":info.experimentId,
            "blockId":info.blockId,
            "trialId":info.trialId,
            "dataName":info.dataName,
            "dataType":info.dataType,
            "dataValue":info.dataValue
        })
    },
    "data":async function(event,type,selector){
        if(type=="experimentName"){
            return await fetchByExperimentName(selector)
        } else if(type==="subjectId"){
            return await fetchBySubjectId(selector)
        } else {
            throw new Error("Unknown data type of experiment records.")
        }
    },
    "export":async function(event,by_what,selector,split=false){
        const save_path = await selectSavePath()
        if(!save_path) return false
        
        let raw_data = null
        switch(by_what){
            case "subject":
            case "subjectId":
            case "subject_id":
                raw_data = await fetchBySubjectId(selector)
                break
            case "experimentName":
            case "experiment_name":
                raw_data = await fetchByExperimentName(selector)
                break
            default:
                throw new Error("Unknown export method")
        }
        let rows = mergeTrialData(raw_data)
        if(!split){
            data = {
                "Sheet1":rows
            }
        } else {
            data = groupBy(rows,split)//subjectId 按被试分表   experimentId 按具体每次实验分表  experimentName按实验种类分表
        }
        return await exportData(save_path,data)
    },
    "exportAll":async function(event,split=false){
        const save_root = await selectSaveRoot()
        if(!save_root) return false
        
        let raw_data = await fetchAll()
        let rows = mergeTrialData(raw_data)
        let data = groupBy(rows,"subjectId")
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
            const promise = exportData(save_root+"\\"+subject_id+".xlsx",info,false)
            promises.push(promise)
        }
        
        let results = await Promise.all(promises)
        for(let result in results){
            if(result==false) return false
        }
        shell.showItemInFolder(save_root)
        return true
    },


}