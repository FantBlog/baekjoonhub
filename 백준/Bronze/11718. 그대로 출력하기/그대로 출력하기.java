import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st;
        while(true){
            st = br.readLine();
            if(st == null) break;
            System.out.println(st);
        }
    }
}