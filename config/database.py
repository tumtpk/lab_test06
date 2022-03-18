from pymongo import MongoClient
import ssl
from core import config

ssl._create_default_https_context = ssl._create_unverified_context



client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/myFirstDatabase?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

db = client.todo_app

students_collection = db["students"]
collection_name = db["todos_app"]
