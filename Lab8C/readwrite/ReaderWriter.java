package readwrite;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class ReaderWriter implements Runnable {
    String FILENAME;
    ProtectedTree ptree;
    boolean iswriter;

    public ReaderWriter(String FILENAME, ProtectedTree ptree, boolean iswriter) {
        this.FILENAME = FILENAME;
        this.ptree = ptree;
        this.iswriter = iswriter;
    }

    @Override
    public void run() {
        if(iswriter == true){
            File f = new File(FILENAME);
            Scanner f_read = null;
            try {
                f_read = new Scanner(f);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            while(f_read.hasNextLine()) {
                int data = Integer.parseInt(f_read.nextLine());
                ptree.write(data);
            }
            f_read.close();
        }
        else{
            File f = new File(FILENAME);
            Scanner f_read = null;
            try {
                f_read = new Scanner(f);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            while (f_read.hasNextLine()) {
                int data = Integer.parseInt(f_read.nextLine());
                try {
                    ptree.read(data);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            f_read.close();
        }

    }

}
