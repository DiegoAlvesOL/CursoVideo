# Para realizar importação de novos modulos devo ditar import.
# existem duas formas de realizar a importação. Eu posso importar toda a biblioteca através do comando impot. o nome da biblioteca.
# Ou eu posso importar apenas o modulo que eu quero, difitando o comando from nome da biblioteca import nome da função

# exemplo para realizar a importação da biblioteca de matemática devo digitar import.math ou posso realiz from math import floor




import math
from math import sqrt
num = int(input("digite um numero: "))
raiz = sqrt(num)
print (" A raiz quadrade de {} é {}".format(num, raiz))


# O modulo random importa uma função que gera numeros aleatórios
import random
num2 = random.randint (1, 5)
print(num2)
