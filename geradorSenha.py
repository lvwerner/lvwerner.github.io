import random
import string

def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

comprimento_da_senha = int(input("Digite o comprimento da senha desejada: "))
senha_gerada = gerar_senha(comprimento_da_senha)
print("Senha gerada:", senha_gerada)
