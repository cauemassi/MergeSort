#retorna primeiro elemento lista
def head(lista):
		return lista[0]

#retorna lista sem o primeiro elemento
def tail(lista):
		return lista[1:len(lista)]

#concatena e ordena duas listas ordenadas
def somaListaOrdenado (lista1, lista2, retorno = []):
	if (lista1 == []):
		return retorno + lista2
	elif(lista2 == []):
		return retorno + lista1
	elif(lista1[0] < lista2[0]):
		return somaListaOrdenado(tail(lista1), lista2, retorno + [head(lista1)])
	return somaListaOrdenado(lista1, tail(lista2), retorno + [head(lista2)])

#divide uma lista
def divideLista(lista):
	m = len(lista)//2
	return lista[0:m], lista[m:len(lista)]

#ordena uma lista pelo metodo mergesort
def mergeSort(lista):
	if(len(lista) == 1):
		return lista
	else:
		lista1, lista2 = divideLista(lista)
		return somaListaOrdenado(mergeSort(lista1), mergeSort(lista2))


print(mergeSort([12, 11, 13, 5, 6, 7]))
