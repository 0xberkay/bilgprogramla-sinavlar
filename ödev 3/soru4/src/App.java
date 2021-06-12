import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //Scanner örneklendirmeleri
        Scanner scanner3 = new Scanner(System.in);
        Scanner scanner = new Scanner(System.in);
        Scanner scanner2 = new Scanner(System.in);
        Bilgiler bilgiler = new Bilgiler();
        System.out.println("==============================");
        System.out.println("MERHABA Bal Coine hoş geldiniz");
        System.out.println("==============================");
        System.out.printf("Lütfen Şifrenizi giriniz : ");
        String alinanSifre = scanner3.nextLine();

        if(alinanSifre.equals(bilgiler.getSifre())){ //Eğer alımam şifre doğruysa
            //Ekranı silme
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("Şifreniz Doğru. Yönlendiriliyorsunuz ...");
            Thread.sleep(1000); //Zaman Aşımı
 
            bilgiler.mesaj(); //Mesaj
            while(true){

                System.out.println("Seçeneğinizi Giriniz : ");
                String secenek = scanner.nextLine();
                
                
                if(secenek.equals("1")){ //Bakiye Sorgu
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Bakiyeniz: "+bilgiler.getCoin());
                    
                    Thread.sleep(1000);
                }else if(secenek.equals("2")){ //Bakiye Ekle
                    System.out.printf("Yatırmak istediğiniz tutar: ");
                    int tutar =  scanner2.nextInt();
                    
                    bilgiler.setCoin(bilgiler.getCoin() + tutar);
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Coinler başarıyla yüklendi. Yeni Bakiyeniz : "+bilgiler.getCoin());
                    Thread.sleep(1000);
                }else if(secenek.equals("3")){ //Bakiye çek
                    System.out.printf("Çekmek istediğiniz tutar: ");
                    int tutar =  scanner2.nextInt();
                    int yeniTutar = bilgiler.getCoin() - tutar;
                    if(yeniTutar >= 0){ //Eğer eki değilse
                        bilgiler.setCoin(yeniTutar);
                        System.out.print("\033[H\033[2J");
                        System.out.flush();
                        System.out.println("Tutarınız başarıyla çekildi . Yeni Bakiyeniz : "+bilgiler.getCoin());
                        Thread.sleep(1000);
                        
                    }else{
                        System.out.print("\033[H\033[2J");
                        System.out.flush();
                        System.out.println("HATA ! Eksik bakiye");
                        Thread.sleep(1000);
                    }
                    
                     
                }else if(secenek.equals("4")){ //Çıkma seçeneği
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    System.out.println("Çıkış yapıyorsunuz...");
                    Thread.sleep(500);
                    break;
                }


            }


        }else{
            System.out.println("Şifreniz Hatalı");
        }





    }
}


class Bilgiler {
    int coin = 100;
    String sifre = "123";   

    //Setter getter  ve mesaj Fonksiyonu
    public int getCoin() {
        return this.coin;
    }

    public void setCoin(int coin) {
        this.coin = coin;
    }

    public String getSifre() {
        return this.sifre;
    }

    public void mesaj(){
        System.out.println("===========================\n"+
                
        "Lütfen Bir İşlem Numarası Seçiniz\n"+

        "1. Bakiye Sorgu\n"+
        "2. Coin Yatır\n"+
        "3. Coin Çek\n" +
        "4. Çıkış\n"
         

        );
    }
}    
    