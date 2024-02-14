from Opcoes.menu import opcao1
from time import sleep

from Escolha_dos_produtos.escolha import mostra_sacola, sacola, gera_arquivo_csv, produtos


print("Bom dia, você está no sacolão do Sebastião!!")
print("Opções: ")
print("Para listar todos nossos produtos de hortifruti, digite 1")
print("Para listar todos nossos produtos de limpeza, digite 2")
print("Para listar todos nossos produtos de açougue, digite 3")
print("Para listar todos nossos produtos de padaria, digite 4")

while True:
    try:
        opcao = int(input("Digite a sua opção: "))

        if opcao == 1:
            opcao1()
            break
            

        if opcao in (2, 3, 4):
            sleep(1)
            print("Opção em construção...você será redirecionado para a seção de hortifruti...")
            opcao1()
            sleep(1)
            break

    except ValueError as e:
        print(f"Digite uma opção válida")

gera_arquivo_csv(sacola)
print("Obrigado pela escolha!!")



