class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        

class Fish(Animal):
    race = ''
    
class Parrots(Animal):
    color = ''
    
class Zoo:
    def __init__(self):
        self.animals_dicts = {}
        
    def add_animal(self, animal):
        self.animals_dicts[animal.name] = animal.category
        
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dicts.values():
            if animal == category:
                result += 1
        return f"No Zoológico temos: {result} quantidade de {category}"
    
zoo = Zoo()

peixe = Fish('nemo', 'ovíparos')
peixe2 = Fish('sicrano', 'ovíparos') #adicionando mais um para contagem ovíparos
papagaio = Parrots('Louro josé', 'aves')
print(vars(peixe))
print(vars(papagaio)) 
zoo.add_animal(peixe)
zoo.add_animal(peixe2)
zoo.add_animal(papagaio)
print(zoo.total_of_category('aves'))
print(zoo.total_of_category('ovíparos'))