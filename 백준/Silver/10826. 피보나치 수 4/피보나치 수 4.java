import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static HashMap<Long, BigInteger> d = new HashMap<>();

    public static BigInteger fibo(long n) {
        if (n <= 0) {
            return BigInteger.valueOf(0);
        } else if (n == 1) {
            return BigInteger.valueOf(1);
        } else if (n == 2) {
            return BigInteger.valueOf(1);
        } else if (d.get(n) != null) {
            return d.get(n);
        } else {
            if (n % 2 == 1) {
                long m = (n + 1) / 2;
                BigInteger t1 = fibo(m);
                BigInteger t2 = fibo(m - 1);
                t1 = t1.multiply(t1);
                t2 = t2.multiply(t2);
                d.put(n, t1.add(t2));
                return d.get(n);
            } else {
                long m = n / 2;
                BigInteger t1 = fibo(m - 1);
                BigInteger t2 = fibo(m);
                t1 = t1.multiply(BigInteger.valueOf(2));
                t1 = t1.add(t2);
                d.put(n, t1.multiply(t2));
                return d.get(n);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        long num = Long.parseLong(br.readLine());

        bw.write(fibo(num) + "");
        bw.flush();
        br.close();
        bw.close();
    }
}