from sys import stdin


def leer_imagen(mapa, w, h):
    visitados = [0] * h
    for i in range(h):
        visitados[i] = [False] * w
    puntos = []
    
    for i in range(h):
        for j in range(w):
            if mapa[i][j] == '*' and not visitados[i][j]:
                puntos_dado = leer_dado(mapa, visitados, w, h, i, j)
                puntos.append(puntos_dado)
                
    puntos.sort()
    return puntos


def leer_dado(mapa, visitados, w, h, x, y):
    dado = []
    stack = [(x, y)]
    visitados[x][y] = True
    
    while stack:
        i = stack.pop()
        x = i[0]
        y = i[1]
        dado.append(i) 
        if 0 <= x - 1 < h and 0 <= y < w and not visitados[x - 1][y] and mapa[x - 1][y] == '*':
            visitados[x - 1][y] = True
            stack.append((x - 1, y))
        if 0 <= x + 1 < h and 0 <= y < w and not visitados[x + 1][y] and mapa[x + 1][y] == '*':
            visitados[x + 1][y] = True
            stack.append((x + 1, y))
        if 0 <= x < h and 0 <= y - 1 < w and not visitados[x][y - 1] and mapa[x][y - 1] == '*':
            visitados[x][y - 1] = True
            stack.append((x, y - 1))
        if 0 <= x < h and 0 <= y + 1 < w and not visitados[x][y + 1] and mapa[x][y + 1] == '*':
            visitados[x][y + 1] = True
            stack.append((x, y + 1))
    
    puntos = 0
    
    for i in dado:
        x = i[0]
        y = i[1]
        if 0 <= x - 1 < h and 0 <= y < w and mapa[x - 1][y] == 'X' and not visitados[x - 1][y]:
            marcar_puntos_juntos(mapa, visitados, x - 1, y, w, h)
            puntos += 1
        if 0 <= x + 1 < h and 0 <= y < w and mapa[x + 1][y] == 'X' and not visitados[x + 1][y]:
            marcar_puntos_juntos(mapa, visitados, x + 1, y, w, h)
            puntos += 1
        if 0 <= x < h and 0 <= y - 1 < w and mapa[x][y - 1] == 'X' and not visitados[x][y - 1]:
            marcar_puntos_juntos(mapa, visitados, x, y - 1, w, h)
            puntos += 1
        if 0 <= x < h and 0 <= y + 1 < w and mapa[x][y + 1] == 'X' and not visitados[x][y + 1]:
            marcar_puntos_juntos(mapa, visitados, x, y + 1, w, h)
            puntos += 1
    
    return puntos

def marcar_puntos_juntos(grid, visitados, x, y, w, h):
    stack = [(x, y)]
    visitados[x][y] = True
    
    while stack:
        i = stack.pop()
        x = i[0]
        y = i[1]
        if 0 <= x - 1 < h and 0 <= y < w and not visitados[x - 1][y] and grid[x - 1][y] == "X":
            visitados[x - 1][y] = True
            stack.append((x - 1, y))
        if 0 <= x + 1 < h and 0 <= y < w and not visitados[x + 1][y] and grid[x + 1][y] == "X":
            visitados[x + 1][y] = True
            stack.append((x + 1, y))
        if 0 <= x < h and 0 <= y - 1 < w and not visitados[x][y - 1] and grid[x][y - 1] == "X":
            visitados[x][y - 1] = True
            stack.append((x, y - 1))
        if 0 <= x < h and 0 <= y + 1 < w and not visitados[x][y + 1] and grid[x][y + 1] == "X":
            visitados[x][y + 1] = True
            stack.append((x, y + 1))

if __name__ == "__main__":
    res = []
    while True:
        w, h = map(int, stdin.readline().split())
        if w == 0 and h == 0:
            break
        
        mapa = []
        for i in range(h):
            mapa.append(stdin.readline().strip())
          
        res.append(leer_imagen(mapa, w, h))
    print("")
    x = 1   
    for i in res:
        print(f"Throw {x}")
        print(" ".join(map(str, i)))
        print("")
        x += 1


