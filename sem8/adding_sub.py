


def add_sub(a):
    f1 = open('sem8/subjects.txt', 'a')
    f2 = open('sem8/magazine.txt', 'a+')
    for f2.read in f2:
        f2.writelines(str(a))
    # f1.writelines(a + '\n')
    # f1.close()
    f2.close()

add_sub(input(' sada s : '))