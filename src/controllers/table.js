const { isTableExist , createTable, selectNewestId } = require('../sqlite/common')

const table_subject = require("../sqlite/subject")
const table_scale = require("../sqlite/scale")
const table_scaleRecord = require("../sqlite/scaleRecord")
const table_experiment = require("../sqlite/experiment")
const table_experimentRecord = require("../sqlite/experimentRecord")
const INFO = {
    [table_subject.TABLE_NAME]    : table_subject.TABLE_INFO,
    [table_scale.TABLE_NAME]      : table_scale.TABLE_INFO,
    [table_scaleRecord.TABLE_NAME]     : table_scaleRecord.TABLE_INFO,
    [table_experiment.TABLE_NAME] : table_experiment.TABLE_INFO,
    [table_experimentRecord.TABLE_NAME] : table_experimentRecord.TABLE_INFO,
}


module.exports = {
    "exist":async function(event,table_name){
        return await isTableExist(table_name)
    },
    "create":async function(event,table_name){
        const table_info = INFO[table_name]
        return await createTable(table_name,table_info)
    },
    "latest":async function(event,table_name){
        return await selectNewestId(table_name)
    }


}