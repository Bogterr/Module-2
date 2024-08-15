numbers = [1, 2, 3, 4,              # дан список чисел
           5, 6, 7, 8,
           9, 10, 11, 12,
           13, 14, 15]

primes = []                         # список для ПРОСТЫХ чисел
not_primes = []                     # список для НЕ ПРОСТЫХ чисел

ctrl = 0                            # счетчик
for i in range(len(numbers)+1):     # прогон в диапазоне от 2 до конца данного списка
    for j in range(2, i):           # прогон в диапазоне от 2 до текущего значения
        if i % j == 0:
            ctrl = ctrl + 1         # количество успешных операции деления
    if ctrl == 0:                   # если поделить не удалось и счетчик на нуле, то
        primes.append(i)            # вносим это ПРОСТОЕ число в список
    else:                           # иначе сбрасываем счетчик и по новой
        not_primes.append(i)        # вносим в список НЕ ПРОСТЫХ чисел
        ctrl = 0                    # сбрасываем счетчик и по новой
print(primes)                       # выводим, что получилось
print(not_primes)
print()
###################################################################################


# Special


ctrl = 0                                            # счетчик
escape = "end"                                      # команда к завершению программы 
work = True

print("Для завершения программы введите: end")

while work:
    numbers_v2 = []                                     # список для простых чисел
    hot_numbers = []                                    # список для НЕ ПРОСТЫХ чисел
    print()
    
    x = input("Введите целое положительное число, больше 2: ")
    print()
    if x.lower() == escape:
        work = False
        print("Выполнен выход из программы")
    elif x.isdigit():
        x = int(x)
        if x < 2:
            print("Выбран диапазон меньше 1")
        else:
            for i in range(2, x+1):                             # прогон в диапазоне от 2 до введенного
                for j in range(2, i):                           # прогон в диапазоне от 2 до текущего
                    if i % j == 0:
                        ctrl = ctrl + 1                         # количество успешных операции деления
                if ctrl == 0:                                   # если поделить не удалось и счетчик на нуле, то
                    numbers_v2.append(i)                        # вносим это простое число в список
                else:                                           # иначе сбрасываем счетчик и по новой
                    hot_numbers.append(i)
                    ctrl = 0
            print(numbers_v2)                                   # выводим, что получилось
            print(hot_numbers)
