const { getListByName, getAll, getInfoById, getInfoByName, editInfoById, insertInfo, isNameExist} = require('../sqlite/subject')


module.exports = {
    "exist":async function(event,name){
        return await isNameExist(name)
    },
    "find":async function(event,id){
        return await getInfoById(id)
    },
    "match":async function(event,name){
        return await getListByName(name)
    },
    "search":async function(event,name){
        return await getInfoByName(name)
    },
    "insert":async function(event,info){
        return await insertInfo(info)
    },
    "edit":async function(event,info){
        return await editInfoById(info)
    },
    "all":async function(event){
        return await getAll()
    }


}