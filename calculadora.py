print('PRIMERA VERSIÓN DE CALCULADORA')
print('Solo puede ingresar expresiones matematicas que sean de suma, resta, multiplicación o división')
cadena = input('Escriba el termino: ')

nuevo = cadena.replace(' ', '')
print(nuevo)
contAlph = 0
exprFin = ''
listChar = []

for i in nuevo:
  if i.isalpha() == True:
    contAlph += 1
  else:
    listChar.append(i)

if contAlph == 0:
  for n in range(len(listChar)):
    if listChar[n] in '(' and listChar[n-1] not in '+-*/' and n-1 != -1:
      exprFin = exprFin + '*('
    elif listChar[n] in ')' and n+1 < len(listChar):
      if listChar[n+1] not in '+-*/':
        exprFin = exprFin + ')*'
      else:
        exprFin = exprFin+ ')'
    else:
      exprFin = exprFin + listChar[n]
else:
  print('No se puede evaluar')

print(eval(exprFin))