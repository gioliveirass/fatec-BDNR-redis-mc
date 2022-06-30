import controllers.cartController as cartController

# CARRINHO DE COMPRAS
mongoData = cartController.getDataFromMongo()

for data in mongoData:
    cartController.insert(data["cpf"], data["cart"])

cartController.findCart('111.111.111-11')
cartController.deleteCart('111.111.111-11')
cartController.findCart('111.111.111-11')