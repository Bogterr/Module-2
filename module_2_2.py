import time
import random                       # чтобы было интересно и случайно

######################          !!!GENERATOR!!!             ######################

var_ = []

# variable 1                                            1 вариант до int(1000)
for i in range(3):
    random_num = int(random.randint(1, 1000))
    var_.append(random_num)
# print(var_)

first = var_[0]
second = var_[1]
third = var_[2]

print("Первое значение = ", first)
print("Второе значение = ", second)
print("Третье значение = ", third)

if first == second and first == third:
    print("Все три числа случайно оказались равны!!! Купи билетик :) Результат = ", 3)
elif first == second or first == third or second == third:
    print("Совпала пара! Результат = ", 2)
else:
    print("Совпадения нет, не переживай - все числа случайны! Результат = ", 0)
print()
####################################################################################
time.sleep(2)
######################          РУЧНОЕ УПРАВЛЕНИЕ             ######################

print("Давай теперь попробуем сами?")

count = 0



while count != 3:
    digit = False
    while digit == False:
        first = input("Введи первое число = ")
        if first.isdigit():
            # print("Первое число = ", first)
            print()
            digit = True
            count += 1
        else:
            print("Введенное значение: ", first, " - не является числом, давай еще раз...")
            print()

    digit = False
    while digit == False:
        second = input("Введи второе число = ")
        if second.isdigit():
            # print("Второе число = ", second)
            print()
            digit = True
            count += 1
        else:
            print("Введенное значение: ", second, " - не является числом, давай еще раз...")
            print()

    digit = False
    while digit == False:
        third = input("Введи третье число = ")
        if third.isdigit():
            # print("Третье число = ", third)
            print()
            digit = True
            count += 1
        else:
            print("Введенное значение: ", third, " - не является числом, давай еще раз...")
            print()

print("Итого:")
print("Первое число =", first)
print("Второе число =", second)
print("Третье число =", third)

if first == second and first == third:
    print("Все три числа равны! Но мы то знаем как это получилось) :) Результат = ", 3)
elif first == second or first == third or second == third:
    print("Совпала пара! Результат = ", 2)
else:
    print("Совпадения нет, не переживай - все числа случайны, хотя... не на этот раз)) Результат = ", 0)
print()