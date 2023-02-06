
const {dialog,shell} = require("electron")
const ExcelJS = require('exceljs')
const CONFIG = require("../../experiment.config")
const child_process = require("child_process")

const selectSavePath = async function(){
    const response = await dialog.showSaveDialog({
        title:"导出为表格文件",
        filters:[
            {
                name:"Excel表格文件",
                extensions:[
                    "xlsx"
                ]
            },
            {
                name:"通用数据文件",
                extensions:[
                    "csv"
                ]
            }
        ]
    })
    return response.filePath
}
const selectSaveRoot = async function(){
    const response = await dialog.showOpenDialog({
        title:"导出所有表格到文件夹",
        properties:[
            "openDirectory","createDirectory","promptToCreate"
        ]
    })
    return response.filePaths[0]
}

const exportData = async(path,data,show_in_explorer=true) => {
    const workbook = new ExcelJS.Workbook()
    workbook.creator = 'Beijing Normal University';
    workbook.lastModifiedBy = 'Beijing Normal University';

    workbook.created = new Date()
    workbook.modified = new Date()
    workbook.calcProperties.fullCalcOnLoad = true
    
    let sheet_number = 0
    for(let sheet_name in data){
        const sheet = workbook.addWorksheet(sheet_name)
        
        let sheet_data = data[sheet_name]
        if(sheet_data.length>0){
            sheet.columns = Object.keys(sheet_data[0]).map((name)=>{
                return {header:name,key:name,width:16}
            })
            sheet.addRows(sheet_data)
        }
        sheet_number++
    }
    if(sheet_number==0){//有可能Select为空导致data=[]，这样excel没有sheet就会bug
        workbook.addWorksheet("Sheet1")
    }
    
    const extension = getExtension(path)
    try{
        if(extension=="xlsx"){
            await workbook.xlsx.writeFile(path)
        } else if(extension=="csv"){
            await workbook.csv.writeFile(path)
        } else {
            throw new Error("Unknown file extension")
        }
    }catch(err){
        return false
    }
    if(show_in_explorer) shell.showItemInFolder(path)
    return true
}

const getExtension = function(path){
    const pos = path.lastIndexOf(".")//.xlsx
    return path.substring(pos+1)//xlsx
}

const groupBy = function(arr, key) {//Array.group是实验特性，node貌似不支持
    return arr.reduce(function(result, current) {
      (result[current[key]] = result[current[key]] || []).push(current);
      return result;
    }, {});
}

const runScript = async(script_path,script_args,handler)=>{
    if(!(script_args instanceof Array)){
        script_args = []
    }
    const task_process = child_process.spawn(CONFIG.env,[script_path,...script_args])

    //启动通信管道
    task_process.stdout.on("data",handler)
    
    //RUN!!!!
    if(CONFIG.mode=="DEBUG"){
        console.log("=======")
        console.log("[Run Script]"+CONFIG.env+" "+script_path+" "+script_args.join(" "))
    }
    let is_running = new Promise((resolve,reject)=>{

        task_process.on("error",(err)=>{
            //用于处理进程无法创建/杀死/传递消息，进程内部的error不会触发这里
            console.log("[Error]"+err)
            console.log("=======")
            reject(err)
        })
        task_process.on("exit",(code,signal)=>{
            //返回return值，在python中需要使用sys.exit(114514)来设置
            console.log("[Return]"+code)
            
            console.log("=======")
            resolve(signal)
        })
    })

    await is_running
}
const waitScript = async(script_path,script_args)=>{
    let data = ""
    await runScript(script_path,script_args,(buffer)=>{
        data += buffer.toString()
    })
    return data
}


const getArgsList = (arg_obj)=>{
    let args = []
    for(let key in arg_obj){
        args.push(
            key+"="+JSON.stringify(arg_obj[key])
        )
    }
    return args
}

module.exports = {
    exportData,
    selectSavePath,
    selectSaveRoot,
    getExtension,
    groupBy,
    runScript,
    waitScript,
    getArgsList
}