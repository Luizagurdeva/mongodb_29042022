# Demo MongoDB

import pymongo

#Connect
connectstring = "mongodb+srv://luizamongo:password@cluster0.icwrc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(connectstring)

# create

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Create new document

# mycol.insert_one({"-id":101, "companyname":"Kea", "contact":"Tue"})
# mycol.insert_one({"-id":102, "companyname":"CPH Business", "contact":"Lars"})
# mycol.insert_one({"-id":103, "companyname":"ITU", "contact":"Ole"})

mycol.insert_one({"-id":104, "companyname":"Something", "contact":"Ole Rasmussen", "country":"UK"})