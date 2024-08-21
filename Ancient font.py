import random

first_tab = 0
second_tab = []


def first_section():
    print()
    
    first_tab = random.randint(3, 20)
    print(first_tab)
  
    border = int(first_tab / 2)
    #print(border)
    if  first_tab % 2 == 0:
        border = border
      
    if  first_tab % 2 != 0:
        border = border + 1
       # print(border)
      
    for i in range(1, border):
        count = first_tab
        res = count - i
        #print(first_tab, " = ", i, " + ", res)
        in_case = str(i) + str(res)
        second_tab.append(in_case)
        
    print("=" * 30)
    print(first_tab, " = ", * second_tab, sep = "")



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


second_section()
first_section()
