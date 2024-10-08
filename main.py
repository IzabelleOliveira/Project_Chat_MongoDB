from databases.mongoHandler import MongoHandler
from databases.entities import User
from pymongo import MongoClient

def menu():
    print('--------------MENU------------')
    print('----- Bem vindo - Opções:------------')
    print(' 1 -> Ver Mensagens')
    print(' 2 -> Enviar Mensagens')
    print(' 3 -> Sair')
    opção = int(input('OPÇÃO:'))

def login():
    usuario = (input('Digite seu nome de usúario: '))
    senha = (input('Digite sua senha: '))
    mail = (input('Digite seu email: '))
    handler = MongoHandler()
    auth = handler.authenticate(nickname= usuario, password= senha, email= mail)
    if auth:
        return menu()
    else:
        print("Dados inválidos ou não cadastrados.")


#chamar função de login - auth
#chamar funçao menu
if __name__ == '__main__':
    print("----CHAT BOT----")
    login()
