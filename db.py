from flask import Flask
from flask_pymongo import pymongo

from app import app

CONNECTION_STRING = "mongodb+srv://izhak:a1234567@cluster0.5itd8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('portfolioDB')
user_collection = pymongo.collection.Collection(db, 'collection')