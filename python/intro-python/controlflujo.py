#if 2 < 5:
    #print ('2 es menor que 5')

# a == b
# a < b
# a > b
# a != b
# a <= b
# a >= b

#if 2 == 2:
    #print ('2 es igual a 2') 

# if 2 == 3:
#     print ('2 es igual a 3')

# if 2 > 5:
#     print ('2 es mayor q 5') 

# if 5 > 2:
#     print ('5 es mayor q 2') 

# if 2 != 2:
#     print ('2 es distinto a 2') 

# if 3 != 2:
#     print ('3 es distinto q 2') 

# if 3 >= 2:
#     print ('3 es mayo o igual a 2')

# if 3 <= 3:
#     print ('3 es menor igual a 3')  

if 2 > 5:
    print ('2 es menor a 5 en if')

elif 2 > 5:
    print ('2 es menor a 5 en elif')

elif 2 < 5:
    print ('2 menor a 5 en segundo elif')

else:
    print ('yo me imprimo solo si lo anterior evalua en falso')


if 2 > 5:
    print ('2 es menor a 5 en if')

else:
    print ('yo me imprimo solo si lo anterior evalua en falso 2')

if 2 < 5: print ('if de una linea')

print ('Cuando devuelve True') if 5 > 2 else print('cuando devuelve false')

if 2 < 4 and 3 > 2:
    print ('ambas devuelven True')


if 2 < 4 and 3 < 2:
    print ('Hay una falsa esto no se mostrara')

if 1 < 0 or 1 > 0: #Si una condicion evalue en true se ejecuta la intruccion
    print ('una de las 2 condiciones devolvio True')


if 1 < 0 or 1 < 0: #si ambas condicion son falsas entonces no se ejecuta
    print ('si ambas condiciones son false no se ejecuta esto')    