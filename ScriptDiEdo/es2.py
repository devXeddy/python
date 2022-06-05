
tot = 1

while True:
    val = int(input('\ninserire un valore:'))
    if val != 0:
        if val%10==0:
            tot+=1
        continue
    else:
        print('\n\nil numero di valori inseriti terminanti con "0" è',tot)