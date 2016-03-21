#!/usr/bin/python


import random
import pymongo
conn = pymongo.Connection("127.0.0.1",27017)
db = conn.tage #连接库tage
#db.authenticate("tage","123") #用户认证
db.test.drop() #删除集合user
db.test.save({'id':1,'name':'kaka','sex':'male'}) #插入一个数据

for id in range(2,10):
    name = random.choice(['steve','koby','owen','tody','rony'])
    sex = random.choice(['male','female'])
    db.test.insert({'id':id,'name':name,'sex':sex}) 
#通过循环插入一组数据
content = db.test.find()
#打印所有数据
for i in content:
    print i

