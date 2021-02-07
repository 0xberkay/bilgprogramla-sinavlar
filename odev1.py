# -*- coding: utf-8 -*-
# berkay küçük
import turtle
from turtle import left
print("diktörgen alan ve çevre hesaplama aracına hoş geldiniz")

print("kısa kenar giriniz")
kisakenar = input()

print("uzun kenar giriniz")
uzunkenar = input()

ks = kisakenar
uk = uzunkenar

cevre = ( int(ks) + int(uk) ) * 2
alan = int(ks) * int(uk)


def efektAlan():
    turta = turtle.Turtle()
    turtle.setup(500,500)

    dfr(turta,-100,50,200,100,5,"black","red")
    turtle.done()
def dfr(turta,x,y,width,height,size,color,fill):
    turta.fillcolor(fill)
    turta.pencolor(color)
    turta.pensize(size)
    turta.setheading(0)
    
    turta.begin_fill()
    turta.up()
    turta.goto(x,y)
    turta.down()
    
    turta.forward(width)
    turta.write(alan,font=("Lemon",35,"normal"),align="center")

    turta.right(90)
    turta.forward(height)
    
    turta.right(90)
    turta.forward(width)
    

    turta.right(90)
    turta.forward(height)
    turta.end_fill()
    turta.write("    Alan :",font=("Lemon",35,"normal"),align="center")

def efektCevre():
    turta = turtle.Turtle()
    turtle.setup(500,500)
    drr(turta,-100,50,200,100,5,"black")
    turtle.done()

def drr(turta,x,y,width,height,size,color):
    turta.pencolor(color)
    turta.pensize(size)
    turta.setheading(0)
    
    turta.up()
    turta.goto(x,y)
    turta.down()
   
    turta.forward(width)
    turta.write(cevre,font=("Lemon",35,"normal"),align="center")

    
    turta.right(90)
    turta.forward(height)
    
    turta.right(90)
    turta.forward(width)
    
    turta.right(90)
    turta.forward(height)
    turta.end_fill()
    turta.write("    Çevre :",font=("Lemon",35,"normal"),align="center")

print("")
print("alan mı hesaplamak istiyorun çevre mi ? alan için 1 çevre için 2 yazınız")
cevap = int(input())
if cevap == 2:
    efektCevre()
elif cevap == 1 :
    efektAlan()
else:
    print("cevabınızı kontrol edin")
