'''Посчитать сумму двух натуральных чисел A и B, записанных в римской системе счисления. Ответ также записать в римской системе счисления.

M = 1000, D = 500, C = 100, L = 50, X = 10, V = 5, I = 1. Все числа – не превышают 2000.

Входные данные

В строке записано два числа в римской системе счисления, между которыми стоит знак + .

Выходные данные

Единственное число – сумма чисел, записанное также в римской системе счисления. Числа в римской системе счисления записаны большими латинскими буквами.'''

word = "IIII" #input()
arr = word.split('+')
print(arr)
summa = 0

value_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
#decoder
for i in range(len(arr[0])):
    print(value_dict[arr[0][i]])
    print('\n')


s = len(arr[0])
for i in range(s):
    for j in range(s-i-1):
        if (value_dict[arr[0][j]] <= value_dict[arr[0][j+1]]):#для сначала меньшие
            print(value_dict[arr[0][j]])
            summa -= value_dict[arr[0][j]]
            '''
        elif(value_dict[arr[0][j]] >= value_dict[arr[0][j+1]]):#для сначала большие
            summa += value_dict[arr[0][j]]
            '''
print(summa)
