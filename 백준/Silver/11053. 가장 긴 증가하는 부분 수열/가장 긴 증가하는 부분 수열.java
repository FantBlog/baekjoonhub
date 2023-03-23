import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine()), point = 0, now;
        int[] arr = new int[N + 1];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 1; i <= N; i++) {
        	now = Integer.parseInt(st.nextToken());
        	
        	if (arr[point] < now) {
        		arr[++point] = now;
        		continue;
        	}
        	else {
        		int start = 1, end = point, mid;
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
        	}
        	
        }
        bw.write(point + "");
        bw.flush();

    }
}