class Movie:
    def __init__(self, name, lancamento, inclusoPlano, nota, duracaoMinutos): #CONSTRUTOR
        self.name = name
        self.lancamento = lancamento
        self.inclusoPlano = inclusoPlano
        self.nota = nota
        self.duracaoMinutos = duracaoMinutos
        
    def __str__(self): #TOSTRING
        return f"Filme: {self.name}\nLançamento: {self.lancamento}\nOn Streaming: {self.inclusoPlano}\nNota: {self.nota}\nDuração: {self.duracaoMinutos}"
    
    def technical_sheet(self):
            print("####Dados do Filme####")
            print(f"Nome Filme: {self.name}")
            print(f"Ano Lançamento: {self.yearLaunch}")
            print(f"Está no plano? {self.includedPlan}")
            print(f"Avaliação Filme: {self.note}")
            print(f"Duração Filme: {self.durationMinutes}")
        
        
movie = Movie("Sonic", 2023, False, 4.6, 124 )

print(movie)