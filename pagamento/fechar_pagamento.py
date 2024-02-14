from Escolha_dos_produtos.escolha import soma_das_compras, sacola
from time import sleep


def pagar_compra():
    print(soma_das_compras(sacola))
    print("Escolha sua forma de pagamento:")
    print("Digite 1 para pagar com cartão de débito")
    print("Digite 2 para pagar em dinheiro")
    print("Digite 3 para pagar com cartão de crédito")
  
    while True:
        try:
            forma_de_pagamento = int(input("Digite a forma de pagamento: "))
        except ValueError:
            print("Escolha uma das opções sugeridas 1, 2 ou 3. ")
            
        else:
            if forma_de_pagamento in (1, 2, 3):
                break
            else:
                print("Escolha uma das opções sugeridas 1, 2 ou 3. ")

    if forma_de_pagamento == 1:
        print("Você escolheu pagar com cartão de débito.")
        print("Sendo calculado o desconto de 5%...")
        sleep(2)
        print(f"Sua compra de R$ {sum(sacola.values()):.2f}, com o desconto de 5% ficou R$ {sum(sacola.values()) * 0.95:.2f}")
        sleep(1)
        print("Insira ou aproxime o cartão")
        print("Aguarde...")
        sleep(2)
        senha = input("Digite sua senha:")
        print("Processando...")
        sleep(3)
        print("Pagamento aprovado!")

    elif forma_de_pagamento == 2:
        print("Você escolheu pagar em dinheiro.")
        print("Sendo calculado o desconto de 5% para pagamento em dinheiro...")
        sleep(2)
        print(f"Sua compra de R$ {sum(sacola.values()):.2f}, com o desconto de 5% ficou R$ {sum(sacola.values()) * 0.95:.2f}")
        sleep(1)
        print("Pegue seu troco!")

    elif forma_de_pagamento == 3:
        print("Você escolheu pagar com cartão de crédito.")
        print(f"Sua compra foi de R$ {sum(sacola.values()):.2f}")
        sleep(1)
        print("Insira ou aproxime o cartão")
        print("Aguarde...")
        senha = input("Digite sua senha:")
        print("Processando...")
        sleep(3)
        print("Pagamento aprovado!")

    