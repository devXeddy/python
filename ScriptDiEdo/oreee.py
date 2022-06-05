M1 = int(input('inserire i minuti:'))
h = M1//60
m = M1-(h*60) 
if m>0:
    print(str(h)+'h',str(m)+'m')
else:
    print(str(h)+'h')