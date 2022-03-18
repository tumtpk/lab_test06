import bson
from pymongo import MongoClient
import sys  
import os      
sys.path.insert(0, '../lab_test06') 

from config import database


path = 'backups/'


def dump(collections):
    # """
    # MongoDB Dump

    # :param collections: Database collections name
    # :param conn: MongoDB client connection
    # :param db_name: Database name
    # :param path:
    # :return:
    
    # >>> DB_BACKUP_DIR = '/path/backups/'
    # >>> conn = MongoClient("mongodb://admin:admin@127.0.0.1:27017", authSource="admin")
    # >>> db_name = 'my_db'
    # >>> collections = ['collection_name', 'collection_name1', 'collection_name2']
    # >>> dump(collections, conn, db_name, DB_BACKUP_DIR)
    # """

    db = database.db
    for coll in collections:
        with open(os.path.join(path, f'{coll}.bson'), 'wb+') as f:
            for doc in db[coll].find():
                f.write(bson.BSON.encode(doc))


def restore():
    # """
    # MongoDB Restore

    # :param path: Database dumped path
    # :param conn: MongoDB client connection
    # :param db_name: Database name
    # :return:
    
    # >>> DB_BACKUP_DIR = '/path/backups/'
    # >>> conn = MongoClient("mongodb://admin:admin@127.0.0.1:27017", authSource="admin")
    # >>> db_name = 'my_db'
    # >>> restore(DB_BACKUP_DIR, conn, db_name)
    
    # """
    
    db = database.db
    for coll in os.listdir(path):
        if coll.endswith('.bson'):
            with open(os.path.join(path, coll), 'rb+') as f:
                db[coll.split('.')[0]].delete_many({})
                db[coll.split('.')[0]].insert_many(bson.decode_all(f.read()))