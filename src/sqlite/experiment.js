const {run,generateSQL,createTable,getKeys,getValues,getKeyValuePairs} = require('./common')

//实验信息管理模块

const TABLE_NAME = "experiment"

const TABLE_INFO = {
    id:      "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL",
    subjectId:       "INTEGER NOT NULL",
    experimentName:  "VARCHAR NOT NULL",//用来记录当前在做的是哪种实验
    createdAt:       "DATETIME DEFAULT (datetime('now','localtime')) NOT NULL"
}

//插入某人的信息
const create = async(info)=>{
    return await run(async(db)=>{
        return await db.run(
            generateSQL(
                "INSERT INTO @table_name(@table_keys) VALUES(@table_values)",
                {
                    "@table_keys":getKeys(info),
                    "@table_values":getValues(info),
                    "@table_name":TABLE_NAME,
                }   
            ),
        )
    })
}


module.exports = {
    create,

    TABLE_NAME,
    TABLE_INFO

}