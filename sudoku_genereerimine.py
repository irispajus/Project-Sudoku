import random
#---------------------------------------kysi_valja_suurust---------------------------------------#
# Kasutaja saab valida, kui palju numbreid väljalt eemaldatakse
def kysi_raskusaste ():
    while True:
        sisend = input("Sisesta raskusaste (1-3) või 0 kui soovid juhuslikku raskusastet: ")
        if sisend.isdigit() and int(sisend) < 4:
            return sisend
        else:
            print("Viga raskusastme lugemisel!\n")
#---------------------------------------kysi_valja_suurust---------------------------------------#

#----------------------------------kontrollin_vaartuste_sobivust---------------------------------#
#sudoku reeglid: ühes reas ja veerus ei tohi sama number korduda
def kontrollin_vaartuste_sobivust (vali, rida, veerg, vaaartus):
    for i in range(valja_suurus): 
        for j in range(valja_suurus):
            if vali[rida][i] == vaaartus or vali[i][veerg] == vaaartus:
                return False
    #väiksemas väljas (3x3) ei tohi samuti numbrid korduda
    pisivali_suurus = int(valja_suurus ** 0.5)
    read = (rida // pisivali_suurus) * pisivali_suurus
    veerud = (veerg // pisivali_suurus) * pisivali_suurus
    for i in range(read, read + pisivali_suurus):
        for j in range(veerud, veerud + pisivali_suurus):
            if vali [i][j] == vaaartus:
                return False
    return True   
#----------------------------------kontrollin_vaartuste_sobivust---------------------------------#

#-------------------------------------------lahenda----------------------------------------------#
def lahenda (vali):
    for rida in range(valja_suurus):
        for veerg in range(valja_suurus):
            if vali[rida][veerg] == 0:
                for vaartus in range (1, valja_suurus+1):
                    if kontrollin_vaartuste_sobivust (vali, rida, veerg, vaartus):
                        vali[rida][veerg] = vaartus
                        if lahenda (vali):
                            return True
                        vali[rida][veerg] = 0
                return False
    return True
#--------------------------------------------lahenda----------------------------------------------#

#-------------------------------------------genereeri---------------------------------------------#
def genereeri (vali):
    for rida in range(valja_suurus):
        for veerg in range(valja_suurus):
            if vali[rida][veerg] == 0:
                for vaaartus in range (1, valja_suurus+1):
                    vaaartus = random.randint(1,9)
                    if kontrollin_vaartuste_sobivust (vali, rida, veerg, vaaartus):
                        vali[rida][veerg] = vaaartus
                        if genereeri (vali):
                            return True
                        vali[rida][veerg] = 0
                return False
    return True
#-------------------------------------------genereeri---------------------------------------------#

#-------------------------------------------tyhjenda----------------------------------------------#
def tyhjenda(vali, tase):
    if (int(tase) == 0):
        tase = random.randint(20, 50)
    elif (int(tase) < 5):
        tase = int(tase) * 20 + 15
    for i in range(tase):
        rida = random.randint(0, valja_suurus-1)
        veerg = random.randint(0, valja_suurus-1)
        vali[rida][veerg] = ''
    return vali
#-------------------------------------------tyhjenda----------------------------------------------#



############################################## MAIN ###############################################
def main ():
    global valja_suurus
    # Küsi kasutajalt raskusastet
    #tase = int(kysi_raskusaste())
    valja_suurus = 9 
    # Loo tühi mänguväli
    vali = [[0 for _ in range(valja_suurus)] for _ in range(valja_suurus)]
    # Täida numbritega
    genereeri(vali)
    # Eemalda numbreid vastavalt raskusastmele
    #vali = tyhjenda(vali, tase)
    #for read in vali: #prinditakse(praegu töö testimiseks)
    #    for vaartus in read:
    #        print (vaartus, end= ' ')
    #    print()
    return vali
############################################## MAIN ###############################################
#main(3)