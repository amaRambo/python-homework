from view_file import for_import

def import_fun(a):
    file = open('sem7/user.csv', 'a')
    file.write(a + '\n') 
    file.close()
    
# import_fun(for_import())