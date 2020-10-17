from pymongo import MongoClient
import datetime

client = MongoClient('localhost','27017')

db = client('Mydb') # Mydb is the database or  another syntax is client.Mydb
users = db.users  # users is the collection
user1 = {'usename':'cedric', 'password':'donsavinero', 'favorite_numbers':123, 'hobbies':['python','java']}

user_id = users.insert_one(user1).inserted_id

# bulk insertion
many_users = [{'username':'don','password':123},{'username':'zed','password':'die'}]
inserted = users.insert_many(many_users)
print(inserted.inserted_ids)

# counting documents
users.find().count()
users.find({'username':'don'}).count()

# multiple find
users.find({'username':'don','password':'don'}).count()

# datetime
current_date = datetime.datetime.now()
old_date = datetime.datetime(2009,11,24)
uid = users.insert({'username':'cedric','date':current_date})
users.find({'date':{'$gte':old_date}}).count()
users.find({'date':{'$tte':old_date}}).count()
users.find({'date':{'$exists':True}}).count()
users.find({'username':{'$ne':'cedric'}}).count()

# how to create index
db.users.create_index([{"username", pymongo.ASCENDING}], unique=True)
users.find({'username':'cedric'})