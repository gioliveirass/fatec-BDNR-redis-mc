import redis

def connect():
    myRedis = redis.Redis(
    host='<endpoint público>',
    port='<porta>', # Deve ser um number
    password='<password>')
    return myRedis