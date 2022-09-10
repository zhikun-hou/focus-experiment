const path = require("path")

const fs = require("fs")

export default {
    env:"./src/PsychoPy/python.exe",
    dataRoot:path.resolve("./data"),
    taskScriptRoot:path.resolve("./src/tasks"),
    tasks:JSON.parse(fs.readFileSync("./src/experiment.config.json"))
}