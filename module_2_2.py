import time
import random                       # чтобы было интересно и случайно

######################          !!!GENERATOR!!!             ######################

var_ = []                                               # список для чисел

# variable 1                                            # 1 вариант до int(1000)
for i in range(3):
    random_num = int(random.randint(1, 1000))     # Генерируем числа
    var_.append(random_num)                             # пишем в список
# print(var_)

first = var_[0]                                         # присваеваем переменным из списка
second = var_[1]
third = var_[2]

print("Первое значение = ", first)                      # Выводим пользователю
print("Второе значение = ", second)
print("Третье значение = ", third)

# УСЛОВИЯ
if first == second and first == third:                                                      # если 3 из 3 равны, то
    print("Все три числа случайно оказались равны!!! Купи билетик :) Результат = ", 3)
elif first == second or first == third or second == third:                                  # или если 2 из 3 равны, то
    print("Совпала пара! Результат = ", 2)
else:                                                                                       # иначе если совпадений нет
    print("Совпадения нет, не переживай - все числа случайны! Результат = ", 0)
print()
####################################################################################

time.sleep(2)                                           # Ожидаем пару секунд

######################          РУЧНОЕ УПРАВЛЕНИЕ             ######################

print("Давай теперь попробуем сами?")

count = 0                                               # Вводим счетчик

while count != 3:                                       # пока счетчик не = 3, то
    digit = False
    while digit == False:
        first = input("Введи первое число = ")          # Пользовательский ввод переменной
        if first.isdigit():                             # Если 1 переменная - Число, то
            # print("Первое число = ", first)
            print()
            digit = True                                # Переходим ко 2й переменной
            count += 1
        else:                                           # Иначе если введенное значение НЕ Число!
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