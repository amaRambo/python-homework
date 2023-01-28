



def add_acad(word):
    f = open('sem8/magazine.txt', 'r+')
    for line in f:
        if word in line:
            print(line)


add_acad("Piter Hooker")

