const {run,generateSQL,createTable,getKeys,getValues,getKeyValuePairs} = require('./common')

//行为量表模块

const TABLE_NAME = "scale"

const TABLE_INFO = {
    id:      "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL",
    scaleName:      "VARCHAR NOT NULL",
    subjectId:      "INTEGER NOT NULL",//这个量表测的是哪个被试的数据，用来筛选
    createdAt:      "DATETIME DEFAULT (datetime('now','localtime')) NOT NULL"//有些实验可能要求对同一被试每隔若干天实验一次，每次填写量表，因此需要日期区分
}


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