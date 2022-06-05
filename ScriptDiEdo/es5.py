values = []

while True:
    try:
        val = int(input('inserire un valore intero positivo:'))
        if val >=0:
            if val != 0:
                values.append(val)
                continue
            else:
                print('il valore minore inserito è:',min(values))
                break
        else:
            print('dato non valido,')
            continue
    except:
        print('il dato inserito non è valido,')