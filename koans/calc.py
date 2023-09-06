while True:
    try:
        num1 = float(input("enter the first number:"))
        num2 = float(input("enter the second number:"))
        cal =input("enter the calculation type:")
        if cal == '+':
            output = num1 + num2
            print(f'sum:{num1} {cal} {num2} = {round(output,2)} ')
        elif cal == '-':
            output = num1 -num2
            print(f'subs:{num1} {cal} {num2} = {round(output,2)} ')
        elif cal == '/':
            output = num1 /num2
            print(f'div:{num1} {cal} {num2} = {round(output,2)} ')
        elif cal == '*':
            output = num1 *num2
            print(f'mul:{num1} {cal} {num2} = {round(output,2)} ')
        else:
            print("Please enter a valid operation ")


    except ZeroDivisionError:
        print("cannot divide by 0")
    except ValueError:
        print("Invalid input")

    except KeyboardInterrupt:
        print("out of loop")
        exit()