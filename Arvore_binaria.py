arvore = {}

def inserir(arvore, valor, raiz):
    if not arvore:
        arvore[valor] = [None, None]
        return valor  # Define o valor como a raiz
    else:
        while True:
            if valor < raiz:
                if arvore[raiz][0] is None:
                    arvore[raiz][0] = valor
                    arvore[valor] = [None, None]
                    return raiz  # Não altera a raiz original
                else:
                    raiz = arvore[raiz][0]
            elif valor > raiz:
                if arvore[raiz][1] is None:
                    arvore[raiz][1] = valor
                    arvore[valor] = [None, None]
                    return raiz  # Não altera a raiz original
                else:
                    raiz = arvore[raiz][1]
            else:
                return raiz  # Valor já está na árvore, não altera a raiz

def exibir_matriz(arvore):
    def profundidade(no):
        if no is None:
            return 0
        return 1 + max(profundidade(arvore[no][0]), profundidade(arvore[no][1]))

    h = profundidade(list(arvore.keys())[0]) if arvore else 0
    largura = (2 ** h) - 1
    matriz = [[" " for _ in range(largura)] for _ in range(h)]
    
    def preencher_matriz(no, linha, coluna):
        if no is None:
            return
        matriz[linha][coluna] = str(no)
        distancia = 2 ** (h - linha - 2)
        preencher_matriz(arvore[no][0], linha + 1, coluna - distancia)
        preencher_matriz(arvore[no][1], linha + 1, coluna + distancia)
    
    raiz = list(arvore.keys())[0] if arvore else None
    preencher_matriz(raiz, 0, largura // 2)

    print("Árvore:")
    for linha in matriz:
        print(" ".join(linha))

def buscar(arvore, valor, raiz):
    if raiz is None:
        return False
    if valor < raiz:
        return buscar(arvore, valor, arvore[raiz][0])
    elif valor > raiz:
        return buscar(arvore, valor, arvore[raiz][1])
    else:
        return True

def remover(arvore, valor, raiz):
    if raiz is None:
        return None

    if valor < raiz:
        arvore[raiz][0] = remover(arvore, valor, arvore[raiz][0])
    elif valor > raiz:
        arvore[raiz][1] = remover(arvore, valor, arvore[raiz][1])
    else:
        # Caso 1: nó com um filho ou nenhum
        if arvore[raiz][0] is None:
            temp = arvore[raiz][1]
            del arvore[raiz]  # Remove o nó da árvore
            return temp
        elif arvore[raiz][1] is None:
            temp = arvore[raiz][0]
            del arvore[raiz]  # Remove o nó da árvore
            return temp
        
        # Caso 2: nó com dois filhos
        min_maior = arvore[raiz][1]
        while arvore[min_maior][0] is not None:
            min_maior = arvore[min_maior][0]

        # Substituir o valor da raiz pelo valor do sucessor
        arvore[raiz][0] = arvore[min_maior][0]  # Mantenha o filho esquerdo do sucessor
        arvore[raiz][1] = remover(arvore, min_maior, arvore[raiz][1])  # Remove o sucessor

    return raiz

def menu():
    arvore = {}
    raiz = None
    while True:
        print("\nMenu:")
        print("1. Inserir valores")
        print("2. Buscar valor")
        print("3. Remover valor")
        print("4. Exibir árvore")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valores = input("Digite os valores para inserir (separados por espaço): ")
            valores = list(map(int, valores.split()))
            for valor in valores:
                if raiz is None:
                    raiz = inserir(arvore, valor, None)
                else:
                    inserir(arvore, valor, raiz)
            print(f"Valores {valores} inseridos.")
        
        elif opcao == "2":
            valor = int(input("Digite o valor para buscar: "))
            encontrado = buscar(arvore, valor, raiz)
            print(f"Valor {'encontrado' if encontrado else 'não encontrado'} na árvore.")
        
        elif opcao == "3":
            valor = int(input("Digite o valor para remover: "))
            raiz = remover(arvore, valor, raiz)
            print(f"Valor {valor} removido da árvore.")
        
        elif opcao == "4":
            exibir_matriz(arvore)
        
        elif opcao == "5":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executar o menu
menu()
