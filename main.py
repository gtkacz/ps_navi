def questao_um(n: int = 5e6) -> int:
    c = 0
    
    for i in range(1, n+1):
        par = m_49 = m_37 = False
        
        if i % 2 == 0:
            par = True
            
        if i % 49 == 0:
            m_49 = True
            
        if i % 37 == 0:
            m_37 = True
        
        if par and m_49 and m_37:
            c += 1
            
    return c

from math import factorial, log
from statistics import mean

def questao_dois(n: int = 10) -> tuple:
    X = []
    
    for i in range(n):
        if i % 2 == 0:
            elemento = (3**i) + 7*(factorial(i))
        else:
            elemento = (2**i) + 4*(log(i))
        
        X.append(elemento)
        
    imax = X.index(max(X))
    avg = round(mean(X), 2)
    
    return imax, avg

def questao_tres(n_g: int, n_a1: int, n_a2: int, n_a3: int, n_a4: int, n_a5: int) -> str:
    notas = {
            'Nota do grupo': n_g,
            'Aluno 1': n_a1,
            'Aluno 2': n_a2,
            'Aluno 3': n_a3,
            'Aluno 4': n_a4,
            'Aluno 5': n_a5,
            }
    
    aluno = max(notas, key=notas.get)
    
    return f'O aluno {aluno} teve a maior nota, tendo tirado {notas[aluno]}.'