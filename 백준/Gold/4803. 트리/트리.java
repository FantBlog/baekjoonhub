import java.io.*;
import java.util.*;

public class Main {
    
    static List<Integer>[] graph;
    static boolean[] isVisited;
    static int treeCnt, caseNum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        caseNum = 1;
        while (true) {
            st = new StringTokenizer(br.readLine(), " ");

            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if (n == 0 && m == 0) break;

            graph = new ArrayList[n + 1];
            for (int i = 1; i <= n; i++) {
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine(), " ");

                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                // 양방향 그래프
                graph[a].add(b);
                graph[b].add(a);
            }

            isVisited = new boolean[n + 1];
            treeCnt = 0;
            for (int i = 1; i <= n; i++) {
                if(isVisited[i]) continue;

                if (!dfs(i, 0)) treeCnt++;
            }

            if (treeCnt == 0) {
                System.out.printf("Case %d: No trees.\n", caseNum);
            } else if (treeCnt == 1) {
                System.out.printf("Case %d: There is one tree.\n", caseNum);
            } else {
                System.out.printf("Case %d: A forest of %d trees.\n", caseNum, treeCnt);
            }

            caseNum++;
        }
    }

    static boolean dfs(int x, int start) {
        isVisited[x] = true;
        
        for(int nxt : graph[x]){
        	if(nxt == start) continue;
            if(isVisited[nxt] || dfs(nxt, x)) return true;
        }
        
        return false;
    }
    

}
