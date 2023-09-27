import math

UserChoice = 123
def c1(num1,num2):
    S = num1 + num2
    return S

def c2(num1,num2):
    S = num1 - num2
    return S

def c3(num1,num2):
    S = num1*num2
    return S

def c4(num1,num2):
    S = num1/num2
    return S

def c5(num1,num2):
    return num1**num2

def c6(num1):
    return math.sqrt(num1)

def c7(num1):
    return math.factorial(num1)

def c8(num1):
    return math.sin(num1)

def c9(num1):
    return math.cos(num1)

def c10(num1):
    return math.tan(num1)

def inputFunc():
    try:
        num1 = float(input())
        num2 = float(input())
        return num1, num2
    except:
        print("Скорее всего вы ввели данные неправильно")
        return 0, 0

def inputFuncInt():
    try:
        num1 = int(input())
        return num1
    except:
        print("Скорее всего вы ввели данные неправильно")
        return 0, 0
def inputFunc1():
    try:
        num1 = float(input())
        return num1
    except:
        print("Скорее всего вы ввели данные неправильно")

while UserChoice != 9:
    print("\n"
          "Выберите действие: \n"
          "1. Сложить два числа \n"
          "2. Вычесть из первого второе \n"
          "3. Перемножить два числа \n"
          "4. Разделить первое число на второе \n"
          "5. Найти степень числа \n"
          "6. Найти квадратный корень числа \n"
          "7. Найти факториал от числа \n"
          "8. Найти синус радиан \n"
          "9. Найти косинус радиан \n"
          "10. Найти тангенс радиан \n"
          "0. Прекратить программу \n")
    try:
        UserChoice = int(input())
        match(UserChoice):
            case 1:
                num1, num2 = inputFunc()
                print("Ответ: ", c1(num1,num2))
            case 2:
                num1, num2 = inputFunc()
                print("Ответ: ", c2(num1,num2))
            case 3:
                num1, num2 = inputFunc()
                print("Ответ: ", c3(num1, num2))
            case 4:
                num1, num2 = inputFunc()
                print("Ответ: ", c4(num1, num2))
            case 5:
                num1, num2 = inputFunc()
                print("Ответ: ", c5(num1, num2))
            case 6:
                num1 = inputFunc1()
                print("Ответ: ", c6(num1))
            case 7:
                num1 = inputFuncInt()
                print("Ответ: ", c7(num1))
            case 8:
                num1 = inputFunc1()
                print("Ответ: ", c8(num1))
            case 9:
                num1 = inputFunc1()
                print("Ответ: ", c9(num1))
            case 10:
                num1 = inputFunc1()
                print("Ответ: ", c10(num1))
            case 0:
                break
    except:
        print("Скорее всего вы ввели данные неправильно!")
