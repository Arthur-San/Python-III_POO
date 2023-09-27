class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Nome: {self.name} - Salário R$ {self.__salary}")
        
fulano = Employee("Teste", 1400)

fulano.__salary = 10000

fulano.show()
        
