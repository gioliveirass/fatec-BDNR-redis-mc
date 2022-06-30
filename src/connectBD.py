from pymongo import MongoClient
import redis

def connectRedis():
    myRedis = redis.Redis(
    host='<endpoint público>',
    port='<porta>', # Deve ser um number
    password='<password>')
    return myRedis

def connectMongo():
    client = MongoClient("mongodb+srv://<user>:<password>@<url>")
    mydb = client.MercadoLivre
    return mydb