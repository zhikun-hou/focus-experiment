const {app,BrowserWindow} = require('electron')

//electron的入口文件
//修改此文件不需要重新vite build编译

const MODE = "RELEASE"
//const MODE = "DEBUG"

app.on('ready',()=>{
    const win = new BrowserWindow({
        width:800,
        height:600,
        webPreferences:{
            //electron本质是用chrome内核去渲染网页，为了使用node的内置模块需要进行此项配置
            nodeIntegration:true,
            contextIsolation:false
        }
    })
    if(MODE=="DEBUG") win.webContents.openDevTools()
    
    win.setMenu(null)
    win.loadFile('dist/index.html')
    
    
})

