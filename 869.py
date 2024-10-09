import sys

def vuelos(matriz1, matriz2):
    
    for k in range(26):
        for i in range(26):
            for j in range(26):
                matriz1[i][j] = min(matriz1[i][j], matriz1[i][k] + matriz1[k][j])
                matriz2[i][j] = min(matriz2[i][j], matriz2[i][k] + matriz2[k][j])
    
    
    for i in range(26):
        for j in range(26):
            if (matriz1[i][j] < float('inf') and matriz2[i][j] == float('inf')) or \
               (matriz2[i][j] < float('inf') and matriz1[i][j] == float('inf')):
                return False
    return True

def main():
   
    matriz1 = [[float('inf')] * 26 for _ in range(26)]
    matriz2 = [[float('inf')] * 26 for _ in range(26)]
    
    
    for i in range(26):
        matriz1[i][i] = 0
        matriz2[i][i] = 0

    
    abc = {}
    for i in range(26):
        letra = chr(ord('A') + i)  
        abc[letra] = i

   
    n = int(sys.stdin.readline().strip())
    
    for a in range(n):
       
        numV1 = int(sys.stdin.readline().strip())
        for _ in range(numV1):  
            vuelo = sys.stdin.readline().strip()
            origen, destino = vuelo.split()
            matriz1[abc[origen]][abc[destino]] = 1
            matriz1[abc[destino]][abc[origen]] = 1  

        
        numV2 = int(sys.stdin.readline().strip())
        for _ in range(numV2):  
            vuelo = sys.stdin.readline().strip()
            origen, destino = vuelo.split()
            matriz2[abc[origen]][abc[destino]] = 1
            matriz2[abc[destino]][abc[origen]] = 1  

        
        iguales = vuelos(matriz1, matriz2)
        if iguales:
            print("YES")
        else:
            print("NO")


main()
