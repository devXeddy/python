values = []
counter = 0
j = -1
i = 0
while True:
    try:
        val = int(input('inserire un valore:'))
        if val == 0:
            break
        else:
            if i<1:
                values.append(val)
                i+=1
            if val == values[0]:
                counter = counter + 1 
            continue
    except:
        print('dato non valido,')

print('il numero di valori uguali al primo inserito è:',counter)