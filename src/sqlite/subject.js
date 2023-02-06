const {run,generateSQL,createTable,getKeys,getValues,getKeyValuePairs} = require('./common')

//被试信息管理模块

const TABLE_NAME = "subject"

const TABLE_INFO = {
    id:      "INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL",
    name:    "VARCHAR NOT NULL",
    gender:  "CHAR    NOT NULL",
    age:     "INTEGER NOT NULL",
    contact: "VARCHAR NOT NULL",
    createdAt:"DATETIME DEFAULT (datetime('now','localtime')) NOT NULL"
}

const getAll = async()=>{
    return await run(async(db)=>{
        return await db.all(
            generateSQL(
                "SELECT * FROM @table_name",
                {
                    "@table_name":TABLE_NAME
                }
            )
        )
    })
}

//用于模糊查询，名字输入一半就能返回相似的以供选择
const getListByName = async(name)=>{
    return await run(async(db)=>{
        return await db.all(
            generateSQL(
                "SELECT * FROM @table_name WHERE @search_key LIKE :search_value",
                {
                    "@table_name":TABLE_NAME,
                    "@search_key":"name",
                    ":search_value":name+"%"
                }
            )
        )
    })
}

//具体查询某个人的信息
const getInfoById = async(id)=>{
    return await run(async(db)=>{
        return await db.get(
            generateSQL(
                "SELECT * FROM @table_name WHERE id=:id",
                {
                    "@table_name":TABLE_NAME,
                    ":id":id
                }
            )
        )
    })
}
const getInfoByName = async(name)=>{
    return await run(async(db)=>{
        return await db.get(
            generateSQL(
                "SELECT * FROM @able_name WHERE @search_key=:search_value",
                {
                    "@table_name":TABLE_NAME,
                    "@search_key":"name",
                    ":search_value":name
                }
            )
        )
    })
}

//更新某人的信息
const editInfoById = async(info)=>{
    return await run(async(db)=>{
        return await db.run(
            generateSQL(
                "UPDATE @table_name SET @update_str WHERE id=:subject_id",
                {
                    "@update_str":getKeyValuePairs(info),
                    "@table_name":TABLE_NAME,
                    ":subject_id":info.id
                }
            )
        )
    })
}

//插入某人的信息
const insertInfo = async(info)=>{
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


//重名判断
const isNameExist = async(name)=>{
    return (
        await run(async(db)=>{
            return await db.get(
                generateSQL(
                    "SELECT count(*) as count FROM @table_name WHERE name=:name",
                    {
                        "@table_name":TABLE_NAME,
                        ":name":name
                    }
                )
            )
        })
    ).count > 0
}




module.exports = {
    getAll,
    getListByName,
    
    getInfoById,
    getInfoByName,
    isNameExist,

    editInfoById,
    insertInfo,

    TABLE_NAME,
    TABLE_INFO

}