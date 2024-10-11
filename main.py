from databases.mongoHandler import MongoHandler
from criptography.crypto import *
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
            ver_mensagens(handler, nickname)
        elif opcao == 2:
            enviar_mensagens(handler, nickname)
        elif opcao == 3:
            print("Sair...")
            break
        else:
            print("opção inválida")


def ver_mensagens(handler, nickname_to):
    mensagens = handler.getMessages(nickname_to)

    if mensagens:
        print(f"Mensagens Recebidas por: {nickname_to}")

        mensagens_agrupadas = {}
        for mensagem in mensagens:
            remetente = mensagem['nickname_from']
            if remetente not in mensagens_agrupadas:
                mensagens_agrupadas[remetente] = []
            mensagens_agrupadas[remetente].append(mensagem['message'])

        for i, remetente in enumerate(mensagens_agrupadas.keys(), 1):
            print(f"{i} -> {remetente}")

        try:
            opcao = int(input("Escolha o remetente para ver as mensagens: "))
            remetente_escolhido = list(mensagens_agrupadas.keys())[opcao - 1]
            print(f"\nMensagens de {remetente_escolhido}:")

            chave_simetrica = input(f"Digite a chave de criptografia para mensagens de {remetente_escolhido}: ")

            for mensagem in mensagens_agrupadas[remetente_escolhido]:
                try:
                    mensagem_decifrada = decifrar_mensagem(chave_simetrica, mensagem)
                    print(f"Mensagem: {mensagem_decifrada}")
                except Exception as e:
                    print(f"Erro ao decifrar mensagem: {e}")
        except (IndexError, ValueError):
            print("Opção inválida. Tente novamente.")
    else:
        print("Nenhuma mensagem encontrada.")


def enviar_mensagens(handler, nickname_from):
    nickname_to = input("Digite o nome do destinatário: ")
    mensagem = input("Digite sua mensagem: ")

    chave_simetrica = input("Digite a chave de criptografia compartilhada: ")

    try:
        mensagem_cifrada = cifrar_mensagem(chave_simetrica, mensagem)

        if mensagem_cifrada:
            handler.saveMessage(nickname_from, nickname_to, mensagem_cifrada)
            print("Mensagem enviada e criptografada com sucesso!")
    except ValueError as e:
        print(f"Erro na chave de criptografia: {e}")
    except Exception as e:
        print(f"Erro inesperado ao criptografar a mensagem: {e}")


if __name__ == '__main__':
    print("----CHAT BOT----")
    login()
