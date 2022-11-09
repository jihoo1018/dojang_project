def average():
    return (ko+en+ma)/3

if __name__ == '__main__':
    ko = int(input("국어 성적을 입력하시오: "))
    en = int(input("영어 성적을 입력하시오: "))
    ma = int(input("수학 성적을 입력하시오: "))
    print(average())
