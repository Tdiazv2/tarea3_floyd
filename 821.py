import sys

def page_hoping(matriz, n):
   
    for k in range(101):
        for i in range(101):
            for j in range(101):
                matriz[i][j] = min(matriz[i][j], matriz[i][k] + matriz[k][j])
    
    valor = 0
    
    for i in range(101):
        for j in range(101):
            if i != j and matriz[i][j] < float('inf'):
                valor += matriz[i][j]

    div = n * (n - 1)
    return valor / div if div > 0 else float('inf')   

def main():
    while True:
        matriz = [[float('inf')] * 101 for _ in range(101)] 
        for i in range(101):
            matriz[i][i] = 0  

        nodos_unicos = set()
        lista = list(map(int, sys.stdin.readline().strip().split()))
        if lista == [0, 0]:  
            break
        
        
        for i in range(0, len(lista), 2):
            origen = lista[i]
            destino = lista[i+1]
            matriz[origen][destino] = 1  
            if origen != 0 or destino != 0:
                nodos_unicos.add(origen)  
                nodos_unicos.add(destino) 

        n = len(nodos_unicos)       
        promedio = page_hoping(matriz, n)  
        print(f"Promedio de distancias más cortas: {promedio:.3f}")


main()
