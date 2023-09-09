import random

pr = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pas = int(input('введи длину пароля: '))

passave = ''

for i in range(pas): 
    passave += random.choice(pr)
print(passave)