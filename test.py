from random import randint
import string
Todos= list()
C3 = string.punctuation[randint(0, len(string.punctuation) - 1)]
C4 = string.digits[randint(0, len(string.digits) - 1)]
C5 = C4, C3
Todos.append(C5)
c1 = string.punctuation + string.digits
cont = 0
for i in c1:
    cont += 1
    print('', c1[cont-1], end='')



