class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    else:
        if valor < raiz.valor:
            raiz.esquerda = inserir(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = inserir(raiz.direita, valor)
    return raiz

def criar_arvore_balanceada(lista):
    if not lista:
        return None
    meio = len(lista) // 2
    raiz = No(lista[meio])
    raiz.esquerda = criar_arvore_balanceada(lista[:meio])
    raiz.direita = criar_arvore_balanceada(lista[meio + 1:])
    return raiz

def buscar_com_posicao(raiz, valor, caminho="", nivel=0):
    if raiz is None:
        return None
    if valor < raiz.valor:
        return buscar_com_posicao(raiz.esquerda, valor, caminho + "esquerda -> ", nivel + 1)
    elif valor > raiz.valor:
        return buscar_com_posicao(raiz.direita, valor, caminho + "direita -> ", nivel + 1)
    else:
        return caminho + "raiz", nivel  

def encontrar_minimo(raiz):
    atual = raiz
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual

def remover(raiz, valor):
    if raiz is None:
        return raiz
    if valor < raiz.valor:
        raiz.esquerda = remover(raiz.esquerda, valor)
    elif valor > raiz.valor:
        raiz.direita = remover(raiz.direita, valor)
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
        temp = encontrar_minimo(raiz.direita)
        raiz.valor = temp.valor
        raiz.direita = remover(raiz.direita, temp.valor)
    return raiz

def exibir_arvore_formatada(raiz):
    if raiz is None:
        return None
    return [raiz.valor, exibir_arvore_formatada(raiz.esquerda), exibir_arvore_formatada(raiz.direita)]

def obter_nos_nivel(raiz, nivel_desejado):
    if raiz is None:
        return []
    fila = [(raiz, 0)]  # (nó, nível)
    nos_nivel = []
    while fila:
        no_atual, nivel_atual = fila.pop(0)
        if nivel_atual == nivel_desejado:
            nos_nivel.append(no_atual.valor)
        elif nivel_atual < nivel_desejado:
            if no_atual.esquerda:
                fila.append((no_atual.esquerda, nivel_atual + 1))
            if no_atual.direita:
                fila.append((no_atual.direita, nivel_atual + 1))
    return nos_nivel

def menu():
    raiz = None
    while True:
        print("\nMenu:")
        print("1. Inserir valores (balanceado ou não)")
        print("2. Buscar valor")
        print("3. Remover valor")
        print("4. Exibir árvore")
        print("5. Contar e listar elementos em um nível")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            modo_balanceado = input("Deseja inserir valores de forma balanceada? (s/n): ").lower()
            valores = input("Digite os valores para inserir (separados por espaço): ")
            valores = list(map(int, valores.split()))
            
            if modo_balanceado == "s":
                valores.sort()  # Ordena para garantir balanceamento
                raiz = criar_arvore_balanceada(valores)
                print(f"Valores {valores} inseridos de forma balanceada.")
            else:
                for valor in valores:
                    raiz = inserir(raiz, valor)
                print(f"Valores {valores} inseridos de forma não balanceada.")
        
        elif opcao == "2":
            valor = int(input("Digite o valor para buscar: "))
            resultado = buscar_com_posicao(raiz, valor)
            if resultado:
                posicao, nivel = resultado
                print(f"Valor encontrado na posição: {posicao} no nível: {nivel}")
            else:
                print("Valor não encontrado na árvore.")
        
        elif opcao == "3":
            valor = int(input("Digite o valor para remover: "))
            raiz = remover(raiz, valor)
            print(f"Valor {valor} removido da árvore.")
        
        elif opcao == "4":
            print("Árvore formatada:")
            print(exibir_arvore_formatada(raiz))
        
        elif opcao == "5":
            nivel_desejado = int(input("Digite o nível para listar os elementos: "))
            nos_nivel = obter_nos_nivel(raiz, nivel_desejado)
            print(f"Nível {nivel_desejado} tem {len(nos_nivel)} elemento(s): {nos_nivel}")
        
        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

menu()
