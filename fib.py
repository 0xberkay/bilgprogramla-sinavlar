# -*- coding: utf-8 -*-
#fibonacci sayıları

from renkler import * #renk modülünü import ediyoruz

terim_sayisi = int(input("""
...{} =============berkay.py====[-][o][x]
... |                                 |
... |    {} fibonacci hesaplayıcısına   |
... |           Hoş geldiniz          |
... |    kaç tane fibonacci terimi ?  |
... |          bir değer girin {} {}      |
... |                                 |
... |=================================|
...   """.format(pembe,kirmizi,sifirla,mor))) #.formatla renkleri cagirdik

ilk = 0
ikinci = 1
sayac = 0
toplam = 0
print(f"""{turkuaz} 
... ============berkay.py=====[-][o][x]
... |                                 |                    
... |   {lacivert}girdiğiniz terim sayısı: {terim_sayisi}{turkuaz}   |
... |                                 |
... |=================================|
{yesil}==>$""", end = " ") # fstringle renkleri cagırdık
while sayac < terim_sayisi:
    print(rastgeleRenkler(mavi,sari,yesil,kirmizi,beyaz,mor,pembe),ilk,end = " ") 
    # ^^rastgele renkler belirleyip yazdirdik
    toplam = ilk + ikinci 
    ilk = ikinci 
    ikinci = toplam
    sayac+=1 
print("")   

