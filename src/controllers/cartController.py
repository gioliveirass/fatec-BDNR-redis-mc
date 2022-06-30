import connectBD as connectDB
from pprint import pprint
import simplejson as json
from bson import json_util

def getDataFromMongo(): 
    mydb = connectDB.connectMongo()
    mycol = mydb.usuario
    results = mycol.find()
    resultsJson = []
    for result in results:
        resultsJson.append(json.loads(json_util.dumps({"cpf": result["cpf"], "cart" : result["carrinho"]})))
    return resultsJson


def insert(userCpf, product):
    myRedis = connectDB.connectRedis()
    key = f'carrinho:{userCpf}' 
    value = {f'"produtos": {product}'}
    myRedis.set(key, f'{value}')
    pprint('== INSERÇÃO DE CARRINHO ==')
    pprint('Carrinho inserido com sucesso!')
    pprint(myRedis.get(key))
    print('\n')

def findCart(userCpf):
    myRedis = connectDB.connectRedis()
    key = f'carrinho:{userCpf}' 
    carts = myRedis.get(key)
    pprint(f'== CARRINHOS DE {userCpf.upper()} ==')
    pprint(carts)
    print('\n')

def deleteCart(userCpf):
    myRedis = connectDB.connectRedis()
    key = f'carrinho:{userCpf}' 
    myRedis.delete(key)
    pprint(f'== DELETAR CARRINHO ==')
    pprint('Carrinho deletado com sucesso!')
    print('\n')