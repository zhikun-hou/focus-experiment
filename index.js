const { app,BrowserWindow,ipcMain } = require('electron')
const SqliteTableHandlers = require("./src/controllers/table")
const SubjectDataHandlers = require("./src/controllers/subject")
const ExperimentTaskHandlers = require("./src/controllers/task")
const ExperimentInfoHandlers = require("./src/controllers/experiment")
const BehaviorScaleHandlers = require("./src/controllers/scale")
const ExperimentReportHandlers = require("./src/controllers/report")
const ChartPaintingHandlers = require("./src/controllers/chart")
const DataAnalyzeHandlers = require("./src/controllers/analyze")
const CONFIG = require("./experiment.config")

//electron的入口文件
//修改此文件不需要重新vite build编译


//加载服务模块
ipcMain.use = (module_name,handlers)=>{
    for(let handler_name in handlers){
        let handler = handlers[handler_name]
        ipcMain.handle(module_name+":"+handler_name,handler)
    }
}


app.on('ready',()=>{
    const win = new BrowserWindow({
        width:1024,
        height:768,
        webPreferences:{
            //electron本质是用chrome内核去渲染网页，为了使用node的内置模块需要进行此项配置
            nodeIntegration:true,
            contextIsolation:false
        }
    })
    if(CONFIG.mode=="DEBUG"){
        const devtools = new BrowserWindow()
        win.webContents.setDevToolsWebContents(devtools.webContents)
        win.webContents.openDevTools({ mode: 'detach' })
        win.on('close',()=>{
            if(!devtools.isDestroyed)
                devtools.close()
        })
    }
    
    win.setMenu(null)
    win.loadFile('dist/index.html')
    

    //加载服务模块
    ipcMain.use("table",SqliteTableHandlers)
    ipcMain.use("subject",SubjectDataHandlers)
    ipcMain.use("task",ExperimentTaskHandlers)
    ipcMain.use("experiment",ExperimentInfoHandlers)
    ipcMain.use("scale",BehaviorScaleHandlers)
    ipcMain.use("report",ExperimentReportHandlers)
    ipcMain.use("chart",ChartPaintingHandlers)
    ipcMain.use("analyze",DataAnalyzeHandlers)
})


