tot = 0

while True:
    try:
        val1 = int(input('inserire il primo valore:'))
        if val1<=0:
            print('il dato inserito non è valido,')
            continue
        else:
            break
    except:
        print('il dato inserito non è valido,')



while True:
    try:
        val2 = int(input('inserire il primo valore:'))
        if val2<=0:
            print('il dato inserito non è valido,')
            continue
        else:
            break
    except:
        print('il dato inserito non è valido,')

        
while True:
    tot = tot + val1
    val2 = val2 -1
    if val2==0:
        print('il risultato è:',tot)
        break
    else:
        continue