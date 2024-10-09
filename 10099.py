import sys

def tourist_guide(n, matriz, origen, destino, turistas):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = max(matriz[i][j], min(matriz[i][k], matriz[k][j]))

    capacidad_maxima = matriz[origen][destino]

    if capacidad_maxima == float('-inf'):
        return float('inf')

    return (turistas + capacidad_maxima - 1) // capacidad_maxima  

def main():
    numero_escenario = 1

    while True:
        entrada = sys.stdin.readline().strip()
        if entrada == "0 0":
            break
        
        N, R = map(int, entrada.split())
        
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

        S, D, T = map(int, sys.stdin.readline().strip().split())
        S -= 1  
        D -= 1  

        viajes = tourist_guide(N, matriz, S, D, T)

        print(f"Escenario #{numero_escenario}")
        print(f"Número Mínimo de Viajes = {viajes}")
        
        numero_escenario += 1

if __name__ == "__main__":
    main()
