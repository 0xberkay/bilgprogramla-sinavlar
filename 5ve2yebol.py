#5 ve 2 ye bolenbilen sayılar
import random
renkler = ['\033[95m','\033[94m','\033[92m','\033[93m','\033[91m','\033[1m']
#usteki renk kodu altdaki printle rastgele renk olusturuyor
i = 1
while i <=100:
    
    if i % 2== 0 and i%5==0:
        print(random.choice(renkler)+"5 ve 2 ile bölünebilen sayı: {}".format(i)+'\033[0m')

    i += 1