import java.util.Scanner;

public class App {
    
    
    
    
    public static void main(String[] args) throws Exception {
        
        
        Scanner input = new Scanner(System.in); // scanner nesnesi
        long start = System.currentTimeMillis(); //zaman baslangici
        
        int a; //a kenarı
        int b; // b kenarı

        //Değer alma
        while(true){
        System.out.print("A kenarının uzunluğunu giriniz: ");
        a = input.nextInt();
        System.out.print("B kenarının uzunluğunu giriniz: ");
        b = input.nextInt();
        
        if(a == 1 && b == 1){ //diktörgen belitrmeyecek değerler kontrolü
            System.out.println("Kabul edilmeyen değer");
        }else if(a > 0 && b > 0){
            break;
        }else{
            System.out.println("Kabul edilmeyen değer");
        }

    
    
        }
        //fonksiyon çağrıları

        System.out.println("İçi dolu dörgen:"); 
        iciDoluYazdir( a,b);
        System.out.println("İçi boş dörtgen:");
        iciBosYazdir( a, b);
    }

    private static void iciDoluYazdir( int genislik, int yukseklik) throws InterruptedException { 
        for (int i = 1; i <= yukseklik; i++) { // ici dolu icin for döngüsü
            for (int j = 1; j <= genislik; j++) {//yukseklik kadar genislik
                System.out.print("*");
                Thread.sleep(160);
            }
            System.out.println();
        }
    }

    private static void iciBosYazdir(int genislik, int yukseklik) throws InterruptedException {
        for (int j = 1; j <= genislik; j++) { // ici bos icin for döngüsü
            System.out.print("*"); //genislik üstaban
            Thread.sleep(160);
        }
        System.out.println(); 
        for (int i = 1; i <= yukseklik - 2; i++) { //alttaban ve üstaban eksik döngü
            System.out.print("*");  // yanlar döngüsü
            Thread.sleep(160);
            for (int j = 1; j <= genislik - 2; j++) {
                System.out.print(" "); //bosluk dögüsü
                Thread.sleep(160);
            }
            System.out.println("*");
        }
        for (int j = 1; j <= genislik; j++) { //genislik altaban
            System.out.print("*"); 
            Thread.sleep(160);
            
        }
    }
}
