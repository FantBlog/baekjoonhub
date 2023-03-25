import java.io.*;
import java.util.*;

public class Main {
	
	static class Hash{
		String key;
		Hash next;
	}
	
	static int tablesize;
	static Hash[] table;
	
	public static int hash(String str) {
		int hash = 5381;
		
		for (int i = 0; i < str.length(); i++) {
			int c = (int)str.charAt(i);
			hash = ((hash << 5) + hash + c) % tablesize;
		}
		if (hash < 0) hash *= -1;
		return hash % tablesize;
	}
	
	public static void init(int num) {
		tablesize = num;
		table = new Hash[tablesize];
	}
	
	public static void add(String key) {
		int num = hash(key);
		Hash input = new Hash();
		
		input.key = key;
		
		if (table[num] != null) {
			Hash now = table[num];
			while (now.next != null) {
				now = now.next;
			}
			now.next = input;
		}
		else {
			table[num] = input;
		}
		
	}

	public static boolean get(int num) {
		if (table[num] == null) return false;
		return true;
	}
	
	public static boolean find(String str) {
    	int hs;
		Hash result;
		hs = hash(str);
		result = table[hs];
    	while (result != null && !result.key.equals(str)) {
    		result = result.next;
    	}
    	if (result == null) return false;
    	else return true;
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        init(100003);
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()),M = Integer.parseInt(st.nextToken()), num, cnt = 0;
        String str;
        
        for (int i = 1; i <= N; i++) {
        	str = br.readLine();
        	num = hash(str);
        	add(str);
        }

        for (int i = 0; i < M; i++) {
        	str = br.readLine();
        	if (find(str)) cnt += 1;
        }
        System.out.println(cnt);
    }
}