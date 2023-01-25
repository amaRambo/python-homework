



def mag_gen():
    f1 = open('sem8/magazine.txt', 'w+')
    f2 = open('sem8/students.txt', 'r+')
    f3 = open('sem8/subjects.txt', 'r+')

    a = ''
    for f3.read in f3:
        c = f3.read.splitlines()
        a = a + str(c)

    for f2.read in f2:
        g = f2.read.splitlines()
        f1.write(str(g) + str(a) + '\n')
    f1.close()
    f2.close()
    f3.close()
mag_gen()                                                            