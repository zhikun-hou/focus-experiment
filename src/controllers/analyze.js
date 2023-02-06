
const CONFIG = require("../../experiment.config")
const path = require("path")
const {waitScript,getArgsList} = require("./common")


module.exports = {
    //name是算法名称，比如算C0复杂度的脚本、算排序熵的脚本；每个脚本对应一种数据分析的方式，通过print来输出
    "eeg":async function(event,algorithm_name,file_path,algorithm_args){//加载edf文件进行分析
        const algorithm_path = path.resolve(CONFIG.analysisAlgorithmRoot,algorithm_name+".py")//file_path是edf文件的位置，是必填参数

        return await waitScript(algorithm_path,["filePath="+file_path,...getArgsList(algorithm_args)])
    },
    "performance":async function(event,algorithm_name,algorithm_args){//加载数据库分析
        const algorithm_path = path.resolve(CONFIG.analysisAlgorithmRoot,algorithm_name+".py")
        return await waitScript(algorithm_path,getArgsList(algorithm_args))
    }
}