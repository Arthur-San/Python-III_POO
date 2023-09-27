class Animal:
    name = ''
    size = ''
    color = ''
    
    def eat(self):
        print('animal comendo')
        
class Horse(Animal):
    race = ''
    
    def escape(self):
        print('Cavalo fugindo')

class Lion(Animal):
    mane = True
    
    def hunting(self):
        print('leao caçando')
        
h = Horse()

h.name = 'Pé de pano'
h.color = 'branco'
h.escape()
h.eat()

l = Lion()
l.name = 'simba'
l.color = 'azul'
l.hunting()
l.eat()