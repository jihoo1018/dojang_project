def calc():
    add = num1 +num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div

if __name__ == '__main__':
    num1 = int(input("숫자 1: "))
    num2 = int(input("숫자 2: "))
    print(calc())