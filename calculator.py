def sum_of_numbers(number1,number2):
    total = number1+number2
    print("Сумма чисел:",total)

def difference_of_numbers(number1,number2):
    total = number1-number2
    print("Разность чисел:",total)

def mult_of_numbers(number1,number2):
    total = number1*number2
    print("Произведение чисел:",total)

def division_of_numbers(number1,number2):
    if number2 == 0:
        message = "Делить на нуль нельзя!"
        print(message)
        return
    else:
        print("Частное чисел:",number1/number2)


while True:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))

    operation = input("Выберите операцию(+, -, /, *): " )

    if operation == '+':
        sum_of_numbers(number1,number2)
    elif operation == '-':
        difference_of_numbers(number1,number2)
    elif operation == '*':
        mult_of_numbers(number1,number2)
    elif operation == '/':
        division_of_numbers(number1,number2)

