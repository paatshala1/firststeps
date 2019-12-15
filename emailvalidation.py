def validchar(string , pos , currentchar):
    """
    string : cadena de texto a la que se evaluarán sus caracteres
    pos : posición del caracter que se está evaluando
    currentchar : caracter actual que se está evaluando
    
    Valida que los caracteres sean válidos y esten en posiciones correctas,
    que no haya caracteres especiales fuera del '.' y '@', además que estos
    no estén en la primera o última posición
    """
    if pos == 0 or pos == (len(email)-1):
        if not currentchar.isalpha():
            return False
        else:
            return True
    elif currentchar == '.' or currentchar == '@':
        return string[pos + 1].isalpha()
    else:
        return currentchar.isalpha()

print('Validación de email\n' + 15 * '-')

valid = True
email = input('Ingrese su email: ')
arrobas = 0
puntos = 0

for i , v in enumerate(email):
    if v == '@':
        arrobas += 1
    if v == '.':
        puntos += 1
    valid = validchar(email , i , v)
    if valid == False:
        global ERR
        ERR = i
        break

if arrobas != 1 or puntos == 0:
    print('Correo inválido')
elif valid:
    print('Correo válido')
else:
    print(f'Correo inválido posiciones' , {ERR} , {ERR+1})
    