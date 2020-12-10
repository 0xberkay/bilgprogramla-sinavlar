# -*- coding: utf-8 -*-
#fibonacci sayıları

import os
os.system('clear')# terminali temizedik
terim_sayisi = int(input("""\033[34m
... =============berkay=======[-][o][x]
... |                                 |
... |     fibonacci hesaplayıcısına   |
... |           Hoş geldiniz          |
... |    kaç tane fibonacci terimi ?  |
... |          bir değer girin        |
... |                                 |
... |=================================|
...   """))

ilk = 0
ikinci = 1
sayac = 0
toplam = 0
os.system('clear')# terminali temizedik
print("""\033[31m
... ============berkay========[-][o][x]
... |                                 |                    
... |   girdiğiniz terim sayısı: {}   |
... |                                 |
... |=================================|
==>$""""\033[28m".format(terim_sayisi), end = " ")
while sayac < terim_sayisi:
    print(ilk,end = " ") 
    toplam = ilk + ikinci 
    ilk = ikinci 
    ikinci = toplam
    sayac+=1 
print("")    