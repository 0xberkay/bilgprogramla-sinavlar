import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.printf("Bir string giriniz: ");
        String string = scanner.nextLine(); //String Değeri alma
        string = string.toLowerCase(); // Eğer büyük harf varsa
        scanner.close();

        List<Character> sesliler = new ArrayList<Character>();
        sesliler.addAll(Arrays.asList(new Character[]{'a', 'e', 'i', 'o', 'u'})); // Sesli harfler
        List<Character> sessizler = new ArrayList<Character>();
        sessizler.addAll(Arrays.asList(new Character[]{'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'})); //Sessiz harfler
        int sesliSayac = 0;
        int sessizSayac = 0;
        for (int i = 0; i < string.length(); i++){ //Stringin uzunluğunca i ye bir ekle
            // karakterleri tek tek harfe atayıp ses türüne göre sayaca ekliyoruz
            Character harf = string.charAt(i); 
            if (sesliler.contains(harf)){
                sesliSayac ++;
            } else if (sessizler.contains(harf)){
                sessizSayac++;
            }
        }

        System.out.println("\nSesli harf sayısı:"+sesliSayac);
        System.out.println("Sessiz harf sayısı:"+sessizSayac);
    }

    
}
