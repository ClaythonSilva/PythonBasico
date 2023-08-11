import random
import string

#ABC9D - 99

sortear_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

C1 = random.choice(sortear_letras)
C2 = random.choice(sortear_letras)
C3 = random.choice(sortear_letras)
N1 = str(random.randrange(0,9))
C4 = random.choice(sortear_letras)
Numero_Decimal = str(random.randrange(10,99))

print("Modelo de placa padrao gerado aleatoriamente: ",C1+C2+C3+N1+C4+"-"+Numero_Decimal)














