from renkler import *
import os,time # os ve time kütüphanesini import ettim
def sil(): # bazı yerlerde güzel görünsün diye üsteki yazılan değerleri silmek için modül yazdım
    sistem = os.name #işletim sisteminizi öğrendim

    if os.name == 'nt': #windows için
        sil = os.system('cls') #terminal temizleme komutu
    else: #linux için
        sil = os.system('clear') #terminal temizleme komutu
    sil 
def vur():
    vur = r"""{}

     -   \ O                                       ,  .-.___
    -     /\                                     O/  /xx\XXX\
    -   __/\ `                                   /\  |xx|XXX|
      `     \,()                                ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil)
    vur1 = r"""{}

        -  \O                                      ,  .-.___
    -      /\                                    O/  /xx\XXX\
    -     /\ `                                   /\  |xx|XXX|
        `/   \,()                               ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil)
    vur2 = r"""{}

     -  __ O                                       ,  .-.___
    -     /\                                     O/  /xx\XXX\
    -     /\ `                                   /\  |xx|XXX|
     `   /  \,()                                ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil)    
    vur3 = r"""{}

    -     __ O                                      , .-.___
    -      /\                                    O/  /xx\XXX\
    -      \\ `                                  /\  |xx|XXX|
        -   \\,()                               ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil)  
    vur4 = r"""{}

    -   __ O                                      ,  .-.___
    -     /\                                    O/  /xx\XXX\
    -    / \ `                                  /\  |xx|XXX|
        /   \,  ()                             ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil)  
    vur5 = r"""{}

       __ O                                        ,  .-.___
         /\                                      O/  /xx\XXX\
        / \ `                                    /\  |xx|XXX|
       /   \,       ()                          ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil) 
    vur6 = r"""{}

       __ O                                        ,  .-.___
         /\                                      O/  /xx\XXX\
        / \ `                                    /\  |xx|XXX|
       /   \,            ()                     ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil) 
    vur7 = r"""{}

       __ O                                        ,  .-.___
         /\                                      O/  /xx\XXX\
        / \ `                                    /\  |xx|XXX|
       /   \,                 ()                ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil)     
    vur8 = r"""{}

       __ O                                        ,  .-.___
         /\                                      O/  /xx\XXX\
        / \ `                                    /\  |xx|XXX|
       /   \,                   ()              ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil) 
    vur9 = r"""{}

       __ O                                        ,  .-.___
         /\                                      O/  /xx\XXX\
        / \ `                                    /\  |xx|XXX|
       /   \,                       ()          ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil) 
    vur10 = r"""{}

        __ O                                      ,  .-.___
          /\                                    O/  /xx\XXX\
         / \ `                                  /\  |xx|XXX|
        /   \,                          ()     ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil) 

    vur11 = r"""{}

        __ O                                      ,  .-.___
          /\                                    O/  /xx\XXX\
         / \ `                                  /\  |xx|XXX|
        /   \,                              () ` << |xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil) 
    vur12 = r"""{}

        __ O                                     ,   .-.___
          /\                                   O/   /xx\XXX\
         / \ `                                 /\   |xx|XXX|
        /   \,                                `<< ()|xx|XXX|
    {}^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        """.format(gri,yesil)

    vur13 = r"""
    {}
             ___    ___     ___     ___   __    __
            // \\  // \\   // \\   // \\  ||    ||
           ((___  ((   )) ((   )) ((   )) ||    ||
            \\_||  \\_//   \\_//   \\_//  ||__| ..

                                                                    
    {}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    """.format(kirmizi,yesil)





    #bir bar listesi oluşturp 2 döneride ekledim 
    bar = [ 
            vur,
            vur1,
            vur2,
            vur3,
            vur4,
            vur5,
            vur6,
            vur7,
            vur8,
            vur9,
            vur10,
            vur11,
            vur12,
            vur13,

    ]
    i = 0 # sayaç

    while i<14: # döngü yaptım
        sil()   # yukardakı sil fonkumu çağırdımki önceki print gözükmesin
        print(bar[i % len(bar)], end="\r") #aynı satır başı şeklinde barı printliyorum
        time.sleep(0.7) #sleep fonksiyonu 0.3 delay için
        i += 1  #sayaç    


vur()