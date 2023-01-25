



# def create_sub(inp):
#     a = inp + ".txt"
#     f1 = open(f'sem8/{a}', "w+")

#     f1.close


def std_sub(inp):
    a = inp + ".txt"
    f1 = open('sem8/students.txt', 'r')
    f2 = open(f'sem8/{a}', "w")
    for line in f1:
        f2.write(line)
    f1.close
    f2.close

# inp = 'phisic'
# create_sub(inp)
# std_sub(inp)