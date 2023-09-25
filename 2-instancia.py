class Movie:
    name = ""
    yearLauch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0
    

# Primeiro filme
movie = Movie()
movie.name = 'Super mario'
movie.yearLauch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130

print(f"Dados do filme:")
print(f"Nome do filme: {movie.name}\nAno de Lançamento: {movie.yearLauch}\n")

# Segundo filme
filme2 = Movie()

filme2.name = 'Five Nigths'
filme2.yearLauch = 2023
filme2.includedPlan =  True
filme2.note = 4.7
filme2.durationMinutes = 137

print(f"Dados do filme:")
print(f"Nome do filme: {filme2.name}\nAno de Lançamento: {filme2.yearLauch}\n")



