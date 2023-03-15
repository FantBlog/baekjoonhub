import java.io.*;
import java.util.*;

public class Main {
    static long x = 1000000007L;
    static HashMap<Long, Long> d = new HashMap<>();

    public static long fibo(long n) {
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 1;
        } else if (d.get(n) != null) {
            return d.get(n);
        } else {
            if (n % 2 == 1) {
                long m = (n + 1) / 2;
                long t1 = fibo(m);
                long t2 = fibo(m - 1);
                d.put(n, (t1 * t1 + t2 * t2) % x);
                return d.get(n);
            } else {
                long m = n / 2;
                long t1 = fibo(m - 1);
                long t2 = fibo(m);
                d.put(n, (2L * t1 + t2) * t2 % x);
                return d.get(n);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        long N = Long.parseLong(br.readLine());
        bw.write(fibo(N)*fibo(N+1)%x+"");

        bw.flush();
        br.close();
        bw.close();
    }
}