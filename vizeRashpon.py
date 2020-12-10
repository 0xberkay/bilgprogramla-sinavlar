# -*- coding: utf-8 -*-

#bisection method

import os # gerekli fonksiyonları indiriyor
os.system("pip install turtle")
os.system("pip install time")
import turtle,time

def animasyon():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")        
    wn.title("vize odevi Newton-Raphson - Berkay Küçük") #penceredeki ismi
    
    berkay = turtle.Turtle() #turtelı berkaya tanımladım :)
    
    berkay.pensize(4)
    berkay.color("purple")
    
    berkay.penup()
    berkay.setpos(-270,110)
    berkay.write("Berkay Küçük Newtoon-rashpon",font=("lemon",32,"normal")) #baslık
    berkay.setpos(-50,0)
    berkay.pendown()
    
    def kardanAdam(color, radius, x, y): # kardan adam 
        berkay.penup()
        berkay.fillcolor(color)
        berkay.goto(x,y)
        berkay.pendown()
        berkay.begin_fill()
        berkay.circle(radius)
        berkay.end_fill()   
 
    
    kardanAdam("#ffffff", 30, 0, -40)
    kardanAdam("#ffffff", 40, 0, -100)
    kardanAdam("#ffffff", 60, 0, -200)
    kardanAdam("#ffffff", 2, -10, -10) 
    kardanAdam("#ffffff", 2, 10, -10) 
    kardanAdam("#FF6600", 3, 0, -15) 
    kardanAdam("#ffffff", 2, 0, -35)
    kardanAdam("#ffffff", 2, 0, -45)
    kardanAdam("#ffffff", 2, 0, -55)
    
    berkay.penup()
    berkay.goto(-15,-35)
    berkay.pendown()
    berkay.pensize(5)
    berkay.goto(-75, -50)
    berkay.penup()
    berkay.goto(15,-35)
    berkay.pendown()
    berkay.pensize(5)
    berkay.goto(75, -50)

    time.sleep(2)   
    berkay.reset()
    #2.sayfa
    berkay.penup()       #karekök işareti
    berkay.setpos(-200,0)
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
    berkay.setpos(-160,-30)
    berkay.write(k,font=("lemon",25,"normal")) # k sayısını yazdırıyor
    time.sleep(1)
    berkay.setpos(-85,-30)
    berkay.write("sayısının kökü : {}".format(tahmin),font=("lemon",17,"normal")) #tahmin degerini yazdırıyor
    time.sleep(1)
    berkay.setpos(-160,-90)
    berkay.write("Toplam : {} denemede buldum".format(tedas_sayaci),font=("lemon",20,"normal")) # sayac değerini yazdırıyor
    
    wn.exitonclick() 


#method
tedas_sayaci = 0 #sayaç
epsilon = 0.01 # aralık

k = 24.0  # değişken

tahmin = k/2.0 

while abs(tahmin*tahmin - k) >= epsilon: 

    tedas_sayaci += 1 

    tahmin = tahmin - (((tahmin**2) - k)/(2*tahmin)) 

print(k, " sayısının kare karekökü", "yaklaşık:", tahmin) 
print("\ntoplam '{}' denemede buldum".format(tedas_sayaci)) 

animasyon() # animasyon çağrılıyor