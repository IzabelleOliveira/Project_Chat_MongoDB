from databases.mongoHandler import MongoHandler
from databases.entities import User,Message
from pymongo import MongoClient

def login():
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    mail = input('Digite seu email: ')

    handler = MongoHandler()
    auth = handler.authenticate(nickname=usuario, password=senha, email=mail)

    if auth:
        print("Login bem-sucedido!")
        menu(nickname=usuario)
    else:
        print("Dados inválidos ou não cadastrados.")


def menu(nickname):
    while True:
        handler = MongoHandler()
        print('--------------MENU-------------')
        print('----- Bem Vindo - Opções:------------')
        print(' 1 -> Mensagens Recebidas')
        print(' 2 -> Enviar Mensagens')
        print(' 3 -> Sair')
        opcao = int(input('OPÇÃO:'))

        if opcao == 1:
            verMensagens(handler,nickname)
        elif opcao == 2:
            print("...")
        elif opcao == 3:
            print("Sair...")
            break
        else:
            print("opção inválida")


def verMensagens(handler, nickname_to):
    mensagens = handler.getMessages(nickname_to)
    if mensagens:
        print(f"Mensagens Recebida por: {nickname_to}")
        for mensagen in mensagens:
            print(f"De: {mensagen['nickname_from']}")
            print(f"Mensagem: {mensagen['message']}")
    else:
        print("Nenhuma mensagem encontrada.")

#def enviarMensagens():


if __name__ == '__main__':
    print("----CHAT BOT----")
    login()

