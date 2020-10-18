from pymongo import MongoClient

client = MongoClient("mongodb://root:example@0.0.0.0:57017")
print(client)
database_names = client.list_database_names()
print(database_names)
# DB接続(存在しない場合は作成)
db = client["sampledb"]
# collection接続(存在しない場合は作成)
collection = db["test_collection"]

# # 1件登録
collection.insert_one({"name": "TestA", "age": 100})
# # collection.insert_one({"name": "TestB", "age": 200})
# # collection.insert_one({"name": "TestC", "age": 300})

client.close()