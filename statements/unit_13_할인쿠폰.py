def discount():
    if cash == "cash3000":
        print(price - 3000)
    elif cash == "cash5000":
        print(price - 5000)
    else:
        print(price)

if __name__ == '__main__':
    price = float(input("가격을 입력하시오: "))
    cash = input("cash3000, cash5000중 해당을 입력하시오: ")
    discount()