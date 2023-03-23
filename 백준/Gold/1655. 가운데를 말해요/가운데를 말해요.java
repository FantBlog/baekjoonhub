import java.io.*;
import java.util.*;

public class Main {
	static int[] min_heap = new int[131073], max_heap = new int[131073];
	static int mn_p = 0, mx_p = 0;
	
	public static void min_push(int num) {
		min_heap[++mn_p] = num;
		int i = mn_p, temp;
		while (i > 1) {
			if (min_heap[i / 2] < min_heap[i]) break;
			temp = min_heap[i / 2];
			min_heap[i / 2] = min_heap[i];
			min_heap[i] = temp;
			i /= 2;
		}
	}

	public static void max_push(int num) {
		max_heap[++mx_p] = num;
		int i = mx_p, temp;
		while (i > 1) {
			if (max_heap[i / 2] > max_heap[i]) break;
			temp = max_heap[i / 2];
			max_heap[i / 2] = max_heap[i];
			max_heap[i] = temp;
			i /= 2;
		}
	}
	
	public static int min_pop() {
		int result = min_heap[1], temp;
		min_heap[1] = min_heap[mn_p];
		min_heap[mn_p--] = 10001;
		
		for (int i = 1; i * 2 <= mn_p;) {
			if (min_heap[i] < min_heap[i * 2] && min_heap[i] < min_heap[i * 2 + 1]) break;
			if (min_heap[i * 2] < min_heap[i * 2 + 1]) {
				temp = min_heap[i * 2];
				min_heap[i * 2] = min_heap[i];
				min_heap[i] = temp;
				i = i * 2;
			}
			else {
				temp = min_heap[i * 2 + 1];
				min_heap[i * 2 + 1] = min_heap[i];
				min_heap[i] = temp;
				i = i * 2 + 1;
			}
		}
		return result;
	}

	public static int max_pop() {
		int result = max_heap[1], temp;
		max_heap[1] = max_heap[mx_p];
		max_heap[mx_p--] = -10001;
		
		for (int i = 1; i * 2 <= mx_p;) {
			if (max_heap[i] > max_heap[i * 2] && max_heap[i] > max_heap[i * 2 + 1]) break;
			if (max_heap[i * 2] > max_heap[i * 2 + 1]) {
				temp = max_heap[i * 2];
				max_heap[i * 2] = max_heap[i];
				max_heap[i] = temp;
				i = i * 2;
			}
			else {
				temp = max_heap[i * 2 + 1];
				max_heap[i * 2 + 1] = max_heap[i];
				max_heap[i] = temp;
				i = i * 2 + 1;
			}
		}
		return result;
	}
	
    public static void main(String[] args) throws IOException{
    	Arrays.fill(max_heap, -10001);
    	Arrays.fill(min_heap, 10001);
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	int N = Integer.parseInt(br.readLine()), num;
    	for (int i = 0; i < N; i++) {
    		num = Integer.parseInt(br.readLine());
    		
    		if (mn_p == mx_p) {
	    		if (max_heap[1] > num) {
	    			min_push(max_pop());
	    			max_push(num);
	    		}
	    		else if (mn_p == mx_p) {
	    			min_push(num);
	    		}
    			bw.write(min_heap[1] + "\n");
    		}
    		else {
    			if (min_heap[1] < num){
	    			max_push(min_pop());
	    			min_push(num);
	    		}
	    		else max_push(num);
    			bw.write(max_heap[1] + "\n");
    		}
    	}
    	bw.flush();
    }
}
