"""
1 - o método de classe utiliza o primeiro parametro referente a classe.
2 - o método de classe podeacessar ou modificar o estado da classe.
3 - usamos o decorator @classmethod para criar um método de classe
"""

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))
    
wiiu = Console.from_text("meu video game é wiiu e o preço é 1000 reais")
xbox = Console.from_text("meu video game é xbox e o preço é 2000 reais")

print(wiiu.__dict__)
print(xbox.__dict__)