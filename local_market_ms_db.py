from pymongo import MongoClient
from bson.objectid import ObjectId

global con
global db
global col_places

def configure_db():
    global con
    global db
    global col_places

    con = MongoClient('mongodb+srv://graduate_proj:proj1234@clustercollegems.7keiz.mongodb.net/localMarketMS_db?retryWrites=true&w=majority')
    db = con.localMarketMS_db
    col_places = db.student_registration_info

def save_data(data):
    global col_places
    configure_db()

    col_places.insert_one(data)
    return