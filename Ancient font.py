############################   Бибилиотеки   ############################
import random
import time

##########################    Переменные    ######################################

first_tab = 0
second_tab = []
InGame = True

############################    Функции    ############################
# ====================================
def History():
    txt_1 = 'Вы отправились в путешествие на необитаемый остров '
    txt_2 = 'и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").'
    txt_3 = 'К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры. '
    txt_4 = 'Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел. '
    txt_5 = 'В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым. '
    txt_6 = 'К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, '
    txt_7 = 'где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно..."'
  
    book = [txt_1, txt_2, txt_3, txt_4, txt_5, txt_6, txt_7]
    for i in book:
        for j in i:
            print(j, end = "", flush = True)
            #time.sleep(0.03)
        print()

# ====================================
def first_section():                                    # Первая секция с генератором
    print()                                             # Отступ для наглядности текста
    
    first_tab = random.randint(3, 20)                   # Генерация первого числа
    print(first_tab)
  
    border = int(first_tab / 2)                         # Определение границы "Зеркальности"
    #print(border)
    if  first_tab % 2 == 0:                             # Если число четное
        border = border                                 # Граница равна половине числа
      
    if  first_tab % 2 != 0:                             # Если число нечетное
        border = border + 1                             # Граница равна половине числа + 1
       # print(border)
      
    for i in range(1, border):                          # Цикл для генерации зеркального числа
        count = first_tab                               # Переменная для хранения первого числа
        res = count - i                                 # Результат вычитания
        #print(first_tab, " = ", i, " + ", res)
        in_case = str(i) + str(res)                     # Преобразование в строку для дальнейшего удобства
        second_tab.append(in_case)
        
    print("=" * 30)
    print(first_tab, " = ", * second_tab, sep = "")     # Вывод результата
    second_tab.clear()


# ====================================
def second_section():
    print()
  
    print("=" * 50)
    print("Все пароли для чисел от 3 до 20 (для сверки):")
    print("=" * 50)
  
    for cntrl in range(3, 21):
        first_tab = cntrl
        #print(first_tab)
    
        border = int(first_tab / 2)
        if  first_tab % 2 == 0:
            border = border
    
        if  first_tab % 2 != 0:
            border = border + 1
    
        for i in range(1, border):
            count = first_tab
            res = count - i
            #print(first_tab, " = ", i, " + ", res)
            in_case = str(i) + str(res)
            second_tab.append(in_case)
    
        print(first_tab, " = ", * second_tab, sep = "")
        second_tab.clear()
        #print()

# ====================================
def Game():
  while InGame:
      print()
      print("=" * 50)
      print("Выберите действие:")
      print("1 - Вывести на экран расшифровку")
      print("2 - Сгенерировать игру")

  #   print("3 - Сыграть в игру")
  #   Задумка: сделать возможность сыграть в игру.
  #   Выпадает первое число, второе ручной ввод, если введено не то число, то повторяется ввод.
  #   Проверка на число или не число.
  #   После ввода числа, выводится результат
  #   на количество попыток
  #   c концом игры и результатами.
  #   создать файл сохранения, с результатами игры. Загрузки игры.

      print("3 - Выход")
      print("=" * 50)
      print()

      print()

      digit = False
      while digit == False:
          choice = input("Ваш выбор: ")
          if choice.isdigit():
              print()
              digit = True
          else:
              print("Введите число от 1 до 3: ")
              print()

      if choice == "1":
          second_section()
      elif choice == "2":
          first_section()
      elif choice == "3":
          print("Выход из игры")
          Game = False
          break

##################################################################################
####################    "Слишком древний шифр"    ################################


History()
Game()
