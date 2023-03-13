import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedWriter bw2 = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Stack<Integer> stk = new Stack<>();
        Stack<Integer> stk_idx = new Stack<>();

        int[] arr = new int[1000000];
        int num;
        for (int i = 0; i < N; i++){
            num = Integer.parseInt(st.nextToken());
            while (!stk.empty() && stk.peek() < num){
                stk.pop();
                arr[stk_idx.pop()] = num;
            }
            stk.push(num);
            stk_idx.push(i);
        }
        while(!stk.empty()){
            stk.pop();
            arr[stk_idx.pop()] = -1;
        }
        for (int i = 0; i < N; i++) {
            bw.write(arr[i] + " ");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}