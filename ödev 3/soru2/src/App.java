import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        

        Scanner scanner = new Scanner(System.in);

        System.out.printf("Bir parola giriniz: ");
        String parola = scanner.nextLine();

        if(parolaKontrol(parola) == true) { //Gelen Değer Truysa
            System.out.println("Parola geçerlidir: " + parola);
        }else{
            System.out.println("Geçersiz Numara");
        }
        
    }

    public static boolean parolaKontrol(String password) 
{
    return password.matches("^(?=(?:\\D*\\d){2})[a-zA-Z0-9]{8,}$"); //eşleşiyorsa true döndüren regex ifadesi
    
    
    // REGEX AÇIKLAMA
    // ^ dizenin başlangıcındaki konumu belirtir
    // \\D*\\d {2} iki ve daha fazla sayı olduğunu hesaplamak için
      //  \D rakam olmuyuyan karakterlerle eşleimesi için
      //  \d bir rakamla eşleşir
    //  [a-zA-Z0-9]  a- z A - Z 1-9 aralığındaki karakterleri kontrol eder
    // {8,} minumum karakter limiti 
}


}