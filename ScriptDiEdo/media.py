#variables
j = 0
i = 0
tot1 = 0


while i<50:

    print('inserire un voto:')
    while True:
        try:
            voto = int(input())
            break
        except:
            print('il dato inserito non è valido, inserire un nuovo dato:')
    
    tot1 = tot1 + voto

    print('digitare [S] per inserire un nuovo voto \ndigitare [N] per calcolare la media')

    while True:
        try:
            req = str(input())
            break
        except:
            print('il dato inserito non è valido, inserire un nuovo dato:')
    j+=1
    if req == str('S') or req == str('s'):
        i = 0

    elif req == str('N') or req == str('n'):
        i = 100
        
    else:
        print('il dato non è valido, inserire nuovamente il voto:')
        j-=1

print('la media dei voti è', tot1/j)