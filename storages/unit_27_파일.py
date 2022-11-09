def file():
    with open('./data/words.txt', 'r')as file:
        for line in file:
            words = line.split()
            for word in words:
                if'c'in word:
                    print(word.strip(',.'))

if __name__ == '__main__':
    file()
