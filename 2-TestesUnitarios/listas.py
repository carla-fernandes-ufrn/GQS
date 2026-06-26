def typeerror_lista(lista):
    for elemento in lista:
        if (isinstance(elemento, bool) or not isinstance(elemento, (int, float))):
            raise TypeError('Os elementos da lista devem ser inteiros ou reais.')

def ordenacao (lista):
    typeerror_lista(lista)

    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp

    return lista

def menor_elemento(lista):
    typeerror_lista(lista)

    valor_final = lista[0]

    for elemento in lista:
        if elemento < valor_final:
            valor_final = elemento
    
    return valor_final

def posicao_menor_elemento(lista):
    typeerror_lista(lista)

    valor_final = lista[0]
    posicao = 0

    for i in range(len(lista)):
        if lista[i] < valor_final:
            valor_final = lista[i]
            posicao = i
    
    return posicao