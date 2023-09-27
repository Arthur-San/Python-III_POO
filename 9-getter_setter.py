class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Nome: {self.name} - Salário R$ {self.__salary}")
        
    # método para buscar dados
    def get_salary(self):
        return self.__salary
    
    #método para modificar atributo privado
    def set_salary(self, salary):
        self.__salary = salary
        
fulano = Employee('fulano', 2000)
siclano = Employee('siclano', 6000)

fulano.show()
siclano.show()

fulano.set_salary(3000)
fulano.show()