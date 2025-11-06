name = input("Введите имя: ")
age = input("Ввведите возраст: ")
for i in range(10):
    print(f'Меня зовут {name} и мне {age} лет') #Задание 1

a = input("Введите число от 1 до 9: ")
b = 1
for i in range(10):
    print(a ,'*', b, '=', int(a)*b)
    b += 1 #Задание 2

for i in range(2, 101, 3):
    print(i) #Задание 3

num = int(input("Введите число: "))
k1 = 1
for i in range(1, num+1):
    k1 = k1 * i
print(k1) #Задание 4

count = 20
while count >= 0:
    print(count)
    count -= 1 #Задание 5

limit=int(input('Введите число:'))
a,b=0,1
print((f'Числа фибоначчи до {limit}:'))
while a<=limit:
    print(a,end=' ')
    a,b = b, a+b
        #Задание 6

word = str(input('Введите слово: '))
otvet = []
k = 1
for letter in word:
    otvet.append(letter)
    otvet.append(str(k))
    k += 1
print(*otvet, sep='')  #Задание 7

while True:
    a, b = input('Введите два числа через пробел: ').split()
    print('Сумма равна = ', (int(a)) + (int(b))) #Задание 8