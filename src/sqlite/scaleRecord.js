const {run,generateSQL,createTable,getKeys,getValues,getKeyValuePairs, getValuesOfList} = require('./common')
const Scale = require("./scale")
//量表数据记录模块

const TABLE_NAME = "scaleRecord"

const TABLE_INFO = {
    id:      "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL",
    scaleId:    "INTEGER NOT NULL",
    question:       "VARCHAR NOT NULL",//为什么要把question包含在表里？看似是冗余了，但保不齐量表可能会修改，那样的话之前的数据就无法导出了
    answer:         "VARCHAR NOT NULL",//同上，刻意做的冗余
    score:          "INT NOT NULL",//原始数据，所选选项对应的分值
}

//插入量表记录
const submit = async(items)=>{
    if(!(items instanceof Array)){
        items = [items]
    }
    return await run(async(db)=>{
        return await db.run(
            generateSQL(
                "INSERT INTO @table_name(@table_keys) VALUES @table_values",
                {
                    "@table_keys":getKeys(items[0]),
                    "@table_values":getValuesOfList(items),
                    "@table_name":TABLE_NAME,
                }   
            ),
        )
    })
}


const fetchAll = async(subjects_list)=>{
    return await run(async(db)=>{
        return await db.all(
            generateSQL(
                "SELECT @targets FROM @fetcher_table INNER JOIN @selector_table ON @fetcher_table.@fetcher_joiner=@selector_table.@selector_joiner",
                {
                    "@targets":[Scale.TABLE_NAME+".scaleName",Scale.TABLE_NAME+".subjectId",TABLE_NAME+".scaleId",TABLE_NAME+".question",TABLE_NAME+".answer",TABLE_NAME+".score",Scale.TABLE_NAME+".createdAt"].join(','),

                    "@fetcher_table":TABLE_NAME,
                    "@fetcher_joiner":"scaleId",

                    "@selector_table":Scale.TABLE_NAME,
                    "@selector_joiner":"id",
                }   
            ),
        )
    })
}
//获取某人的信息
const fetchBySubjectId = async(subjects_list)=>{
    return await run(async(db)=>{
        return await db.all(
            generateSQL(
                "SELECT @targets FROM @fetcher_table INNER JOIN @selector_table ON @fetcher_table.@fetcher_joiner=@selector_table.@selector_joiner WHERE @selector_table.@selector_key in (@selector_val)",
                {
                    "@targets":[Scale.TABLE_NAME+".scaleName",Scale.TABLE_NAME+".subjectId",TABLE_NAME+".scaleId",TABLE_NAME+".question",TABLE_NAME+".answer",TABLE_NAME+".score",Scale.TABLE_NAME+".createdAt"].join(','),

                    "@fetcher_table":TABLE_NAME,
                    "@fetcher_joiner":"scaleId",

                    "@selector_table":Scale.TABLE_NAME,
                    "@selector_joiner":"id",
                    "@selector_key":"subjectId",
                    "@selector_val":subjects_list
                }   
            ),
        )
    })
}

module.exports = {
    submit,
    fetchAll,
    fetchBySubjectId,

    TABLE_NAME,
    TABLE_INFO

}