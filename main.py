import math

UserChoice = 123
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
                try:
                    num1 = float(input("Введите 1 число "))
                    num2 = float(input("Введите 2 число "))
                    print("Ответ: ", num1+num2)
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 2:
                try:
                    num1 = float(input("Введите 1 число "))
                    num2 = float(input("Введите 2 число "))
                    print("Ответ: ", num1-num2)
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 3:
                try:
                    num1 = float(input("Введите 1 число "))
                    num2 = float(input("Введите 2 число "))
                    print("Ответ: ", num1*num2)
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 4:
                try:
                    num1 = float(input("Введите 1 число "))
                    num2 = float(input("Введите 2 число "))
                    print("Ответ: ", num1/num2)
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 5:
                try:
                    num1 = float(input("Введите 1 число "))
                    num2 = float(input("Введите степень числа "))
                    print(num1**num2)
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 6:
                try:
                    num1 = float(input("Введите 1 число "))
                    print("Ответ: ", math.sqrt(num1))
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 7:
                try:
                    num1 = int(input("Введите 1 число "))
                    if num1 < 0:
                        print("Факториал нельзя найти от отрицательного числа!")
                    elif num1 == 0 or num1 == 1:
                        print("Ответ: 1")
                    else:
                        CountNum1 = 1
                        for i in range(1, num1+1):
                            CountNum1 = CountNum1 * i
                        print("Ответ: ", CountNum1)
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 8:
                try:
                    num1 = float(input("Введите число в радианах "))
                    print("Ответ: ", math.sin(num1))
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 9:
                try:
                    num1 = float(input("Введите число в радианах "))
                    print("Ответ: ", math.cos(num1))
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 10:
                try:
                    num1 = float(input("Введите число в радианах "))
                    print("Ответ: ", math.tan(num1))
                except:
                    print("Скорее всего вы ввели данные неправильно!")
            case 0:
                break
    except:
        print("Скорее всего вы ввели данные неправильно!")
