#задание 1
a=int(input('введите температуру:'))
if a >=20:
    print('кондиционер выключен')
else:
    print('кондиционер включен')

#задание 2
mes=int(input('введите номер месяца(1-12)'))
if mes==12 or 1<=mes<=2:
    print('зима')
elif 3<= mes <= 5:
    print('весна')
elif 6<=mes<=8:
    print('лето')
elif 9<=mes<=11:
    print('осень')
else:
    print('число не подходит!!!')

#задание 3
age=float(input('введите возрст собаки'))
human_age=0
if age>22:
    print('возраст собаки должен быть меньше 22')
else:
    if age<=2:
        human_age=age*10.5
    else:
        human_age=21+(age-2) *4
print(f'вашей собаке {human_age} лет в человеческих годах' )

#задание 4
number=int(input('введите число:'))
str_num=str(number)
def summ(n):
    return sum(map(int,str(n)))
if int(str_num[-1]) % 2 == 0 and summ(number)%3 == 0:
    print(number / 6)
else:
    print('число не прошло условия')


#задание 6
year = int(input('введите число:'))
if (year %100!=0 and year % 4 ==0) or (year % 400 == 0):
    print(f'{year} год високосный')
else:
    print(f'{year} год не високосный')

#задание 8
cost=float(input('введите сумму покупки:'))
if cost < 1000:
    print(f'итогова сумма покупики{cost}:')
elif 5000>cost>=1000:
    cost=(cost/100)*95
    print(f'итоговая сумма вашей покупки{cost}:')
elif 10000>cost>=5000:
    cost=(cost/100)*90
    print(f'итоговая сумма вашей покупки{cost}:')
elif cost>=10000:
    cost=(cost/100)*85
    print(f'итоговая сумма вашей покупки{cost}:')

#задание 9
hour=int(input('введит текущий час:'))
if hour in range(0,6):
    print('ночь')
elif hour in range(6, 12):
    print('утро')
elif hour in range(12, 18):
    print('день')
elif hour in range(18, 24):
    print('вечер')
else:
    print('неккоретный час:')


#задание 10
def prime(n):
    if n <=1:
        return False
    if n ==2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5) + 1,2):
        if n %i==0:
            return False

    return True
number=int(input('введите число:'))
if prime(number):
    print(f'{number} - простое')
else:
    print(f'{number} - составное')












