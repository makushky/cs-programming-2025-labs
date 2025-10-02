age=18
height=1.58
name='кристина'
devochka=True

name='кристина'
age=18
print(f'Имя: {name}')
print(f'Возраст: {age}')

s1=342
s2=(float(56.2))
s3=43
sm=s1+s2+s3
print(sm)

a=3
b=8
otvet=((a + 4 * b) * (a-3*b) + a **2)
print(otvet)

a=float(input('длина a:'))
b=float(input('длина b:'))
S=a*b
P=2*(a+b)
print(f'S:{S}')
print(f'P:{P}')

print('*   *   *')
print(' **  **')
print('  *  *')

a=10
b=12
print(f'a+b= {a+b}')
print(f'a-b= {a-b}')
print(f'a*b= {a*b}')
print(f'a//b= {a//b}')
print(f'a/b= {a/b}')
print(f'a%b= {a%b}')
print(f'a**b= {a**b}')

print(f'a<b= {a<b}')
print(f'a>b= {a>b}')
print(f'a==b= {a==b}')
print(f'a!=b= {a!=b}')
print(f'a<=b= {a<=b}')
print(f'a>=b= {a>=b}')


name='кристинка'
age=18
print(f'меня зовут {name}, мне {age} лет')


p1='Съешь еще '
p2='этих мягких'
p3='французских булок'
p4='да'
p5='выпей чаю'
otvet=(p1 + ' ' + p2 + ' ' + p3 + ' ' + p4 + ' ' + p5)
print(otvet)


a='Нет! Да! ' * 4
print(a)


data = input('Введите три числа через запятую:')
a, b, c = map(float,data.split(','))
otvet=(a+c)//b
print(f'Результат: {otvet}')


word = input('слово из 10 символов:')
if len(word) >= 10:
    print(f'Исходное слово:{word}')
    print(f'Первые 4 символа:{word[0:4]} ')
    print(f'Последние 2 символа:{word[-2:]} ')
    print(f'Символы с 4 до 8:{word[4:8]} ')
    print(f'Перевернутое:{word[::-1]} ')






