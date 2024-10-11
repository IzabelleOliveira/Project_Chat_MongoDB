from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding

output_format = "b64"
iv_parameter = "0011223344556677"


def cifrar_mensagem(key, message):
    try:
        cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
        return cipher.encrypt(message)
    except ValueError as e:
        print(f"Erro na chave de criptografia")
        return None


def decifrar_mensagem(key, encrypted_message):
    try:
        cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
        return cipher.decrypt(encrypted_message)
    except ValueError as e:
        print(f"Erro na chave de descriptografia")
        return None
