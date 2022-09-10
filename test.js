const fs = require("fs")
const path = require("path")
const child_process = require("child_process")



const task_process = child_process.spawn("G:/PsychoPy/python.exe",
[
    path.resolve("./src/tasks/vs2.py"),
    "test",
    path.resolve("./data"),
    "hzk_1452",


])

task_process.stdout.on("data",(buffer)=>{
    console.log(buffer.toString())
})