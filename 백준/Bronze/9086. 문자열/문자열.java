import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String st;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i<N; i++){
            st = br.readLine();
            bw.write(st.charAt(0));
            bw.write(st.charAt(st.length()-1));
            bw.newLine();
        }
        bw.flush();
    }
}