operadores = []
operandos = []
digitos = []
unir = ''
signo = 1
flagListar = True


print('PRIMERA VERSIÓN DE CALCULADORA')
pantalla = input('Escriba el termino ')


if pantalla.isdigit() == False:
    for i in pantalla:
      if i in '.+-*x/0123456789':        
        digitos.append(i)
      else:
        print('No se puede realizar ninguna operación, vuelva a intentarlo')
        flagListar = False
        break
print('lista: ',digitos)

if flagListar == True:
  for j in range(len(digitos)):
    if digitos[j] in '0123456789.':
      unir=unir+digitos[j]
    if digitos[j] in '+-*x/':
      if digitos[j-1] == '+' and digitos[j] == '-':
        signo*=-1
      print(signo)
      if unir != '':
        numero = float(unir)*signo
        operandos.append(numero)
        operadores.append(digitos[j])
        signo = 1
      unir = ''          
    if len(digitos) == j+1 and unir != '':    
      operandos.append(float(unir)*signo)
