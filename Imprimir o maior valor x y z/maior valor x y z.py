
x = int(input('digite o primeiro número:'))
y = int(input('digite o segundo  número:'))
z = int(input('digite o terceiro número:'))
#verificando maior valor
maior = x
if y > x and y > z :
  maior = y
if z > x and z > y:
  maior = z
  print('==' * 20)
  print('o maior número é {}'.format (maior))
  
  