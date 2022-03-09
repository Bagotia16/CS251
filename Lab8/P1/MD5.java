import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import javax.management.RuntimeErrorException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5 {
    // return MD5 value
    public static String getMD5(String input) throws NoSuchAlgorithmException {
        try{
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes());
            BigInteger no = new BigInteger(1, messageDigest);
            String hashtext = no.toString(16);

            while(hashtext.length() < 32){
                hashtext = "0"+hashtext;
            }
            return hashtext;
        }
        catch(Error e) {
            throw new RuntimeErrorException(e);
        }
    }

    //compare original and given MD5 value
    public static boolean check(String line) throws NoSuchAlgorithmException {
        String[] value = line.split("-");
        String s = "";
        //to handel more than 1 -
        for(int i=0; i<value.length-1; i++){
            if(i==0)
                s += value[i];
            else
                s += ("-"+value[i]);
        }
        String hashValue = getMD5(s.replaceAll("\\s", ""));
        String hashtext = value[value.length -1].replaceAll("\\s", "");

        if(hashtext.equals(hashValue))
            return true;
        else
            return false;
    }

    //readfile and output the result
    public static void main(String[] argv) throws NoSuchAlgorithmException {
        try{
            File file  = new File("MD5sums");
            Scanner file_read = new Scanner(file);
            while(file_read.hasNextLine()){
                String data = file_read.nextLine();
                if(check(data))
                    System.err.println("verified");
                else
                    System.err.println("not verified");

            }
            file_read.close();
        }
        catch(FileNotFoundException e){
            System.out.println("Cannot read the file!");
            e.printStackTrace();
        }
    }
}
