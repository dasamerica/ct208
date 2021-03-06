# -*- coding: utf-8 -*-
"""ct208_simulacao_chaos_games.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12WIIWwZSPV4vo56QsEV_nEWjMDptevF3
"""

#utilizado como referencia o código proposto em Python por John Cook 
#aprimorado para diversos exemplos por Peter Novig, e 
#disponível em: https://colab.research.google.com/github/norvig/pytudes/blob/master/ipynb/Sierpinski.ipynb


import matplotlib.pyplot as plt
import random

def random_walk(vertexes, N):
    "Walk halfway from current point towards a random vertex; repeat for N points."
    points = [random.choice(vertexes)]
    for _ in range(N-1):
        points.append(midpoint(points[-1], random.choice(vertexes)))
    return points

def show_walk(vertexes, N=5000):
    "Walk halfway towards a random vertex for N points; show reults."
    Xs, Ys = transpose(random_walk(vertexes, N))
    Xv, Yv = transpose(vertexes)
    plt.plot(Xs, Ys, 'r.')
    plt.plot(Xv, Yv, 'bs', clip_on=False)
    plt.gca().set_aspect('equal')
    plt.gcf().set_size_inches(9, 9)
    plt.axis('off')
    plt.show()
    
def midpoint(p, q): return ((p[0] + q[0])/3, (p[1] + q[1])/3)

def transpose(matrix): return zip(*matrix)

triangle = ((0, 0), (0.5, (3**0.5)/2), (1, 0))

show_walk(triangle, 100)

show_walk(triangle, 1000)

show_walk(triangle, 10000)

show_walk(triangle, 100000)

square = ((0, 0), (0, 1), (1, 0), (1, 1))

show_walk(square, 100)

show_walk(square, 1000)

show_walk(square, 10000)

show_walk(square, 100000)