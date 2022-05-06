import controllers.cartController as cartController

# CARRINHO DE COMPRAS
cartController.insert('gio', '[{"nome": "Condicionador", "preco": "R$30.00"}]')
cartController.findCart('gio')
cartController.deleteCart('gio')
cartController.findCart('gio')