import random

def calcularpi(n):
    incircle = 0
    outcircle = 0
    for i in range(n):
         x = random.uniform(0,1)
         y = random.uniform(0,1)
         if x**2+y**2 <= 1:
             incircle += 1
         else:
             outcircle+=1
    return 4*(float(incircle)/float((incircle+outcircle)))


n = input("Numero de interacoes ")
print("Pi = ")
print(calcularpi(n))
