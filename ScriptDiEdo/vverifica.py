val1 = int(input('inserisci un valore'))

val2 = int(input('inserisci un secondo valore'))

val3 = int(val1) + int(10)

if val2 >= val3:
    print('I tre valori precedenti a val1 e val2 sono:')
    print('val1:')
    print(int(val1)-int(1))
    print(int(val1)-int(2))
    print(int(val1)-int(3))
    print('val2:')
    print(int(val2)-int(1))
    print(int(val2)-int(2))
    print(int(val2)-int(3))

elif val2 < val3:
    print('I tre valori precedenti e successivi a val1 e val2 sono:')
    print('minori di val1:')   #minori
    print(int(val1)-int(1))
    print(int(val1)-int(2))
    print(int(val1)-int(3))
    print('minori di val2:')
    print(int(val2)-int(1))
    print(int(val2)-int(2))
    print(int(val2)-int(3))

    print('maggiori di val1:')   #maggiori
    print(int(val1)+int(1))
    print(int(val1)+int(2))
    print(int(val1)+int(3))
    print('maggiori di val2:')
    print(int(val2)+int(1))
    print(int(val2)+int(2))
    print(int(val2)+int(3))
    