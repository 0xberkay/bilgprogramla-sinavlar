# -*- coding: utf-8 -*-


try: #renkler var mı diye bakıyorum 
    from renkler import *
    #import olmazsa pip install renk
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'renk'])
    from renkler import *  #kendi yaptığım renk kütüphanesini import ediyirom https://github.com/bksec/renkler 

try: #terminaltables var mı diye kontrol ediyorum 
    from terminaltables import *
    #import olmazsa pip install terminaltables
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'terminaltables'])
    from terminaltables import *  #Tablo kütüphanesini import ediyorum
try: #terminaltables var mı diye kontrol ediyorum 
    import matplotlib.pyplot as plt 
    import matplotlib as mpl
    #import olmazsa pip install matplotlib
except ImportError: #matplotlib varmı diye kontrol ediyorum
    from pip._internal import main as pip # 7.sorudaki kullandığım kütüphane
    pip(['install', '--user', 'matplotlib'])
    import matplotlib.pyplot as plt 
    import matplotlib as mpl

        
import os,time # os kütüphanesi ve time  import ettim
def sil(): # bazı yerlerde güzel görünsün diye üsteki yazılan değerleri silmek için modül yazdım
    sistem = os.name #işletim sisteminizi öğrendim

    if os.name == 'nt': #windows için
        sil = os.system('cls') #terminal temizleme komutu
    else: #linux için
        sil = os.system('clear') #terminal temizleme komutu
    sil 



# In[1]:
                             ## PROBLEMLER 


###
### Problem 1 Sözlukler (20 Puan)
###

# Spesifikasyonuna göre aşağıdaki kayıt birleştir fonksiyonunu yazınız.

def kayit_birlestir(d1, d2):#fonksiyon

# Cevap


    birlesmis_sozluk = {} # boş bir sözlük oluşturuyorum

    for anahtar in d1: # d1 içinde  her anahtar için
        if anahtar in d2: # eğer anahtar d2deyse
            yeni_deger = [d1[anahtar][0] + d2[anahtar][0] , d1[anahtar][1] + d2[anahtar][1]] # yeni değer = anahtar d1 ve d2 nin elamanlarının toplamı yapıyorum 
        else:# eğer anahtar d2de değilse
            yeni_deger = d1[anahtar] #  yeni değere d1in anahtarını ekliyorum

        birlesmis_sozluk[anahtar] = yeni_deger #birleşmiş sözlüğe yeni değeri ekliyoruz

    for anahtar in d2:# d1 içinde  her anahtar için
        if anahtar not in birlesmis_sozluk: # eğer anahtar birleşmiş sözlükte değilse 
            birlesmis_sozluk[anahtar] = d2[anahtar] #d2 yi birleşmiş sözlüğe  eşitliyorum

    return birlesmis_sozluk # birleşmiş sözlüğü return ediyoruz


def birSoru(): # SORUYU ÇALIŞTIRMAK İÇİN  ==> birSoru()    
    import vur # küçük bir vurma animasyonu ana dizin vur.py
    d1 = {"GS": [8,1], "FB": [6,3] } # D1 sözlüğümüz
    d2 = {"GS": [2,0], "BJK": [5,4] } # D2 sözlüğümüz

    print(f"{kirmizi} {d1} + {d2} =  {kayit_birlestir(d1,d2)} {sifirla}") #sözlükleri fonksiyonda çağırar print ettiriyorum 
    #ve renk kütüpyanesini kullanıyorum
#birSoru()  #çalıştırma komutu

# In[2]:

###
### Problem 2 While Döngüleri  (15 Puan)
###
# Cevap
#


def gerisayim_n(dan_gerisay, kadar_gerisay):
    for i in range(dan_gerisay-(dan_gerisay%kadar_gerisay),-1,-kadar_gerisay): #dan gerisaydan başlayıp diziyi -kadar gerisay kadar artırıp dan gerisayın kadar ggerisayına göre modunu alıp döngü oluşturuyorum 
            print(rastgeleRenkler(mavi,kirmizi,sari,mor,pembe,yesil,beyaz,gri,lacivert,turuncu),i,sifirla) # kendi renkler kütüphanemi kullanarak rastgele renkler oluşurup sayıları print ediyorum
def ikiSoru(): #ikinciyi soruyu çalıştırmak için ikiSoru()
    print(f"{kirmizi}16 dan geriye doğru 5 er 5 er")
    gerisayim_n(16, 5) # fonksiyu değerlerle çağıryorum 
    print(f"{kirmizi}21 dan geriye doğru 7 şer 7 şer")
    gerisayim_n(21, 7) # fonksiyu değerlerle çağıryorum 
#ikiSoru() kodu çalıştırmak için



# In[3]:

###
### Problem 3 Test etme ve istisnalar/Exceptions  (10 Puan)
###


def buyuk_kucuk_harf(s): #fonksiyonumuz
    bos = "" #boş bir str atıyorum
    kosul = str(s) #koşulumuz str olması
    
    for i in kosul: # koşuldaki her i için 
        if i == i.upper(): # eğer i büyük karakterse
            i = i.lower() # i yi büyük karakter yapıyoruz
            bos += i # boşada onu ekliyoruz
              
        elif i == i.lower(): # eğer i küçük karakterse
            i = i.upper() #i yi büyük karakter yapıyoruz
            bos += i  # boşada onu ekliyoruz
              
    return bos # boşu return ediyoruz


def soru3():
        
    ilk_girdi = r"" #boş girdi girip nolduğuna bakıyoruz çünkü Bos liste her zaman önemlidir
    ilk = buyuk_kucuk_harf(ilk_girdi)
    ilk_nedeni = "Bos liste her zaman önemlidir"
    
    iki_girdi = r"RUBYONRAILS" #Büyük harflerde çalışıyor mu diye test ediyoruz
    iki = buyuk_kucuk_harf(iki_girdi) #bi sorun yok
    iki_nedeni = "Büyük harflerle çalışıyor mu kontrolü" 
    
    uc_girdi = r"tatarböreği" #küçük harflerde çalışıyor mu diye test ediyoruz
    uc = buyuk_kucuk_harf(uc_girdi)#bi sorun yok
    uc_nedeni = "Küçük harflerle çalışıyor mu kontrolü"    
    
    dort_girdi = r"01100001" # sayılarda çalışıyor mu diye test ediyoruz
    dort = buyuk_kucuk_harf(dort_girdi)#bi sorun yok
    dort_nedeni = "Sayılarla çalşıyor mu kontrolü"    
    
    bes_girdi = r"¯\_(ツ)_/¯" # karakterlerde çalışıyor mu diye test ediyoruz
    bes = buyuk_kucuk_harf(bes_girdi)#bi sorun yok
    bes_nedeni = "Karakterlerle çalışıyor mu kontrolü"   
     
    alti_girdi = r"\n\t" # kaçış karakterlerine bakıyoruz n ve t yi büyültecek mi diye
    alti = buyuk_kucuk_harf(alti_girdi)#bi sorun yok
    alti_nedeni = "Özel kaçışlarda çalışıyor mu"    
     
# tablo yapmak için kullandığım kütüphane       
#bir tablo oluşturuyorum kütüphanin fonksiyonuyla her eleman yeni hücre yapıyor
# ilk sıra başlıklar oluyor
    table_data = [
        ["sıra","   Girdi","   Çıktı","              Nedeni"],
        ["1.",ilk_girdi,ilk,ilk_nedeni],
        ["2.",iki_girdi,iki,iki_nedeni],
        ["3.",uc_girdi,uc,uc_nedeni],
        ["4.",dort_girdi,dort,dort_nedeni],
        ["5.",bes_girdi,bes,bes_nedeni],
        ["6.",alti_girdi,alti,alti_nedeni]
    ]
    table = DoubleTable(table_data) # tableye tablomuzu atıyorum
    
    print(table.table)

#testetme() 3.soruyu çalıştırıyorum

    

# In[4]:

###
### Problem 4 Nesneler ve Terminoloji  (10 Puan)
###

# Aşağıdaki A ve B sınıflarının tanımını kullanarak, devamındaki soruları bos 
# bırakılan yere satır numarasını yazarak cevaplandırın. Bir kaç doğru cevap 
# olabilir, SADECE 1 tanesini yazın.

#1. class A():
#2.     x = 1
#3.     def __init__(self, n):
#4.         self.y = n
#5.         A.x += 1
#6.     def p(self):
#7.         print(self.y)
#8.         self.y += 3
#9.         self.r()
#10.     def r(self):
#11.         self.y += 2
#12.         print(self.y)
#13. class B(A):
#14.     x = 10
#15.     def __init__(self, n):
#16.         super().__init__(n)
#17.         sum = self.y + B.x
#18.         self.m = sum
#19.     def r(self):
#20.         self.y += self.x
#21.         print(self.m)
#22. a = A(1)
#23. b = B(2)
#24. a.p()
#25. b.p()
def soru4():
    print(
    f"""Cevaplar {pmavi}
    -------- 

    a. Satır 3 de/da bir nesne niteligi yaratılır 
    b. Satır 14  de/da bir sınıf niteliği yaratılır 
    c. Satır 1 de/da bir ustsınıf tanımı baslar 
    d. Satır 6 de/da bir sınıf metodu baslar 
    e. Satır 16 de/da bir metot tanımı ustu yazılmaya/override başlanır

    """)

# soru4()    

# In[5]:

###
### Problem 5 Nesne yaratma ve for döngüleri  (25 Puan)
###

# Aşağıdaki Menu ve Kahvalti sınıf kodlarını göz önüne alarak.

class Menu():
    """Bir örnek nesne/instance menüde bir yemeği temsil eder."""
    
    def __init__(self, isim, vejetaryen_mi, fiyat):
        self.isim = isim
        self.vejetaryen_mi = vejetaryen_mi
        assert fiyat > 0
        self.fiyat = fiyat
        
class Kahvalti(Menu):
    def __init__(self, isim, vejetaryen_mi, fiyat, kahvalti_fiyati):

        Menu.__init__(self, isim, vejetaryen_mi, fiyat)
        assert kahvalti_fiyati > 0
        assert kahvalti_fiyati <= 10
        
        self.kahvalti_fiyati = kahvalti_fiyati
    

# a). 

# Cevap 
# animasyon oluşturmak için 2 tane ascii döneri yaptım .formatla renk ekledim
a = ("""{}
                                         ▐██▌
                                      ▐███
                                      ▐███
                                      ████,  {}
                         ╓████████████████████████████▄
                         ██████████████████████████████
                         ▐█████████████████████████████
                         └▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████████████▌
                                          ╓███████████`
                          ████████████████████████████
                          ▐███████████████████████████
                          ]██████████████████████████▌
                           ██████████████████████████`
                           █████████████
                           ▐████████████████████████▌
                           ▐████████████████████████▌
                            ████████████████████████`
                            ████████████████████████
                                          ▀█████████
                            ┌▄▄▄▄▄▄▄▄▄▄▄▄▄█████████▌
                             ██████████████████████`
                             ██████████████████████
                             ▓█████████████████████
                             ▐██████████▀▀
                              ██████████▄
                              ████████████████████
                              ▐███████████████████
                              ╙██████████████████▌
                                ▀▀▀▀▀▀████▀▀▀▀▀▀    {}
                                      ▐███
                                      ▐███
                                      ▐███""".format(siyah,kahverengi,siyah))
a1 = ("""{} 
                                    ▐██▌
                                      ▐███
                                      ▐███
                                      ████,
                       {} ╓████████████████████████████▄
                         ██████████████████████████████
                         ▐█████████████████████████████
                        ▀█████████████████████
                         ╓███████████████████
                          ████████████████████████████
                          ▐███████████████████████████
                          ]██████████████████████████▌
                           ██████████████████████████`
                                        █████████████
                           ▐████████████████████████▌
                           ▐████████████████████████▌
                            ████████████████████████`
                            ████████████████████████
                            ▀█████████████████▌
                            ▄██████████████████
                             ██████████████████████`
                             ██████████████████████
                             ▓█████████████████████
                                    ███████████████
                                    ███████████████
                              ████████████████████
                              ▐███████████████████
                              ╙██████████████████▌
                                ▀▀▀▀▀▀████▀▀▀▀▀▀    {} 
                                      ▐███
                                      ▐███
                                      ▐███""".format(siyah,kahverengi,siyah))






def donerye():#animasyon
    bar = [ #bir bar listesi oluşturp 2 döneride ekledim 
        a,
        a1

]
    i = 0 # sayaç

    while i<20: # döngü yaptım
        sil()   # yukardakı sil fonkumu çağırdımki önceki print gözükmesin
        print(bar[i % len(bar)], end="\r") #aynı satır başı şeklinde barı printliyorum
        time.sleep(0.3) #sleep fonksiyonu 0.3 delay için
        i += 1  #sayaç
def besAsikki():
    donerye() # döner pişti :)

    yemek1 = Menu("doner",False,24) #yemek menüsünü örneklendiriyorum ve onu yemek1 e atıyorum
    print(f"{kirmizi}Seçilen yemek:{sari} {yemek1.isim},{yesil} Müşteri Vejetaryan mı ?{kirmizi} {yemek1.vejetaryen_mi},{siyah} Ücret: {yemek1.fiyat}{sifirla}") #örneklendirilmiş yemek1 i print ediyorum
    # Ve renk kütüphanemi kullanıyorum

#besAsikki()


# b).


# Cevap



def besBsikki():   
    yemek2 = Kahvalti("Mantarlı Omlet",True,12,8) #kahvaltı menüsünü örneklendiriyorum    
    print(f"{kirmizi}Seçilen yemek: {sari}{yemek2.isim},{yesil} Müşteri Vejetaryan mı ?{kirmizi} {yemek2.vejetaryen_mi},{siyah} Ücret normal: {yemek2.fiyat} {beyaz}Ücret Kahvaltı: {yemek2.kahvalti_fiyati}{sifirla}")
    #kendi renk kütüphanemle değerleri print ediyorum
    print(f"""{sari}
                    .......__
                 ."           ".
                :               :
                :               :
                 `.._________..'
                      :   :
                      :   :
                      :   :
                      `...'        
                
      ,'"`.    
     /     \   
    :       :                       ___
    :       :                    _-"_-"
     `.___,'                   _-_-"
                             _-_-"
  _______________________  -"-"_
  \                          /
   \                        /   
.--_\______________________/_--.
 ""--------------------------""

{sifirla}
            """  )#tava ve yumurta resmi print ediyorum




# c).

# Cevap
#
def besCsikki():
    yemek2 = Kahvalti("Mantarlı Omlet",True,12,8)#kahvaltı menüsünü örneklendiriyorum
    yemek2.kahvalti_fiyati = 50 #kahvaltı_fiyatı 50 ye eşitliyorum ki assetesi aşabileyim
    print(f"{kirmizi}yemek2'nin yeni kahvaltı fiyatı : {yemek2.kahvalti_fiyati},{sifirla}") # ahvaltı_fiyatı print ediyorum
    print(f""" {sari}                                  
                                                                                
                                  %@@.                                          
                                  %@@.                                          
                                  %@@,     @@@,                                 
                                  %@@@@@@@@@@                                   
                              .@@@@@@@@      .*                                 
                            @@@@. %@@, @@@@@@@,                                 
                                 @@@@@@@@                                       
                            @@@@@@@@@.                                          
                            (     %@@.           @@@                            
                                  %@@,           @@@                            
                                  %@@,          @@@.                            
                                  %@@.         @@@                              
                                  %@@,      /@@@@                               
                                  %@@,  &@@@@@                                  
                                  %@@@@@@@@      {sifirla}
    """)

#besCsikki()

# d).

def menu_denetle(ornek_menu): #metotot tanımladık
    for x in range(len(ornek_menu)): # ornek_menu deki elaman sayısı kadar print ettiriyoruz
        if type(ornek_menu[x]) is Kahvalti: # eğer örnek menü kahvaltı classındansa
            print(f"{mavi}örnek menünün{yesil} {x}.{mavi} elemanı kahvaltı menüsü") #örnek menün x elamanın kahvaltı olduğunu print ettiriyorum
            #x + 1 yazmamın sebebi 0 dan başlamasında 1 den başlasın print etmeye
            if ornek_menu[x].kahvalti_fiyati==11:# eğer örnek 1 in kahvaltı_fiyatı 11 e eşitse
                print(f"{mavi}örnek menünün {yesil}{x}.{mavi} elemanının kahvaltı fiyatı 11'e eşit")#örnek menün x elemanı 11 eşit olduğunu print ettiriyorum 
                ornek_menu[x].kahvalti_fiyati = 9 # örnek menünün x elamının kahvalti fiyatını 9 yapıyorum
                print(f"{mavi}örnek menünün{yesil} {x}.{mavi} elemanının kahvaltı fiyatı 9 yapıldı ") # yapılan şeyi print ediyorum
            elif ornek_menu[x].kahvalti_fiyati>11: # eğer kahvaltı fiyatı 11 den büyükse 
                print(f"{mavi}örnek menünün{yesil} {x}.{mavi} elamının kahvaltı fiyatı{yesil} {ornek_menu[x].kahvalti_fiyati}{mavi} ve 11 den büyük") # kahvaltı fiyatının 11den büyük olduğunu print ediyorum     
                adi = "sunulmayan_yemek" # yeni ad beliledim
                vejataryan_kontrol=ornek_menu[x].vejetaryen_mi #vejataryanın olup olmadığını aynen alıyorum
                parasi = ornek_menu[x].kahvalti_fiyati #parisi değerini kahvalti_fiyarı değerine eşitliyorum 
                sunulmayan = Menu(adi,vejataryan_kontrol,parasi) #örneklediriyorum fiyatı kahvaltı_fiyatı olarak belirledim değişmek için yukarıdaki yeri fiyat olarak almalıyız
                ornek_menu[x] = ornek_menu.append(sunulmayan) #Ve önceki örneklendirmeyle bunu değişiyorum istersek ek elaman diyede ekliyebilriz
                print(f"{mor}yeni bir yemek menüsü oluşturuldu") # ve olaylırın olduğunu print ediyorum
                  
        else: # kahvaltı classından değilse
            print(f"{mavi}örnek menünün{yesil} {x}.{mavi} elemanı kahvaltı sınıfından değil{sifirla}") # kahvalti sınıfından olmadığını print ediyorum



def besDsikki(): 
    yemek3 = Kahvalti("Patates Ekmek",True,14,7)#yemek3 diye yeni bir örneklendirme oluşturdum
    yemek3.kahvalti_fiyati = 11 #kahvaltı_fiyatı 11 ye eşitliyorum ki assetesi aşabileyim
    yemek4 = Kahvalti("pide",True,12,8) #yemek4 diye yeni bir örneklendirme oluşturdum
    yemek4.kahvalti_fiyati = 30 #kahvaltı_fiyatı 30 a eşitliyorum ki assetesi aşabileyim
    yemek5 = Menu("doner",False,24)#yemek5 diye yeni bir örneklendirme oluşturdum
    ornek_menu = [yemek3,yemek4,yemek5] #Listeye örneklendirmeleri ekliyorum
    menu_denetle(ornek_menu)#fonksiyona örnek mneüyü veriyoruz
#besDsikki() #çalıştırmak için


# In[6]:

###
### Problem 6 Stringler ve Sayaçlar (10 Puan)
###
def altiSoru():
    sil() #yukardaki sil fonksiyonu çağırdım
    liste = [] # boş bir liste tanımladım
    cift_sayısı = 0  # çift sayısını sıfır yapıyoruz
    # girdi olarak eleman sayısı tanımlıyoruz
    n = int(input(f"{kirmizi}Kaç tane sayıyı test etmek istiyorsunuz :{turuncu} ")) 
    print(f"\n{pkirmizi}test etmek istedğiniz sayıları enterlayın")  
    # n aralığa kadar yineliyorum
    for i in range(0, n): 
        #input alıyorum her input rastgele renk oluyor 
        eleman = int(input(f"{rastgeleRenkler(mavi,mor,yesil,sari,beyaz,turuncu,pembe,gri)}")) #kütüphanamdeki rastgele renk yazdırma fonksiyonu

        liste.append(eleman) #eleman ekliyor 
        
    for num in liste: #listede her num öğesi için
        if num %2 == 0: # eğer 2 ile kalanı 0 ise
            cift_sayısı += 1 # çift sayı yerine bir ekliyorum

    print(f"{yesil}toplam çift sayınız:",pyesil,cift_sayısı,sifirla) # çift sayı sayısını yazdırıyorum
#altiSoru()



# In[7]:


# Cevaplar
#


class cember: #çember sınıfı
    def __init__(self,k, x, y, r): # nesne niteliklerini giriyoruz
        self.r = r #bu şekilde sınıfımızın başka yerlerindede bunları kullanabilir hale getiriyoruz
        self.x = x
        self.y = y
        self.k = k
        print(f"çizgi kalınlığı: {k} X Konumu: {x} Y Konumu {y} YarıÇapı {r}") #nesne niteliklerini print ediyoruz
        fig = plt.figure() #pylotdaki figure fonksiyonu kullanıyoruz
        ax = fig.add_subplot(111, xlim=(-100, 100), ylim=(-100, 100))# gösterilicek alan yerini ayarlıyoruz
        c = ax.add_patch(plt.Circle((x, y), radius=r)) #Çemberin özelliklerini giriyoruz
        transform = mpl.transforms.Affine2D().translate(-5,-5) #TransformNode ağacına göre ölçüleri Affine2Dye ayarlıyoruz
        transform += mpl.transforms.Affine2D().translate(10,10) # affinde2d = https://au.mathworks.com/help/images/ref/affine2d.html
        c.set_transform(transform+ax.transData) # dönüşümü setliyoruz
        ax.set_aspect('equal') #y nin xe göre oranını setliyoruz
        plt.title(f"çizgi kalınlığı: {k} X Konumu: {x} Y Konumu {y} YarıÇapı {r}") # başlık giriyoruz
        plt.grid(True) # kareli olmayı açıyorum
        plt.show() # gösteriyorum
        
    
    def yaricap(self):# yarıçapı döndürmek için getter methodu    
        return self.r # r yi return ediyoruz
        
    
    def yaricap(self, val): # setterla yarıçapı değişiyoruz
        self.r = val #r yi val yapıyoruz
        
        print(f"yeni yarıçapı: {val}") # yeni yarı çapı print ediyoruz
        fig = plt.figure() #pylotdaki figure fonksiyonu kullanıyoruz
        ax = fig.add_subplot(111, xlim=(-100, 100), ylim=(-100, 100)) # gösterilicek alan yerini ayarlıyoruz
        c = ax.add_patch(plt.Circle((10, 15), radius=val)) #Çemberin özelliklerini giriyoruz
        transform = mpl.transforms.Affine2D().translate(-5,-5) #TransformNode ağacına göre ölçüleri Affine2Dye ayarlıyoruz
        transform += mpl.transforms.Affine2D().translate(10,10)# affinde2d = https://au.mathworks.com/help/images/ref/affine2d.html
        c.set_transform(transform+ax.transData) # dönüşümü setliyoruz
        ax.set_aspect('equal')#y nin xe göre oranını setliyoruz
        plt.title(f"Yeni YarıÇapı {val}")  # başlık giriyoruz
        plt.grid(True) # kareli olmayı açıyorum
        plt.show() # gösteriyorum
        
        
def yediSoru():#yedinci soruyu çağırmak için
    t = cember(2,10, 15 ,50) #nesne niteliklerini ekliyruz   
    t.yaricap(20) # yeni yarıçapı setterla ekliyoruz
#yediSoru()


def basla(): #küçük bir giriş animasyonu
    sil()
    isim=[
    ":::::::::  :::::::::: :::::::::  :::    :::     :::   :::   ::: ",
    ":+:    :+: :+:        :+:    :+: :+:   :+:    :+: :+: :+:   :+: ",
    "+:+    +:+ +:+        +:+    +:+ +:+  +:+    +:+   +:+ +:+ +:+  ",
    "+#++:++#+  +#++:++#   +#++:++#:  +#++:++    +#++:++#++: +#++:   ",
    "+#+    +#+ +#+        +#+    +#+ +#+  +#+   +#+     +#+  +#+    ",
    "#+#    #+# #+#        #+#    #+# #+#   #+#  #+#     #+#  #+#    ",
    "#########  ########## ###    ### ###    ### ###     ###  ###    ",
    ":::    ::: :::    :::  ::::::::  :::    ::: :::    :::",          
    ":+:   :+:  :+:    :+: :+:    :+: :+:    :+: :+:   :+: ",          
    "+:+  +:+   +:+    +:+ +:+        +:+    +:+ +:+  +:+  ",          
    "+#++:++    +#+    +:+ +#+        +#+    +:+ +#++:++   ",          
    "+#+  +#+   +#+    +#+ +#+        +#+    +#+ +#+  +#+  ",          
    "#+#   #+#  #+#    #+# #+#    #+# #+#    #+# #+#   #+# ",          
    "###    ###  ########   ########   ########  ###    ###", 
    ]

    don = 0
    while don < 6: # kaç kere dönceğini ayarlıyoruz
        sil()
        print(" ")
        time.sleep(0.1)
        a = rastgeleRenkler(mavi,turuncu,sari,beyaz,yesil,mor,kirmizi,yesil,pembe) # renk kütüphanem
        for i in isim: #isim listesini döndürüyor
            print(a,i)
            time.sleep(0.09)
        don += 1    #sayaç
    print(sifirla)
    time.sleep(0.03) 
       


def konsol(): #konsol fonksiyonumuz küçük bir cui
   # kullanıcıdan değer alıp üsteki soruları çalıştırıyorum
    a = """ {}
  +==========================================================[-][o][x]
  |                                                                  |
  |           1.Soru için == 1        2.soru için == 2               |
  |                                                                  |
  |           3.soru için == 3        4.soru için == 4               |
  |                                                                  |
  |           5.soru için                                            |
  |                                                                  |
  |           a şıkkı == 5a           b şıkkı == 5b                  |
  |                                                                  |
  |           c şıkkı == 5c           d şıkkı == 5d                  |
  |                                                                  |
  |           6.soru için == 6        7.soru için == 7               |
  |                                                                  |
  |    vidyoyu açmak için == v                                       |
  |     _____________________|      |____________________________    | 
  |         ,--.    ,--.          ,--.   ,--.                        |     
  |        |oo  | _  \  `.       | oo | |  oo|                       | 
  |    o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o       | 
  |        |/\/\|   '._,'        |/\/\| |/\/\|                       | 
  |    _____________________         _____________________________   | 
  |                         |        |                               |    
  | Menüyü tekrar görmek için = m          Çıkmak için q             |                               
  +==================================================================+{}
    """.format(mor,sifirla)
    print(a)
    dongu = True
    while dongu:
        
        cevap = str(input(f"{mavi}Hangi soruyu çalıştırmak istiyorsunuz ? "))
        
        if cevap == "1":    
            sil()
            print("")
            print(f"{kirmizi}1.soru birazdan başlatılacak")
            time.sleep(1)
            birSoru()
        elif cevap == "2":    
            sil()
            print("")
            print(f"{kirmizi}2.soru birazdan başlatılacak")
            time.sleep(1)
            sil()
            ikiSoru()
        elif cevap == "3":    
            sil()
            print("")
            print(f"{kirmizi}3.soru birazdan başlatılacak")
            time.sleep(1)
            sil()
            soru3()
        elif cevap == "4":    
            sil()
            print("")
            print(f"{kirmizi}4.soru birazdan başlatılacak")
            time.sleep(1)
            sil()
            soru4()    
        elif cevap == "5a":    
            sil()
            print("")
            print(f"{kirmizi}5.soru a şıkkı birazdan başlatılacak")
            time.sleep(1)
            sil()
            besAsikki()
        elif cevap == "5b":
            sil()
            print("")
            print(f"{kirmizi}5.soru b şıkkı birazdan başlatılacak")
            time.sleep(1)
            sil()
            besBsikki()
        elif cevap == "5c":
            sil()
            print("")
            print(f"{kirmizi}5.soru c şıkkı birazdan başlatılacak")
            time.sleep(1)
            sil()
            besCsikki()  
        elif cevap == "5d":
            sil()
            print("")
            print(f"{kirmizi}5.soru d şıkkı birazdan başlatılacak")
            time.sleep(1)
            sil()
            besDsikki()                     
        elif cevap == "6":
            sil()
            print("")
            print(f"{kirmizi}6.soru birazdan başlatılacak")
            time.sleep(1)
            sil()
            altiSoru()      
        elif cevap == "7":
            sil()
            print("")
            print(f"{kirmizi}7.soru birazdan başlatılacak")
            time.sleep(1)
            sil()
            yediSoru()      
        elif cevap == ("m"):
            sil()
            print(a)
            time.sleep(1)
        elif cevap == ("v"): #hocam console olarak cmd kullanıyorsanız çalışcaktır sadece
            os.system("start https://youtu.be/R0tqoGqHHo8")   
        elif cevap == "q":
            dongu = False
            sil()
            print(f"""{siyah}
            ooOOOO  {pmavi} tren kaltı yine bekleriz {siyah}  
         oo      _____
        _I__n_n__||_|| ________
      >(_________|_7_|-|______|
       /o ()() ()() o   oo  oo

            """)
        
        
        else:
            print(kahverengi)
            print("""
                __________________   __________________
            .-/|                  \ /                  |\-.
            ||||                   |                   ||||
            ||||  Aradığınız       |       ~~*~~       ||||
            ||||   Soruyu          |                   ||||
            ||||  Bulamadık        |                   ||||
            ||||                   |                   ||||
            ||||                   |     --==*==--     ||||
            ||||                   |                   ||||
            ||||     ~~*~~         |    Belki başka    ||||
            ||||                   |     sayfalarda    ||||
            ||||                   |  Aradğınız cevabı ||||
            ||||                   |     Bulursun      ||||
            ||||__________________ | __________________||||
            ||/===================\|/===================\||
            `--------------------~___~-------------------''      
            """)
            print(sifirla)
    print(sifirla)

basla()
konsol()    
