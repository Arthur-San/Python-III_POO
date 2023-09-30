## Agenda de Contatos

# Desenvolva uma agenda de contatos utilizando Programação Orientada a Objetos. O programa deve seguir as especificidades:

# 1. Ter uma classe Contact contendo os atributos: name, phone e email

# 2. Ter uma classe ContactBook contendo quatro métodos:
#     1. Um método para adicionar contato.
#     2. Um método para listar contatos.
#     3. Um método para buscar contatos.
#     4. Um método para remover contatos.

# 3. Criar um arquivo principal para a aplicação que deve instanciar as duas classes criadas anteriormente e desenvolver e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.

from contato import Contact
from contato_agenda import ContactBook

contato_agenda = ContactBook()

while True:
    print('\n--------OPÇÕES AGENDA DE CONTATOS----')
    print('1 - Adicionar Contato')
    print('2 - Remover Contato')
    print('3 - Listar Contatos')
    print('4 - Buscar Contato')
    print('5 - Sair')

    choice = int(input('Escolha uma opção:\n->'))

    if choice == 1:
        print('----------ADICIONANDO CONTATO----------')
        name = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')

        contact = Contact(name, telefone, email)
        contato_agenda.addContact(contact)
        print(f"Contato adicionado!")

    elif choice == 2:
        print('----------REMOVENDO CONTATO----------')
        name = input('informe o nome para remover: ')
        contact = contato_agenda.search_contact(name)
        if contact:
            choice = input('\nDeseja remover este contato? [S/N]\n->')
            if choice == 's' or choice == 'S':
                contato_agenda.remove_contact(contact)
                print(f"Contato Removido!")
            else:
                print('Voltando para o menu!')
    elif choice == 3:
        print('----------LISTANDO CONTATOS----------')
        contato_agenda.display_contact()

    elif choice == 4:
        print('----------BUSCANDO CONTATO----------')
        name = input('informe o nome para consultar: ')
        contact = contato_agenda.search_contact(name)
    
    elif choice == 5:
        break

    else:
        print('opção inválida!')






    
        


