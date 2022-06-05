tot = 0

while True:
    try:
        val1 = int(input('inserire il primo valore:'))
        val2 = int(input('inserire il secondo valore:'))

        while True:
            tot = tot + val1
            val2 = val2 -1
            if val2 == 0:
                print(tot)
                break
            else:
                continue
            
        break

    except:
        print('il dato inserito non è valido')