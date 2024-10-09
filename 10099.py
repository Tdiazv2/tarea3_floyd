import sys

def tourist_guide(n, matriz, origen, destino, turistas):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = max(matriz[i][j], min(matriz[i][k], matriz[k][j]))

    maxi = matriz[origen][destino]

    if maxi == float('-inf'):
        return float('inf')

    return (turistas + maxi - 1) // maxi  

def main():
    num = 1

    while True:
        linea = sys.stdin.readline().strip()
        if linea == "0 0":
            break
        
        N, R = map(int, linea.split())
        
        x = float('-inf')
        matriz = [[0] * N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if i != j:
                    matriz[i][j] = x

        for _ in range(R):
            C1, C2, P = map(int, sys.stdin.readline().strip().split())
            matriz[C1 - 1][C2 - 1] = P  
            matriz[C2 - 1][C1 - 1] = P  

        origen, destino, turistas = map(int, sys.stdin.readline().strip().split())
        origen -= 1  
        destino -= 1  

        viajes = tourist_guide(N, matriz, origen, destino, turistas)

        print(f"Escenario #{num}")
        print(f"Número Mínimo de Viajes = {viajes}")
        
        num += 1

if __name__ == "__main__":
    main()
