sisesta_väli = 2 #kasutaja saab defineerida mis suuruses mänguväljaga on tegu

välja_suurus = sisesta_väli * sisesta_väli #sisestatud number korrutatakse endaga, et saada mänguvälja

väli = [[0 for _ in range(sisesta_väli)] for _ in range(sisesta_väli)] #luuakse väli

for i in range(sisesta_väli): #selles osas tuleks anda väljal numbrid
    for j in range(sisesta_väli):
        väli[i][j] = 0

for read in väli: #prinditakse(praegu töö testimiseks
    print(read)
