## Classe Produto e método desconto

# Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

# 1. Cada produto deve ter um preço e um nome.

# 2. A classe deve ter um método construtor e o método dundle str.

# 3. A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.

import os

os.system('cls')

class Produto:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"-----PRODUTO-----\nDescrição: {self.descricao}\nPreço: {self.preco}" 


    def desconto(self, desc):
        print(f"Desconto de {desc}% aplicado!")
        desc /= 100
        valorDesc = self.preco * desc
        print(f"O desconto é de R$ {valorDesc:.2f}")
        self.preco -= valorDesc



produto = Produto("Refrigerante", 3.5)
print(f"preço antes desconto")
print(produto)

print("----------------------------------------------")

print(f"preço com desconto")
produto.desconto(int(input('Qual o valor do desconto?')))
print(produto)