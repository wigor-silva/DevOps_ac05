numero_maximo = int(input("digite um numero maximo: "))
numero = 1
contador = 1
while contador <= numero_maximo:
   contador = contador + 1
   numero = numero + 1
   if numero % 2 == 1:
      print(numero)
   else:
      contador = contador - 1
