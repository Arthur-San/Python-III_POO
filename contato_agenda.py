# 2. Ter uma classe ContactBook contendo quatro métodos:
#     1. Um método para adicionar contato.
#     2. Um método para listar contatos.
#     3. Um método para buscar contatos.
#     4. Um método para remover contatos.

class ContactBook:
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def display_contact(self):
        if not self.contacts:
            print('lista de contatos está vazia!')
        else:
            for x in self.contacts:
                print(x)
                print('--------------------')

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"\nEncontrado! \n\n{contact}")
                return contact
            
        print(f"\ncontato {name} não foi encontrado!")
