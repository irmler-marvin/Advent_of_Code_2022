if __name__ == '__main__':
    data = open("/Users/mavger22/PycharmProjects/Advent_of_Code_2022/02/data.txt")
    score = 0
    inputs_read = 0
    while True:

        read = data.readline()
        read = read[:3]

        if read == "":
            break

        inputs_read += 1

        me = read[2]

        if me == "X":
            score += 1
        elif me == "Y":
            score += 2
        elif me == "Z":
            score += 3
        else:
            Exception("invalid input")

        if read == "A Y" or read == "B Z" or read == "C X":
            score += 6
        elif read == "A X" or read == "B Y" or read == "C Z":
            score += 3

    print(f'Your score is {score}')
    print(f'(inputs read: {inputs_read})')

# part two

    data = open("/Users/mavger22/PycharmProjects/Advent_of_Code_2022/02/data.txt")
    score = 0
    inputs_read = 0
    while True:

        read = data.readline()
        read = read[:3]

        if read == "":
            break

        inputs_read += 1

        me = read[2]

        if me == "Y":
            score += 3
        elif me == "Z":
            score += 6

        if read == "B X" or read == "A Y" or read == "C Z":
            score += 1
        elif read == "C X" or read == "B Y" or read == "A Z":
            score += 2
        elif read == "A X" or read == "C Y" or read == "B Z":
            score += 3
        else:
            Exception("invalid operation")

    print(f'Your score is {score}')
    print(f'(inputs read: {inputs_read})')
