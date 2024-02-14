import csv

produtos = [
    ['Banana', 10.31], ['Maçã', 8.54], ['Uva', 12.17], ['Abacaxi', 13.92], ['Morango', 7.69],
    ['Pera', 9.12], ['Manga', 11.84], ['Melancia', 5.72], ['Kiwi', 14.23], ['Pêssego', 6.45],
    ['Cereja', 8.76], ['Abacate', 13.45], ['Laranja', 6.98], ['Limão', 14.61], ['Coco', 11.07],
    ['Goiaba', 7.38], ['Papaya', 10.89], ['Caju', 8.23], ['Ameixa', 6.17], ['Maracujá', 13.01],
    ['Pitaya', 12.48], ['Figo', 9.76], ['Melão', 5.42], ['Jabuticaba', 14.79], ['Romã', 5.91],
    ['Açaí', 12.65], ['Guaraná', 10.56], ['Amora', 7.84], ['Grapefruit', 6.79], ['Mirtilo', 9.45]
]
sacola = {}

def mostra_todos_produtos():
    for indice, produto in enumerate(produtos):
        nome, preco = produto
        print(f"{indice + 1} => {nome} - R${preco:.2f}")

def escolhe_produto(id):
    print(f"Você escolheu: {produtos[id - 1][0]}")
    sacola[produtos[id - 1][0]] = produtos[id - 1][1]
    return sacola

def mostra_sacola(sacola):
    print("===Até agora você já colocou em sua sacola===: ")
    for c in sacola.keys():
        print(c)
    soma_sacola = sum(sacola.values())
    print(f"Valor parcial da sacola: R$ {soma_sacola:.2f}")

def soma_das_compras(sacola):
    soma_sacola = sum(sacola.values())
    return f"Valor total da compra: R$ {soma_sacola:.2f}"

def gera_arquivo_csv(dados):
    nome_arquivo_csv = 'lista_compras.csv'
    cabecalho = ['Nota Fiscal Eletronica']
    rodape = ['Compra com pagamento confirmado']
    with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        
        # cabeçalho
        escritor_csv.writerow(cabecalho)
        escritor_csv.writerow([])

        for fruta, valor in sacola.items():
            escritor_csv.writerow([f"{fruta} - {valor}"])
        
        escritor_csv.writerow([])

        escritor_csv.writerow([soma_das_compras(sacola)])

        escritor_csv.writerow([])
        #rodapé
        escritor_csv.writerow(rodape)

        

