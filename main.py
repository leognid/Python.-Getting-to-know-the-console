long = int(input('Введите сторону квадрата:'))

perimeters = (long * 4)
print( 'Периметр квадрата равен: ' , perimeters)
print( 'Площадь квадрата равна: ' , perimeters)

rectangle1 = int(input('Введите первую сторону прямоугольника:'))
rectangle2 = int(input('Введите вторую сторону прямоугольника:'))
perimeterr = (rectangle1*2+rectangle2*2)
print( 'Периметр прямоугольника равен: ', perimeterr)
squarer = (rectangle1 * rectangle2)
print ('Площадь прямоуголька равна: ', squarer)

line = input('Введите символ:')
print (line * (perimeters + squarer))

salary = float(input( 'Введите заработную плату за месяц: '))
mortgage = float(input( 'Введите какой процент уходит на ипотеку: '))
life = float(input( 'Введите какой процент уходит на жизнь: '))
mortgage1 = (salary * mortgage * 12 / 100)
print('На ипотеку было патрачено за год:' , mortgage1)
life1 = (salary * life * 12 / 100)
remains = ( salary * 12 - mortgage1 - life1)
print ('Средств остается конец года: ' , remains)
