"""
1 - o método de classe não utiliza o primeiro parametro referente a classe.
2 - o método de classe pode acessar mas não modificar o estado da classe.
3 - usamos o decorator @staticmethod para criar um método estático
"""

class Courses:
    def __init__(self, name,trail):
        self.name = name
        self.trail = trail
        
    @staticmethod
    def courses_trail(trail):
        if trail == 'Python Fundamentos':
            courses = ['Dominando python', 'modulos e pip', 'orientação a objetos']
        elif trail == 'automação com python':
            courses = ['automação de tarefas', 'web scraping', 'assistente virtual em python']
        else:
            courses = ['A definir']
        
        return courses
            
print(Courses.courses_trail('Python Fundamentos'))
print(Courses.courses_trail('Analise de dados'))
print(Courses.courses_trail('automação com python'))