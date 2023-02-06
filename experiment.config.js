const path = require("path")

const fs = require("fs")


//module.exports    CommonJS规范，用于支持Node和electron
//export default    ES6规范，用于支持Vue和Vite

//将mode改为DEBUG可以进入测试环境，会在终端打印各种log
module.exports = {
    mode:"DEBUG",//DEBUG RELEASE
    env:"./src/PsychoPy/python.exe",
    banner:"./src/banner.png",
    sqlitePath:"./sqlite.db",
    taskScriptRoot:"./src/tasks",
    taskConfig:JSON.parse(fs.readFileSync("./experiment.config.json")),
    scaleRoot:"./src/scales",
    reportTemplateRoot:"./src/reports",
    analysisAlgorithmRoot:"./src/analysis",
    chartPainterRoot:"./src/charts"
}