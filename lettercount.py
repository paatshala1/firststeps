import string

#files = ['ddhs.txt'] #, 'ddhf.txt' , 'ddhe.txt']
files = ['ddhs.txt', 'ddhf.txt' , 'ddhe.txt']

hndnum = 0
hndlst = list()
dctlst = list()

for f in files :
    dynhandler = 'handler' + str(hndnum)    #CREACIÓN DINÁMICA DE HANDLERS Y
    dyndct = 'dict'+ str(hndnum)            #DICTIONARIES, OJO QUE DEBEN CREARSE
    dyndct = dict()                         #COMO DICT() XQ SINO LOS VE COMO STR
    try :
        dynhandler = open(files[hndnum] , 'r')
        hndlst.append(dynhandler)
        dctlst.append(dyndct)
    except :
        print('ERROR en archivo:' , files[hndnum])
    hndnum += 1

pos = 0
for eachhnd in hndlst :
    for line in eachhnd :
        line = line.rstrip()
        line = line.lower()
        line = line.translate(line.maketrans('' , '' , string.punctuation))
        words = line.split()
        for wd in words :
            for lttr in wd :
                if not lttr.isalpha() : #LIMITA EL CONTEO A LETRAS
                    continue
                else :
                    dctlst[pos][lttr] = dctlst[pos].get(lttr , 0) + 1   #LLAMA CADA DICTIONARY PARA ACUMULAR
    print('Archivo en posición %d: %s' % (pos , files[pos]) )
    print(sorted([(v , k) for (k , v) in dctlst[pos].items()] , reverse = True) [ : 5])
    print()
    pos += 1
