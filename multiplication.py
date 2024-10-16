def multiplication_table(n):
    for i in range(1,10):
        for j in range(1, 10):
            print(f"{j} x {i} = {j * i}",end = '\t')
        print()
n = int(input("Введите число для таблицы умножения: "))
multiplication_table(n)
