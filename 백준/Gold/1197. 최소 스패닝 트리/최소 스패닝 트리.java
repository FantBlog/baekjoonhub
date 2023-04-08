import java.util.*;
import java.io.*;

class Node{
	int start;
	int end;
	int val;
	public Node(int a, int b, int c) {
		this.start = a;
		this.end = b;
		this.val = c;
	}
}
public class Main {
	static int[] sets;
	
	public static int find(int num) {
		if (sets[num] == num) return num;
		return sets[num] = find(sets[num]);
	}
	
	public static void union(int start, int end) {
		start = find(start);
		end = find(end);
		sets[end] = start;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		PriorityQueue<Node> que = new PriorityQueue<>(new Comparator<Node>(){
			@Override
			public int compare(Node n1, Node n2) {
				return n1.val < n2.val ? -1 : 1;
			}
		});
		
		for (int i = 0; i < E; i ++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			que.offer(new Node(a,b,c));
		}

		sets = new int[V + 1];
		
		for (int i = 1; i <= V; i ++) {
			sets[i] = i;
		}
		
		int total = 0;
		for (int i = 0; i < E; i ++) {
			Node now = que.poll();
			if (find(now.start) != find(now.end)) {
				total += now.val;
				union(now.start, now.end);
			}
		}
		bw.write(total + "");
		bw.flush();
		
	}
}
