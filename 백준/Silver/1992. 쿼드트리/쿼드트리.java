import java.util.*;
import java.io.*;

public class Main {
	static BufferedWriter bw;
	static int[][] arr;
	
	public static void quad(int r, int c, int size) throws IOException {
		int half = size>>1, pass = (int) size * size, cnt = 0;
		
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				if (arr[i][j] == 1) cnt++;
			}
		}
		if (cnt == pass) bw.write("1");
		else if (cnt == 0) bw.write("0");
		else {
			if (size != 1) bw.write("(");
			quad(r, c, half);
			quad(r, c + half, half);
			quad(r + half, c, half);
			quad(r + half, c + half, half);
			if (size != 1) bw.write(")");
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		
		arr = new int[N][N];
		
		int cnt = 0;
		String st;
		for (int i = 0; i < N; i++) {
			st = br.readLine();
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.charAt(j)+"");
				if (st.charAt(j) == '1') cnt ++;
			}
		}
		
		quad(0, 0, N);
		
		bw.flush();
		
	}
}
