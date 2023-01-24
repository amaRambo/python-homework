



def mag_gen():
    f1 = open('sem8/magazine.txt', 'w')
    f2 = open('sem8/students.txt', 'r')
    f3 = open('sem8/subjects.txt', 'r')
    name = ''
    subject = ''
    a = True
    b = True
    while a:
        b = True
        name = f2.readlines()
        if not name:
            a = False
        f1.write(str(name))
        while b:
            subject = f3.readlines()
            if not subject:
                b = False
            f1.write(str(subject))
    f1.close()
    f2.close()
    f3.close()
 
mag_gen()