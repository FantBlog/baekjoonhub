import java.io.*;
import java.util.*;

public class Main {
    static long[] sumtree;
    static int[] nums, mintree;
    static long result;
    static int N;

    public static long sumseg(int idx, int start, int end) {
        if (start == end) {
            return sumtree[idx] = nums[start];
        }
        return sumtree[idx] = sumseg(idx * 2, start, (start + end) / 2) + sumseg(idx * 2 + 1, (start + end) / 2 + 1, end);
    }

    public static int minseg(int idx, int start, int end) {
        if (start == end) {
            return mintree[idx] = start;
        }
        int left = minseg(idx * 2, start, (start + end) / 2);
        int right = minseg(idx * 2 + 1, (start + end) / 2 + 1, end);
        if (nums[left] < nums[right])
            return mintree[idx] = left;
        else return mintree[idx] = right;
    }

    public static long checksum(int left, int right, int idx, int start, int end) {
        if (left > end || start > right) return 0;

        if (start >= left && right >= end) return sumtree[idx];

        long A = checksum(left, right, idx * 2, start, (start + end) / 2);
        long B = checksum(left, right, idx * 2 + 1, (start + end) / 2 + 1, end);
        return A + B;
    }

    public static int checkmin(int left, int right, int idx, int start, int end) {
        if (left > end || start > right) return 0;

        if (start >= left && right >= end) return mintree[idx];

        int A = checkmin(left, right, idx * 2, start, (start + end) / 2);
        int B = checkmin(left, right, idx * 2 + 1, (start + end) / 2 + 1, end);
        if (nums[A] < nums[B]) return A;
        else return B;
    }


    public static void solution(int idx, int start, int end) {
        if (start == end) {
            if ((long) nums[start] * nums[start] > result)
                result = (long) nums[start] * nums[start];
            return;
        }

        int minidx = checkmin(start, end, idx, 1, N);
        long sum = checksum(start, end, idx, 1, N);
        long temp = nums[minidx] * sum;
        if (result < temp) result = temp;

        if (minidx != end)
            solution(idx, minidx + 1, end);
        if (minidx != start)
            solution(idx, start, minidx - 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        int P = 0;
        nums = new int[N + 1];
        nums[0] = 2147483647;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) nums[i] = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            if (Math.pow(2, i) >= N) {
                P = i;
                break;
            }
        }
        sumtree = new long[(int) Math.pow(2, P + 1)];
        mintree = new int[(int) Math.pow(2, P + 1)];

        sumseg(1, 1, N);
        minseg(1, 1, N);
        solution(1, 1, N);
        bw.write(result + "");
        bw.flush();

    }
}