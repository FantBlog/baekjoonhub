import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
        int N = Integer.parseInt(br.readLine()), temp;
		int[] arr = new int[N + 1];
		
		Arrays.fill(arr, 1000000);
		
		arr[1] = 0;
		
		for (int now = 2; now <= N; now++) {
			if (now % 3 == 0 && now % 2 == 0) {
				temp = Math.min(arr[now / 3], arr[now/2]);
				arr[now] = Math.min(temp, arr[now - 1]) + 1;
			}
			else if (now % 3 == 0) {
				arr[now] = Math.min(arr[now / 3], arr[now - 1]) + 1;
			}
			else if (now % 2 == 0) {
				arr[now] = Math.min(arr[now / 2], arr[now - 1]) + 1;
			}
			else arr[now] = arr[now - 1] + 1;
		}
		
		bw.write(arr[N] + "\n");
		
		int val = arr[N] - 1;
		for (int idx = N; idx != 1;) {
			if (arr[idx - 1] == val) {
				val--;
				bw.write(idx-- + " ");
			}
			else if (idx / 2 >= 0 && idx % 2 == 0 && arr[idx / 2] == val) {
				val--;
				bw.write(idx + " ");
				idx /= 2;
			}
			else if (idx / 3 >= 0 && idx % 3 == 0 && arr[idx / 3] == val) {
				val--;
				bw.write(idx + " ");
				idx /= 3;
			}
		}
		
		bw.write("1");
		bw.flush();
		br.close();
	}
}
