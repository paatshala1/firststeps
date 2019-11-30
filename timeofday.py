file = input('Nombre de archivo: ')
try :
    handler = open(file+'.txt' , 'r')
except :
    print(20*'-')
    print('ERROR de archivo: ' , file)
    print(20*'-')
    quit()

hour = dict()
for line in handler :
    if not line.startswith('From ') :
        continue
    else :
        line = line.rstrip()
        words = line.split()
        t = words[5].split(':')
        hour[t[0]] = hour.get(t[0] , 0) + 1
        #print(hour)    #ESTE PRINT DEBERÍA ESTAR FUERA DEL FOR, SIN EMBARGO
                        #AL ESTAR DENTRO PERMITE VER EL CRECIMIENTO, POR LO QUE
                        #PODRÍA SERVIR EN CASO QUE SE QUIERA VER GRÁFICAMENTE

#IMPRIME ORDENADO POR KEY (LA HORA)
#TENER CUIDADO CON LOS [] XQ ESO DEFINE LA LISTA Y SI LOS PONGO FUERA DEL SORTED
#ENTONCES LO QUE ESTOY PASANDO ES UNA LISTA DE UN ELEMENTO NADA MÁS
orderhour = sorted([(k , v) for k , v in hour.items()])

for k , v in orderhour :
    print(k , v)

#IMPRIME ORDENADO POR VALUE (LA CANTIDAD)
#print([sorted((v , k) for k , v in hour.items())])
