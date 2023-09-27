from exercicio3 import Viagem

viagem0 = Viagem('Alemanha')
viagem1 = Viagem('Paris')
viagem2 = Viagem('Japão')

list_viagens = [viagem0, viagem1, viagem2]



viajante = input('Digite o seu nome: ')

print('Viagens disponíveis')
print(f"temos {len(list_viagens)} destinos para vc"
'''
[0] - Alemanha
[1] - Paris
[2] - Japão
'''      
)

escolha = int(input('Selecione um destino: '))

for opcao in list_viagens:
    if escolha > len(list_viagens):
        print('Opção não disponível!')
        break
    else:
        print(f"{viajante} sua viagem para {list_viagens[escolha]} está marcada!")
        break


