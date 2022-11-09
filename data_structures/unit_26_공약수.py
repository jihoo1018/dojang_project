def divv():
    data = []
    for i in range(1, num1+1):
        if (num1 % i ==0)&(num2%i ==0):
            data.append(i)

    print("%d와 %d의 공약수는"%(num1,num2),data)
    print(sum(data))




if __name__ == '__main__':
    num1 = int(input("수 1 : "))
    num2 = int(input("수 2 : "))
    divv()