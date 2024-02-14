from Escolha_dos_produtos.escolha import mostra_todos_produtos, escolhe_produto, mostra_sacola, sacola, produtos, soma_das_compras
from pagamento.fechar_pagamento import pagar_compra
from time import sleep
from datetime import datetime


data_atual = datetime.today()

def opcao1():
    print(f"Abaixo nossa lista atualizada de frutas para o dia de hoje {data_atual.strftime('%d-%m-%Y')}")
    print(mostra_todos_produtos())
    continua_comprando = 1
    while True:
        if continua_comprando == 1:
            while True:
                try:
                    id_produto = int(input("Digite o numero do produto para por na sacola: "))
                except ValueError:
                    print(f"Digite uma opção entre 1 e {len(produtos)}")
                else:
                    if 1 <= id_produto <= len(produtos) + 1:
                        break
                    else:
                        print(f"Digite uma opção entre 1 e {len(produtos)}")
            escolhe_produto(id_produto)
            while True:
                    try:
                        continua_comprando = int(input("Deseja continuar comprando? Digite 1 para 'SIM', 2 para ir para o pagamento e 3 para mostrar a sacola"))
                    except ValueError:
                        print("Escolha uma das opções sugeridas 1, 2 ou 3. ")
                      
                    else:
                        if continua_comprando in (1, 2, 3):
                            break
                        else:
                            print("Escolha uma das opções sugeridas 1, 2 ou 3. ")
            
            if continua_comprando == 3:
                mostra_sacola(sacola)
                
                while True:
                    try:
                        continua_comprando = int(input("Deseja continuar comprando? Digite 1 para 'SIM' e 2 para ir para o pagamento"))
                    except ValueError:
                        print("Escolha uma das opções sugeridas 1 ou 2. ")
                      
                    else:
                        if continua_comprando in (1, 2):
                            break
                        else:
                            print("Escolha uma das opções sugeridas 1 ou 2. ")

            # else:
            #     continua_comprando = opcao2
        elif continua_comprando == 2:
            print("Agora vamos escolher a forma de pagamento!")
            print(soma_das_compras(sacola))
            print("Digite 1 para pagar")
            print("Digite 2 para voltar às compras")
            while True:
                    try:
                        escolha = int(input("Digite sua opção: "))
                    except ValueError:
                        print("Escolha uma das opções sugeridas 1 ou 2. ")
                      
                    else:
                        if escolha in (1, 2):
                            break
                        else:
                            print("Escolha uma das opções sugeridas 1 ou 2. ")
            
            if escolha == 2:
                continua_comprando = 3
                mostra_sacola(sacola)
                
                while True:
                    try:
                        continua_comprando = int(input("Deseja continuar comprando? Digite 1 para 'SIM' e 2 para ir para o pagamento"))
                    except ValueError:
                        print("Escolha uma das opções sugeridas 1 ou 2. ")
                      
                    else:
                        if continua_comprando in (1, 2):
                            break
                        else:
                            print("Escolha uma das opções sugeridas 1 ou 2. ")
            elif escolha == 1:
                pagar_compra()
                break