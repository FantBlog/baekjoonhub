import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine()), point = 0, now, start, end, mid;
        int[] arr = new int[N + 1], dp = new int[N + 1], input = new int[N + 1];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 1; i <= N; i++) {
        	now = Integer.parseInt(st.nextToken()) + 1000000001;
        	input[i] = now;
        	
        	if (arr[point] < now) {
        		arr[++point] = now;
        		dp[i] = point;
        	}
        	else {
        		start = 1;
                end = point;
        		while (start != end) {
        			mid = (start + end) / 2;
        			if (arr[mid] < now) {
        				start = mid + 1;
        			}
        			else {
        				end = mid;
        			}
        		}
        		arr[end] = now;
        		dp[i] = end;
        	}
        }
        
        int[] result = new int[point];
        int j = point - 1;
        
        for (int idx = N; idx > 0 && j >= 0; idx--) {
        	if (dp[idx] == j + 1) result[j--] = input[idx] - 1000000001;
        }
        
        bw.write(point + "\n");
        for (int i = 0; i < point; i++) bw.write(result[i] + " ");
        bw.flush();
    }
}