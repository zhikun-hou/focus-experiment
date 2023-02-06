const sqlite3 = require('sqlite3')
const {open} = require('sqlite')
const CONFIG = require("../../experiment.config")


const connect = async()=>{
    //如果不存在sqlite数据库，会自动生成一个.db文件
    //因此不用做存在判断
    return await open({
        filename: CONFIG.sqlitePath,
        driver: sqlite3.Database
    })
}

const enableDebug = async()=>{
    sqlite3.verbose()
}

/* -----------MAIN------------- */
const DB_PROMISE = connect()
if(CONFIG.mode=="DEBUG"){
    enableDebug()
}
/* ----------------------------- */

const run = async(callback)=>{
    const db = await DB_PROMISE
    return await callback(db)
}

//表的存在性判断
const isTableExist = async(table_name)=>{
    return (await run(async(db)=>{
            return await db.get(
                generateSQL(
                    "SELECT count(*) as count FROM sqlite_master WHERE type='table' AND name=:table_name",
                    {
                        ":table_name":table_name
                    }
                )
            )
        })
    ).count>0
}
//创建表
const createTable = async(table_name,table_info)=>{
    return await run(async(db)=>{
        return await db.run(
            generateSQL(
                "CREATE TABLE @table_name (@table_description)",
                {
                    "@table_name":table_name,
                    "@table_description":generateTableDescription(table_info)
                }
            )
        )
    })
}
const generateTableDescription = (table_info)=>{
    let arr = []
    for(let column_name in table_info){
        let column_info = table_info[column_name]
        arr.push(column_name+" "+column_info)
    }
    return arr.reduce((str,item)=>{
        return str+","+item
    })
}
//表中最新的id
const selectNewestId = async(table_name)=>{
    return (await run(async(db)=>{
            return await db.get(
                generateSQL(
                    "SELECT last_insert_rowid() as id FROM @table_name",
                    {
                        "@table_name":table_name
                    }
                )
            )
        })
    ).id
}

//nodejs的sqlite库，默认在绑定参数时会加''，绑参数很好，但是动态生成sql语句会有问题
const generateSQL = (statement,bind)=>{
    //for ... in循环出的是key，for ... of循环出的是value

    //用:param匹配注入参数，自动加上单引号
    let params = statement.matchAll(/:(\w+?)\b/g)//惰性模式下全局匹配 :开头 任意字符 空格结尾
    for(let param_info of params){
        let param_key = param_info[0]
        let param_value = bind[param_key]
        if(param_value){
            statement = statement.replace(param_key,"'"+param_value+"'")//这里要加'，所以上面要转义
        }
    }

    //用@param匹配注入参数，不加单引号
    let args = statement.matchAll(/@(\w+?)\b/g)//惰性模式下全局匹配 :开头 任意字符 空格结尾
    for(let arg_info of args){
        let arg_key = arg_info[0]
        let arg_value = bind[arg_key]
        if(arg_value){
            statement = statement.replace(arg_key,arg_value)
        }
    }

    if(CONFIG.mode=="DEBUG"){
        console.log("[Run SQL]"+statement)
    }

    return statement
}

//用于为update和insert语句生成sql字符串
const getKeys = (obj)=>{
    return Object.keys(obj).join(',')
}
const getValues = (obj)=>{
    return Object.values(obj).map((item)=>{
        item = String(item)
        item = item.replaceAll("'","''")//转义
        return "'"+item+"'"
    }).join(",")
}
const getKeyValuePairs = (obj)=>{
    const arr = []
    for(let key in obj){
        let val = String(obj[key])
        val = val.replaceAll("'","''")//转义
        arr.push(key+"='"+val+"'")
    }
    return arr.reduce((str,item)=>{
        return str+","+item
    })
}
const getValuesOfList = (items)=>{
    return items.map((item)=>{
        return "("+Object.values(item).map((prop)=>{
            return "'"+prop+"'"
        }).join(",")+")"
    }).join(",")
}

module.exports = {
    run,
    generateSQL,

    isTableExist,
    createTable,
    selectNewestId,

    getKeys,
    getValues,
    getKeyValuePairs,
    getValuesOfList
}