'''Какое наименьшее число n можно представить в виде произведения n = a ∙ b
ровно k (1 ≤ k ≤ 50) способами? Произведения a ∙ b и b ∙ a считаются
одним способом, все числа натуральные.

Входные данные

Одно число k.

Выходные данные

Выведите число n.



'''
def factors(integer_val):
    n = 0
    while (True):
        kol = 0
        n += 1
        for i in range(n, 0, -1):
            if (n % i == 0):
                if (i * i == n):
                    kol = kol + 2;
                else:
                    kol += 1
        if (kol / 2 == k):
            break
    print(n)


k = int(input())
factors(k)


