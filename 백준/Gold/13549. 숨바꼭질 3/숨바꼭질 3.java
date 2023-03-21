import java.io.*;
import java.util.*;

class llist {
    int node;
    llist left;
    llist right;

    public void set(int node) {
        this.node = node;
    }
}

class que {
    int leng = 0;
    llist start;
    llist end;

    public int getLeng() {
        return leng;
    }

    public void append(int node) {
        if (leng == 0) {
            llist now = new llist();
            now.set(node);
            start = now;
            end = now;
        } else {
            llist now = new llist();
            now.set(node);
            now.left = end;
            end.right = now;
            end = now;
        }
        leng++;
    }
    public void appendleft(int node) {
        if (leng == 0) {
            llist now = new llist();
            now.set(node);
            start = now;
            end = now;
        } else {
            llist now = new llist();
            now.set(node);
            now.right = start;
            start.left = now;
            start = now;
        }
        leng++;
    }
    public int pop() {
        int result = -1;

        if (leng == 0) return result;
        result = end.node;
        end = end.left;
        leng--;
        return result;
    }
    public int popleft() {
        int result = -1;

        if (leng == 0) return result;

        result = start.node;
        start = start.right;
        leng--;
        return result;
    }
}
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());;
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken()), now;
        if(start==end) System.out.println(0);
        else {
            int[] dp = new int[100001];
            Arrays.fill(dp,-1);


            que Q = new que();
            Q.append(start);
            dp[start] = 0;

            while (Q.getLeng() > 0) {
                now = Q.popleft();
                if (0 <= now * 2 && now * 2 <= 100000 && dp[now * 2] == -1) {
                    dp[now * 2] = dp[now];
                    Q.appendleft(now * 2);
                }
                if (0 <= now + 1 && now + 1 <= 100000 && dp[now + 1] == -1) {
                    dp[now + 1] = dp[now] + 1;
                    Q.append(now + 1);
                }
                if (0 <= now - 1 && now - 1 <= 100000 && dp[now - 1] == -1) {
                    dp[now - 1] = dp[now] + 1;
                    Q.append(now - 1);
                }
                if (dp[end] != -1){
                    System.out.println(dp[end]);
                    break;
                }
            }
        }
    }
}