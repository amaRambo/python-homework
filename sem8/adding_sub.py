


def add_sub(a):
    f1 = open('sem8/subjects.txt', 'a')
    with open("sem8/magazine.txt", 'r+') as f2:
        lines = list(map(lambda x: f"{{}}['{a}']\n".format(x.strip()), f2.readlines()))
        f2.seek(0)
        [f2.write(l) for l in lines]
    f1.writelines(a + '\n')
    f1.close()
    f2.close()

add_sub(input(' sada s : '))