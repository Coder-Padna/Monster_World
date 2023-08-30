import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["monster_world_database"]
