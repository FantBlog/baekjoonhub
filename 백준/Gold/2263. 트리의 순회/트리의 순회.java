import java.io.*;
import java.util.*;

public class Main {
	static int[] in, po, result, idx;
	static int point = 0;
	
	public static void pre(int i_s, int i_e, int p_s, int p_e) {
		if (i_e - i_s == 1) {
			if(in[i_s] != po[p_s]) {
				result[point++] = in[i_s];
				result[point++] = in[i_e];
			}
			else {
				result[point++] = in[i_e];
				result[point++] = in[i_s];
			}
			return;
		}
		else if(i_s == i_e) {
			result[point++] = in[i_s];
			return;
		}
		
		int x = idx[po[p_e]];
		result[point++] = po[p_e];
		
		if (x != i_s) pre(i_s, x - 1, p_s, p_s + x - i_s - 1);
		if (x != i_e) pre(x + 1, i_e, p_e - (i_e - x), p_e - 1);
	}

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        
        in = new int[N + 1];
        po = new int[N + 1];
        result = new int[N];
        idx = new int[N + 1];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
        	int now = Integer.parseInt(st.nextToken());
        	in[i] = now;
        	idx[now] = i;
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
        	po[i] = Integer.parseInt(st.nextToken());
        }

        pre(1, N, 1, N);
        
        for (int i = 0; i < N; i++) bw.write(result[i] + " ");
        
        bw.flush();
    }
}