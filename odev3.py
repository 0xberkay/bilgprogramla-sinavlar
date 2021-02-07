## 6. Write a program that asks the user to input 10 integers, and
# then prints the largest odd number that was entered. If no odd number was
# entered, it should print a message to that effect.

# Kullaniciya 10 adet tamsayi isteyen ve girilen sayilar icindeki en buyuk tek 
# sayiyi yazdiran programi yaziniz. Eger hic tek sayi girilmemisse bir mesajla
# tek sayi girilmedigini belirtiniz.

sayi = None
for _ in range(10):
    deger = int(input('Bir deger giriniz: '))
    if (deger % 2 and (sayi is None or deger > sayi)):
        sayi = deger
if sayi:
    print('Girilen en buyuk sayi', sayi)
else:
    print('Tek sayi bulunamadi.')