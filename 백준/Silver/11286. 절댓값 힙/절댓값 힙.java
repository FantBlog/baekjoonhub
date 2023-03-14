import java.io.*;
import java.util.*;

class Heap {
    int[] min_tree = new int[100002];
    int[] max_tree = new int[100002];
    int idx_min = 1;
    int idx_max = 1;

    public void push(int num) {
        if (num > 0) {
            min_push(num);
        } else {
            max_push(num);
        }
    }

    public int pop() {
        int result;
        int a = max_peek();
        int b = min_peek();
        if ( a > b ) {
            result = min_pop();
        } else {
            result = max_pop();
        }
        return result;
    }
    public void min_push(int num) {
        min_tree[idx_min] = num;
        int k = idx_min;
        idx_min++;
        while (k > 1) {
            if (min_tree[k / 2] > min_tree[k]) {
                int temp = min_tree[k];
                min_tree[k] = min_tree[k / 2];
                min_tree[k / 2] = temp;
                k = k / 2;
            }
            else break;
        }
    }

    public void max_push(int num) {
        max_tree[idx_max] = num;
        int k = idx_max;
        idx_max++;
        while (k > 1) {
            if (max_tree[k / 2] < max_tree[k]) {
                int temp = max_tree[k];
                max_tree[k] = max_tree[k / 2];
                max_tree[k / 2] = temp;
                k = k / 2;
            }
            else break;
        }
    }

    public int min_pop() {
        if (idx_min == 1){
            return 0;
        }
        int result = min_tree[1];
        min_tree[1] = min_tree[idx_min - 1];
        min_tree[idx_min - 1] = 0;
        idx_min--;

        int k = 1;
        while (k * 2 < idx_min) {
            if (min_tree[k * 2] < min_tree[k * 2 + 1] && min_tree[k * 2] < min_tree[k]) {
                int temp = min_tree[k];
                min_tree[k] = min_tree[k * 2];
                min_tree[k * 2] = temp;
                k = k * 2;
                continue;
            }
            if (min_tree[k * 2 + 1] < min_tree[k] && k * 2 + 1 < idx_min) {
                int temp = min_tree[k];
                min_tree[k] = min_tree[k * 2 + 1];
                min_tree[k * 2 + 1] = temp;
                k = k * 2 + 1;
                continue;
            }
            if (min_tree[k * 2] < min_tree[k]) {
                int temp = min_tree[k];
                min_tree[k] = min_tree[k * 2];
                min_tree[k * 2] = temp;
                k = k * 2;
                continue;
            }
            break;
        }
        return result;
    }
    public int max_pop() {
        if (idx_max == 1){
            return 0;
        }
        int result = max_tree[1];
        max_tree[1] = max_tree[idx_max - 1];
        max_tree[idx_max - 1] = 0;
        idx_max--;

        int k = 1;
        while (k * 2 < idx_max) {
            if (max_tree[k * 2] > max_tree[k * 2 + 1] && max_tree[k * 2] > max_tree[k]) {
                int temp = max_tree[k];
                max_tree[k] = max_tree[k * 2];
                max_tree[k * 2] = temp;
                k = k * 2;
                continue;
            }
            if (max_tree[k * 2 + 1] > max_tree[k] && k * 2 + 1 < idx_max) {
                int temp = max_tree[k];
                max_tree[k] = max_tree[k * 2 + 1];
                max_tree[k * 2 + 1] = temp;
                k = k * 2 + 1;
                continue;
            }
            if (max_tree[k * 2] > max_tree[k]){
                int temp = max_tree[k];
                max_tree[k] = max_tree[k * 2];
                max_tree[k * 2] = temp;
                k = k * 2;
                continue;
            }
            break;
        }
        return result;
    }

    public int max_peek(){
        if (idx_max != 1)
            return Math.abs(max_tree[1]);
        else
            return 2147483647;
    }
    public int min_peek(){
        if (idx_min != 1)
            return Math.abs(min_tree[1]);
        else
            return 2147483647;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int order;
        Heap hp = new Heap();

        for (int i = 0; i < N; i++) {
            order = Integer.parseInt(br.readLine());
            if (order == 0) {
                bw.write(hp.pop() + "");
                bw.newLine();
            } else {
                hp.push(order);
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}