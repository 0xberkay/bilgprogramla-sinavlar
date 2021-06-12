
import java.util.regex.Matcher; // regex eşleşme apisi
import java.util.regex.Pattern; // regez düzen apisi

public class App {
    public static void main(String[] args) throws Exception {
        
        //degerler
        String email1 = "iletisim@berkaykucuk.com.tr";
        String email2 = "berkay@0xb3rk0y.cf";
        String email3 = "admin@dadas.team";
        String email4 = "/a%+@@gmail.com";


        String ip1 = "127.0.0.1"; 
        String ip2 = "ad.12.as.32"; 
        
        System.out.println(ipDogruMu(ip2));
        System.out.println(ipDogruMu(ip1));
        System.out.println(mailDogruMu(email1));
        System.out.println(mailDogruMu(email2));
        System.out.println(mailDogruMu(email3));
        System.out.println(mailDogruMu(email4));
    }

    public static boolean mailDogruMu(String email) //mail kontrol
    {
        String mailKontrol = 
        "^(?=.{1,64}@)[A-Za-z0-9_-]+(\\.[A-Za-z0-9_-]+)*@"
        + "[^-][A-Za-z0-9-]+(\\.[A-Za-z0-9-]+)*(\\.[A-Za-z]{2,})$";
         
        // açılım regex
        // ^ satır başlangıcı                                
        // en az 1 max 64 karakter
        // ingilizce a - z büyük küçük karakterler ve sayılar
        // bir veya fazla nokta için isteğe bağlı koşul
        // @ mutlaka olmalı
        // domain - işareti ile başlıyamaz
        // ingilizce a - z büyük küçük karakterler ve sayılar
        // bir veya fazla nokta için isteğe bağlı koşul
        // uzantı karakteri en az 2 karakter sadece inglizce harfler


        Pattern duzen = Pattern.compile(mailKontrol); // patter örneklendirmesi

        if (email == null) // eğer email boşsa yanlıştır
            return false;
        return duzen.matcher(email).matches(); //regexe göre eşleştirme
    }

    public static boolean ipDogruMu(String ip){ //ip kontrol
        String ipKontrol =
        "^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\." +
        "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\." +
        "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\." +
        "([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$";
        
        // açılım regex
        // ^ satır başlangıcı
        // parantez işareti
        // 0 veya 9
        //10 veya 99
        //100 veya 199
        //200 veya 249
        // 250 veya 255
        // parantez işareti
        // her satır için nokta
        // son satırda nokta yok


        Pattern duzen = Pattern.compile(ipKontrol);// patter örneklendirmesi
        
        if (ip == null) // eğer ip boşsa yanlıştır
            return false;
        return duzen.matcher(ip).matches(); //regexe göre eşleştirme
    
    }
}

    


