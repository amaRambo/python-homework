


def s_s(word):
    f = open('sem8/magazine.txt', 'r+')
    for line in f:
        if word in line:
            print(line)
    f.close()