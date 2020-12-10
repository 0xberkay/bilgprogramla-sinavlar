# -*- coding: utf-8 -*-
#bisection method
import os # gerekli fonksiyonları indiriyor
os.system("pip install turtle")
os.system("pip install time")

import turtle,time

#turtle elementi
def animasyon():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")        
    wn.title("vize odevi bisection - Berkay Küçük")
    
    berkay = turtle.Turtle()
    
    berkay.pensize(4)
    berkay.color("purple")
    
    berkay.penup()
    berkay.setpos(-170,110)
    berkay.write("Berkay Küçük bisection",font=("lemon",32,"normal"))
    berkay.setpos(-50,0)
    berkay.pendown()
    
    for i in range(5):
        berkay.forward(150)
        berkay.right(144)
    time.sleep(2)   
    berkay.reset()
    #2.sayfa
    berkay.penup()
    berkay.setpos(-140,0)
    berkay.pendown()

    berkay.color("black")              
    berkay.pensize(3)                 

    berkay.right(70)
    berkay.forward(30)

    berkay.left(140)
    berkay.forward(60)

    berkay.right(70)
    berkay.forward(80)

    time.sleep(1)
    berkay.penup()
    berkay.setpos(0,0)
    berkay.setpos(-100,-30)
    berkay.write(k,font=("lemon",25,"normal"))
    time.sleep(1)
    berkay.setpos(-35,-30)
    berkay.write("sayısının kökü : {}".format(tahmin),font=("lemon",19,"normal"))
    time.sleep(1)
    berkay.setpos(-100,-90)
    berkay.write("Toplam : {} denemede buldum".format(tedas_sayaci),font=("lemon",20,"normal"))
    
    wn.exitonclick() 

#bisection methodu
k = 24 # değişken

buyuk = k 
kucuk = 0
epsilon = 0.01
tedas_sayaci = 0 
orta = (kucuk + buyuk) / 2.0

while abs((orta**2)-k) > epsilon :

	if orta**2 < k:
		kucuk = orta
	else:
		buyuk = orta
	orta = (kucuk + buyuk)/2.0
	tedas_sayaci = tedas_sayaci + 1

tahmin = orta

print(k, " sayısının kare karekökü", "yaklaşık:", tahmin) 
print("\ntoplam '{}' denemede buldum".format(tedas_sayaci))

animasyon()