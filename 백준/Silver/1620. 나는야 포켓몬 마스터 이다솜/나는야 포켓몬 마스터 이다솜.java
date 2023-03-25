import java.io.*;
import java.util.*;

public class Main {
	static class Hash{
		public Hash() {
		}
		String key;
		int value;
		Hash next;
	}
	static int tablesize;
	static Hash[] table;
	static int[] arr;
	
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
	
	public static void add(String key, int value) {
		int num = hash(key);
		Hash input = new Hash();
		
		input.key = key;
		input.value = value;
		
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

	public static boolean isInteger(String strValue) {
		try {
	        Integer.parseInt(strValue);
	        return true;
	    } catch (NumberFormatException ex) {
	        return false;
	    }
	}
	
	public static void find(String str) {
    	int hs;
		Hash result;
    	if (isInteger(str)) {
    		hs = arr[Integer.parseInt(str)];
    		result = table[hs];
        	while (result.value != Integer.parseInt(str)) {
        		result = result.next;
        	}
    		System.out.println(result.key);
    	}
    	else {
    		hs = hash(str);
    		result = table[hs];
        	while (!result.key.equals(str)) {
        		result = result.next;
        	}
    		System.out.println(result.value);
    	}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        init(100003);
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()),M = Integer.parseInt(st.nextToken()), num;
        arr = new int[N + 1];
        String str;
        
        for (int i = 1; i <= N; i++) {
        	str = br.readLine();
        	num = hash(str);
        	arr[i] = num;
        	add(str, i);
        }

        for (int i = 0; i < M; i++) {
        	str = br.readLine();
        	find(str);
        }
    }
}