i = 0

print('inserire un numero intero positivo:')

while True:
    try:
        num = int(input())
        if num>=0:
            break
        else:
            print('dato non valido, inserire un nuovo valore POSITIVO:')
            continue
    except:
        print('il dato inserito non è corretto,\ninserire un nuovo dato:')

if int(num)>int(0):
    while i<20:
        i+=1
        print('\n',i)
else:
    while i>-20:
        i-=1
        print('\n',i)