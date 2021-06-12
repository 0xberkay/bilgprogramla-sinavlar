import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        
        
        //ARAÇ Örneklendirmlerimi oluşturuyorum
        
        Otomobil starfighter = new Otomobil("111111", "Darth Vader", "28/05/5902", "12:24", 12, 1);
        Otomobil tantive = new Otomobil("111112", "Luke Skywalker", "28/05/5902", "13:25", 15, 1);

        Minibus millennium = new Minibus("111113", "Han Solo", "28/05/5902", "13:26", 13, 2);
        Minibus starDestroyer = new Minibus("111114", "Leia Organa", "28/05/5902", "13:28", 12, 2);

        Otobus hammerHead = new Otobus("111115", "Obi-Wan Kenobi", "28/05/5902", "13:24", 21, 3);
        Otobus jumpSpeeder = new Otobus("111116", "R2-D2", "16/03/5902", "17:12", 24, 3);
        

        Otomobil speeder = new Otomobil("Rey Skywalker", "28/05/5902", "23:12", 3,true);
        Otomobil razorCrest = new Otomobil("Grogu", "28/05/5902", "11:12", 1,true);




        Gise gise = new Gise();

        

        //Gise Hesaplama fonksiyonuma örneklendirmeleri veriyorum

        gise.giseHesapla(starfighter);
        gise.giseHesapla(tantive);
        gise.giseHesapla(millennium);
        gise.giseHesapla(starDestroyer);
        gise.giseHesapla(hammerHead);
        gise.giseHesapla(jumpSpeeder);
        
        
        gise.giseHesapla(speeder);
        gise.giseHesapla(razorCrest);
       
        
        gise.getYonetim().detayRapor(); //Detaylı rapor
        gise.getYonetim().rapor(); //Normal Rapor

        

    }

}
////////////////////////////////////////
///////// A ŞIKKI //////////////////////
///////////////////////////////////////
class OgsArac {
    //Modeller
    private String ogsNumara;
    private String isimSoyisim;
    private String tarih;
    private String saat;
    private int bakiye;
    private int sinifi;
    private boolean rebelAlliance;
    
    //Normal Constrocat

    public OgsArac(String ogsNumara, String isimSoyisim, String tarih, String saat, int bakiye, int sinifi) {
        this.ogsNumara = ogsNumara;
        this.isimSoyisim = isimSoyisim;
        this.tarih = tarih;
        this.saat = saat;
        this.bakiye = bakiye;
        this.sinifi = sinifi;
    }
    //Kaçak Constrocat
    public OgsArac(String isimSoyisim, String tarih, String saat, int sinifi, boolean rebelAlliance) {
        this.isimSoyisim = isimSoyisim;
        this.tarih = tarih;
        this.saat = saat;
        this.sinifi = sinifi;
        this.rebelAlliance = rebelAlliance;
    }

    //Setter Getter ve  Checkerlar
    public boolean isRebelAlliance() {
        return this.rebelAlliance;
    }

    public boolean getRebelAlliance() {
        return this.rebelAlliance;
    }

    public void setRebelAlliance(boolean rebelAlliance) {
        this.rebelAlliance = rebelAlliance;
    }

    public String getOgsNumara() {
        return this.ogsNumara;
    }

    public void setOgsNumara(String ogsNumara) {
        this.ogsNumara = ogsNumara;
    }

    public String getIsimSoyisim() {
        return this.isimSoyisim;
    }

    public void setIsimSoyisim(String isimSoyisim) {
        this.isimSoyisim = isimSoyisim;
    }

    public String getTarih() {
        return this.tarih;
    }

    public void setTarih(String tarih) {
        this.tarih = tarih;
    }

    public String getSaat() {
        return this.saat;
    }

    public void setSaat(String saat) {
        this.saat = saat;
    }

    public int getBakiye() {
        return this.bakiye;
    }

    public void setBakiye(int bakiye) {
        this.bakiye = bakiye;
    }

    public int getSinifi() {
        return this.sinifi;
    }

    public void setSinifi(int sinifi) {
        this.sinifi = sinifi;
    }

}

class Otomobil extends OgsArac { //Kalıtımla ogs arac Sınıfını alıypruö 

    public Otomobil(String isimSoyisim, String tarih, String saat, int sinifi, boolean rebelAlliance) {
        super(isimSoyisim, tarih, saat, sinifi, rebelAlliance);
        
    }

    public Otomobil(String ogsNumara, String isimSoyisim, String tarih, String saat, int bakiye, int sinifi) {
        super(ogsNumara, isimSoyisim, tarih, saat, bakiye, sinifi);

    }

}

class Minibus extends OgsArac { //Kalıtımla ogs arac Sınıfını alıypruö 


    public Minibus(String isimSoyisim, String tarih, String saat, int sinifi, boolean rebelAlliance) {
        super(isimSoyisim, tarih, saat, sinifi, rebelAlliance);
        
    }

    public Minibus(String ogsNumara, String isimSoyisim, String tarih, String saat, int bakiye, int sinifi) {
        super(ogsNumara, isimSoyisim, tarih, saat, bakiye, sinifi);

    }

}

class Otobus extends OgsArac { //Kalıtımla ogs arac Sınıfını alıypruö 


    public Otobus(String isimSoyisim, String tarih, String saat, int sinifi, boolean rebelAlliance) {
        super(isimSoyisim, tarih, saat, sinifi, rebelAlliance);
        
    }

    public Otobus(String ogsNumara, String isimSoyisim, String tarih, String saat, int bakiye, int sinifi) {
        super(ogsNumara, isimSoyisim, tarih, saat, bakiye, sinifi);

    }}

////////////////////////////////////////
///////// b ŞIKKI //////////////////////
///////////////////////////////////////
class Gise { //Gise Sınıfı

    Yonetim yonetim = new Yonetim();


    public Yonetim getYonetim() { //Örneklendirme getteri
        return this.yonetim;
    }    
    
    public void giseHesapla(OgsArac gelenArac) { //Gise hesaplama methodu

        
                //Sinifa Gçre bakiye azaltma ve kazanç ekleme
                if (gelenArac.getSinifi() == 1) {

                    int yeniBakiye = gelenArac.getBakiye() - 1;
                    gelenArac.setBakiye(yeniBakiye);
        
                    int yeniKazanc = yonetim.getKazanc() + 1;
                    yonetim.setKazanc(yeniKazanc);
        
                } else if (gelenArac.getSinifi() == 2) {
                    
        
                    int yeniBakiye = gelenArac.getBakiye() - 2;
                    gelenArac.setBakiye(yeniBakiye);
        
                    int yeniKazanc = yonetim.getKazanc() + 2;
                    yonetim.setKazanc(yeniKazanc);
        
                } else if (gelenArac.getSinifi() == 3) {
                    
        
                    int yeniBakiye = gelenArac.getBakiye() - 3;
                    gelenArac.setBakiye(yeniBakiye);
        
                    int yeniKazanc = yonetim.getKazanc() + 3;
                    yonetim.setKazanc(yeniKazanc);
        
                } else {
                    System.out.println("Tanımlanamıyan cisim");
                }



////////////////////////////////////////
///////// d ŞIKKI //////////////////////
///////////////////////////////////////
        if(gelenArac.isRebelAlliance() == true){ //Eğer asiyse
            System.out.println("Gemiye asiler binmek istiyor !!! Kırmızı alarm");
            int yeniKazanc = yonetim.getKazanc() - gelenArac.getSinifi();
            
            
            //Liste Ekleme

            yonetim.setKazanc(yeniKazanc);
            yonetim.setKacakAraclar(gelenArac.getIsimSoyisim());

            yonetim.setKacakAraclarDetay(gelenArac.getIsimSoyisim());
            yonetim.setKacakAraclarDetay(gelenArac.getSaat());
            yonetim.setKacakAraclarDetay(gelenArac.getTarih());
            yonetim.setKacakAraclarDetay(Integer.toString(gelenArac.getSinifi()));



        }
        
        if(gelenArac.getOgsNumara() != null){ // Eğer ogs numarası varsa
            yonetim.setAraclar((gelenArac.getOgsNumara()));

            yonetim.setAraclarDetay(gelenArac.getOgsNumara());
            yonetim.setAraclarDetay(gelenArac.getIsimSoyisim());
            yonetim.setAraclarDetay(gelenArac.getTarih());
            yonetim.setAraclarDetay(gelenArac.getSaat());
            yonetim.setAraclarDetay(Integer.toString(gelenArac.getBakiye()));
            
            yonetim.setAraclarDetay(Integer.toString(gelenArac.getSinifi()));



        }
        


    }
}
////////////////////////////////////////
///////// c ŞIKKI  ////////////////////
///////////////////////////////////////
class Yonetim {
    private int kazanc;
    private String busun;

    //Rapor listeleri



    ArrayList<String> araclar = new ArrayList<String>();
    ArrayList<String> araclarDetay = new ArrayList<String>();

    ArrayList<String> kacakAraclar = new ArrayList<String>();
    ArrayList<String> kacakAraclarDetay = new ArrayList<String>();

    
    //Sinif belirleme Fonksiyonları

    public void senNesin(String nesin){
        if (nesin.equals("1")){
            senBusun("otomobil");
        }else if(nesin.equals("2")){
            senBusun("minibüs");
        }else if(nesin.equals("3")){
            senBusun("otobüs");
        }
    }
    public void senBusun(String busun) {
        this.busun = busun;
    }
    public String getSenBusun() {
        return this.busun;
    }
    
    //Liste Setter Getterları

    public ArrayList<String> getAraclarDetay() {
        return this.araclarDetay;
    }
    public void setAraclarDetay(String araclarDetay) {

    this.araclarDetay.add(araclarDetay);
}

    public ArrayList<String> getKacakAraclarDetay() {
        return this.kacakAraclarDetay;
    }

    public void setKacakAraclarDetay(String kacakAraclarDetay) {
        this.kacakAraclarDetay.add(kacakAraclarDetay);
    }


    public ArrayList<String> getKacakAraclar() {
        return this.kacakAraclar;
    }

    public void setKacakAraclar(String kacakAraclar) {
        this.kacakAraclar.add(kacakAraclar);
    }


    public int getKazanc() {
        return this.kazanc;
    }

    public void setKazanc(int kazanc) {
        this.kazanc = kazanc;
    }

    public ArrayList<String> getAraclar() {
        return this.araclar;
    }

    public void setAraclar(String araclar) {
        this.araclar.add(araclar);
    }
    //Küçük rapor

    public void rapor() {
        int listeBoyutu = araclar.size();
        int kacakSayisi = kacakAraclar.size();
        System.out.println("===========================");
        System.out.printf("Droid RAPORU : \n");
        System.out.println("===========================");
        System.out.println("Toplam Galaktik kredi kazancı : " + getKazanc());
        for (int i = 0; i < listeBoyutu;i++){
            System.out.println("Gelen araç no : " +araclar.get(i));
            
        }
        System.out.printf("Toplam Gelen Cumhuriyet Araçı : %d | Toplam gelen Kaçak Asi Sayısı : %d\n",listeBoyutu,kacakSayisi);
        System.out.println("===========================");
        
        for (int j = 0; j < kacakSayisi;j++){
            System.out.println("Kaçak Yolcunun Adı :" +kacakAraclar.get(j));
            
        }
        
    }

    //Detay Rapor
    public void detayRapor(){
        int detayListeBoyutu = araclarDetay.size();
        int detayKacakSayisi = kacakAraclarDetay.size();
        
            System.out.println("===========================");
            System.out.printf("Detaylı Droid RAPORU : \n");
            System.out.println("===========================");
        
        for (int i = 0; i < detayListeBoyutu;i+=6){
            

            senNesin(araclarDetay.get(i + 5));
            System.out.println("Gelen araç no : " +araclarDetay.get(i) +
            " Gelen Araç Sürücü Adı :  "  + araclarDetay.get(i + 1) + 
            " Tarih : " + araclarDetay.get(i + 2) + 
            " Saat : " + araclarDetay.get(i + 3) +
            " Bakiye : " + araclarDetay.get(i + 4) +
            " Sınıfı : " + getSenBusun()
            
            );
        
            

        }
        System.out.println("===========================");
        for (int j = 0; j < detayKacakSayisi;j+=4){
            
            senNesin(kacakAraclarDetay.get(j + 3));
            
            System.out.println(
            "Gelen Kaçak Araç Sürücü Adı :  "  + kacakAraclarDetay.get(j) + 
            " Tarih : " + kacakAraclarDetay.get(j + 1) + 
            " Saat : " + kacakAraclarDetay.get(j + 2) +
            " Sınıfı : " + getSenBusun()
            
            
            );
            
        }
        int kacakSayisi = kacakAraclar.size();
        int listeBoyutu = araclar.size();
        System.out.println("===========================");
        System.out.println("Toplam kaçak sayısı : "+kacakSayisi);
        System.out.println("Toplam gelen araç : "+listeBoyutu);
        System.out.println("===========================");
        System.out.println("Toplam Galaktik kredi kazancı : " + getKazanc());
   
   
   
    }



}