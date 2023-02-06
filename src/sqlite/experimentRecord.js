const {run,generateSQL,createTable,getKeys,getValues,getKeyValuePairs} = require('./common')
const Experiment = require("./experiment")
//实验数据记录模块

const TABLE_NAME = "experimentRecord"

const TABLE_INFO = {
    id:      "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL",
    experimentId:    "INTEGER NOT NULL",
    blockId:         "INTEGER NOT NULL",
    trialId:         "INTEGER NOT NULL",
    dataName:        "VARCHAR NOT NULL",
    dataType:        "VARCHAR NOT NULL",//在python获取，str int float list dict tuple bool NoneType
    dataValue:       "VARCHAR NOT NULL"
}

//插入实验记录
const record = async(info)=>{
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

//获取某人的信息
const fetchAll = async(subjects_list)=>{
    return await run(async(db)=>{
        return await db.all(
            generateSQL(
                "SELECT @targets FROM @fetcher_table INNER JOIN @selector_table ON @fetcher_table.@fetcher_joiner=@selector_table.@selector_joiner",
                {
                    "@targets":[TABLE_NAME+".*",Experiment.TABLE_NAME+".experimentName",Experiment.TABLE_NAME+".subjectId"].join(','),

                    "@fetcher_table":TABLE_NAME,
                    "@fetcher_joiner":"experimentId",

                    "@selector_table":Experiment.TABLE_NAME,
                    "@selector_joiner":"id",
                }   
            ),
        )
    })
}
const fetchBySubjectId = async(subjects_list)=>{
    return await run(async(db)=>{
        return await db.all(
            generateSQL(
                "SELECT @targets FROM @fetcher_table INNER JOIN @selector_table ON @fetcher_table.@fetcher_joiner=@selector_table.@selector_joiner WHERE @selector_table.@selector_key in (@selector_val)",
                {
                    "@targets":[TABLE_NAME+".*",Experiment.TABLE_NAME+".experimentName",Experiment.TABLE_NAME+".subjectId"].join(','),

                    "@fetcher_table":TABLE_NAME,
                    "@fetcher_joiner":"experimentId",

                    "@selector_table":Experiment.TABLE_NAME,
                    "@selector_joiner":"id",
                    "@selector_key":"subjectId",
                    "@selector_val":subjects_list
                }   
            ),
        )
    })
}


//获取某实验的信息
const fetchByExperimentName = async(experiment_name)=>{
    return await run(async(db)=>{
        return await db.all(
            generateSQL(
                "SELECT @targets FROM @fetcher_table INNER JOIN @selector_table ON @fetcher_table.@fetcher_joiner=@selector_table.@selector_joiner WHERE @selector_table.@selector_key is :selector_val",
                {
                    "@targets":[TABLE_NAME+".*",Experiment.TABLE_NAME+".experimentName",Experiment.TABLE_NAME+".subjectId"].join(','),

                    "@fetcher_table":TABLE_NAME,
                    "@fetcher_joiner":"experimentId",

                    "@selector_table":Experiment.TABLE_NAME,
                    "@selector_joiner":"id",
                    "@selector_key":"experimentName",
                    ":selector_val":experiment_name
                }   
            ),
        )
    })
}


module.exports = {
    record,
    fetchAll,
    fetchByExperimentName,
    fetchBySubjectId,

    TABLE_NAME,
    TABLE_INFO

}