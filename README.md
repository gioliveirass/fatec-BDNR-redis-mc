<h1 align="center"> Manipulação de documentos Chave-Valor no Redis utilizando Python </h1>

<p align="center"> 
<a href="#sobre"> Sobre o projeto </a> • <a href="#tecnologias"> Tecnologias utilizadas </a> • <a href="#comoRodar"> Como rodar o projeto </a> • <a href="#doc"> Documentação das coleções </a> • <a href="#resultados"> Resultados </a>
</p>

## <a id="sobre"> 🎲 Sobre o projeto </a>

Atividade desenvolvida durante a aula de Banco de Dados Não Relacional da Fatec, que consiste em armazenar no Redis certas coleções desenvolvidas com MongoDB na [atividade de modelagem com MongoDB](https://github.com/gioliveirass/fatec-BDNR-MercadoLivre). Também é válido desenvolver novas funcionalidades.

## <a id="tecnologias"> 🎲 Tecnologias utilizadas </a>

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)

## <a id="comoRodar"> 🎲 Como rodar o projeto </a>

Antes de tudo, baixe as dependências do projeto com o comando `pip install -r requirements.txt`.

Para autenticar com o banco de dados, certifique-se de adicionar os dados corretos do banco de dados em `src/connectBD.py`.

Uma vez que os dados estiverem corretos, execute o arquivo `src/main.py`.

## <a id="resultados"> 🎲 Documentação das coleções </a>

<details>
  <summary>Carrinho de compras</summary>
  <br>
  <table>
    <tr>
      <th>Chave</th>
      <th>Valor</th>
    </tr>
    <tr>
      <td>carrinho:{nomeDoUsuario}</td>
      <td>{"produtos": [{"nome": {nomeDoProduto}, "preco": {precoDoProduto}}]}</td>
    </tr>
  </table>
</details>

## <a id="resultados"> 🎲 Resultados </a>

<details>
  <summary>Carrinho de compras</summary>
  <br>
  <p>Resultados obtidos após executar as funções do arquivo <a href="https://github.com/gioliveirass/fatec-BDNR-redis-ml/blob/main/src/controllers/cartController.py">cartController.py</a>:</p>
  <p><img src = ".github\result.PNG" alt = "Deleção de um usuário" width = 600 /></p>
</details>

