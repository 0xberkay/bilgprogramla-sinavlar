import java.util.regex.Pattern; // regex kütüphanesi

public class App {
    public static void main(String[] args) {

        Insan insan1 = new Insan("ali", "11111111111"); // insan örneklendirmesi

        insan1.kendiniTanit(); // kendiniTanit fonksiyonu çağrılıyor

    }


    private static Pattern pattern = Pattern.compile("-?\\d+(\\.\\d+)?"); //sayimi olduğunun regexi

    public static boolean buSayimi(String strSayi) {
        if (strSayi == null) { //eğer boşsa
            return false;
        }
        return pattern.matcher(strSayi).matches(); // alinan değerle regex karşılaştırması
    }


    /**
     * Insan
     */
    public static class Insan {

        // Değişkenler ve örneklendirmeler

        private String isim;
        private String tcno;

        Akvaryum akt = new Akvaryum(5);

        Kedi kedi = new Kedi("Şakir");

        // Consuracter


        public Insan(String isim, String tcno) {
            this.isim = isim;
            this.tcno = tcno;

            //tcno kontrol
            if (this.tcno.length() == 11 && buSayimi(this.tcno) == true) {
                this.tcno = tcno;
            } else {
                String hata = "Hatalı tc girdiniz";
                this.tcno = hata;
            }

        }

        // getter methodu

        public String getIsim() {
            return this.isim;
        }

        // setter methodu

        public void setIsim(String isim) {
            this.isim = isim;
        }

        // getter methodu

        public String getTcno() {
            return this.tcno;
        }

        // setter methodu

        public void setTcno(String tcno) {
            //tcno kontrol
            if (this.tcno.length() == 11 && buSayimi(this.tcno) == true) {
                this.tcno = tcno;
            } else {
                String hata = "Hatalı tc girdiniz";
                this.tcno = hata;
            }
        }

        public void kendiniTanit() { // kendiniTanit methodu
            akt.balikEkle(3);
            akt.balikSil(3);
            System.out.printf("Merhaba , Benim adım : %s , TC no'um : %s , Balık sayım : %d , Kedimin ismi : %s", isim,
                    tcno, akt.getBalikSayisi(), kedi.getIsim());

        }
    }

    /**
     * Akvaryum
     */
    static class Akvaryum {
        private int balikSayisi;

        // Consuracter

        public Akvaryum(int balikSayisi) {
            this.balikSayisi = balikSayisi;
        }

        // getter methodu

        public int getBalikSayisi() {
            return this.balikSayisi;
        }

        public void balikEkle(int adet) {
            this.balikSayisi = this.balikSayisi + adet;
        }

        public void balikSil(int adet) {
            this.balikSayisi = this.balikSayisi - adet;
        }
    }

    /**
     * Kedi
     */
    static class Kedi {

        private String isim;

        // getter methodu

        public String getIsim() {
            return this.isim;
        }

        // setter methodu

        public void setIsim(String isim) {
            this.isim = isim;
        }

        // Consuracter

        public Kedi(String isim) {
            this.isim = isim;
        }

    }
}