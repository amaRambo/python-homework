# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(fComp):
    count = 1
    z = ""
    fcomp = fComp.readline()
    for i in range(len(fcomp)-1):
        if fcomp[i] == fcomp[i+1]:
            count = count + 1
        else:
            z = z + str(count) + fcomp[i] 
            count = 1
    return z + str(count) + fcomp[i] 


def recovery(fRec):
    f = fRec.readline()
    z = ""
    for i in range(0, len(f)-1, 2):
        j = 0
        while j < int(f[i]):
            z = z + f[i + 1]
            j += 1
    return z


fComp = open("comp.txt", "r")
fRec = open("rec.txt", "w")
fRec.write(compression(fComp))
fRec.close()
fComp.close()
fRec = open("rec.txt", "r")
print("Возвращаем: ", recovery(fRec))
fRec.close()




