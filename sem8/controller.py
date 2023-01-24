import view, adding_std, adding_sub

def button():
    flag = True
    while flag == True:
        a = view.viewer()
        if a == 1:
            adding_std.add_std(view.for_add_std())
        if a == 2:
            adding_sub.add_sub(view.for_add_sub())
        if a == 3:
            pass
        if a == 4:
            pass
        if a == 5:
            flag = False



        

button()