import java.util.Random;

public class App {
    // değişkeler
    static Random rand = new Random(); // random sınıfı
    static int ilkZar;
    static int ikiZar;
    static int toplam;
    static int puan;

    public static void main(String[] args) throws Exception {

        zarAt(); // kontrol durumları oluşturup şartları test ediyorum

        System.out.printf("Oyuncunun attığı zar %d + %d = %d\n", ilkZar, ikiZar, toplam);

        if (toplam == 11 || toplam == 7) { // 7 ve ya 11 ise
            System.out.println("Oyuncu kazandı!");
            System.exit(0);

        } else if (toplam == 2 || toplam == 3 || toplam == 12) { // barbut durumu
            System.out.println("Oyuncu kaybetti! BARBUT");
            System.exit(0);

        } else { // iki durumda değilse puan == toplam
            puan = toplam;
            System.out.printf("Oyuncunun Puanı: %d\n", puan); // ikinci koşul duruumu için
        }

        while (true) { // ilk koşullar sağlanmazsa

            zarAt(); // tekrar zar atıyorum
            System.out.printf("Oyuncunun attığı zar %d + %d = %d\n", ilkZar, ikiZar, toplam);

            if (toplam == 7) {
                System.out.println("Oyuncu kaybetti!");
                break;
            } else if (toplam == puan) {
                System.out.println("Oyuncu kazandı!");
                break;
            }
        }

    }

    public static int zarAt() { // zar atma methodu
        ilkZar = rand.nextInt(6) + 1; // rastgele sayılar
        ikiZar = rand.nextInt(6) + 1;
        toplam = ilkZar + ikiZar; // toplam rastgele sayılara eşit
        
        String zar1 ="+-------+"+
                     "|       |"+
                     "|   o   |"+
                     "|       |"+
                     "+-------+"; 
        
        
        
        System.out.println(zar1);
        
        
        
        
        
        
        
        return toplam; // toplamı return ediyorum
    
    
    
    
    
    
    
    }
}