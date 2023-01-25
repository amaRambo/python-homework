



def add_acad():
    f = open('sem8/phisic.txt','r+')
    for line in f:
        a = line.split()[0].strip() + ' ' + line.split()[1].strip()
        # print(a)
        if a == 'Kevin Smith':
            f.write('3, 4 ,5')
    f.close()

add_acad()