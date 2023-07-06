import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][M];

        Queue<Index> que = new LinkedList<>();

        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                int temp = Integer.parseInt(st.nextToken());
                map[i][j] = temp;
                if(temp == 1){
                    Index shark = new Index(i, j, 1);
                    que.offer(shark);
                }
            }
        }

        bw.write(BFS(que, map, N, M) - 1 + "");
        bw.flush();

    }
    public static int BFS(Queue<Index> que, int[][] map, int N, int M){
        int start = 0;
        boolean check = false;
        // 8방 탐색
        int[][] dd = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

        // que가 빌때 까지 반복
        while(!que.isEmpty()){
            int len = que.size();
            for(int i = 0; i < len; i++){
                Index now = que.poll();
                check = false;
                for(int j = 0;j < 8; j++){
                    // 맵 밖으로 나가면 스킵
                    if (now.x_index + dd[j][0] < 0 || now.x_index + dd[j][0] >= N || now.y_index + dd[j][1] < 0 || now.y_index + dd[j][1] >= M) continue;
                    // 왔던 곳이면 스킵
                    if (map[now.x_index + dd[j][0]][now.y_index + dd[j][1]] != 0) continue;

                    map[now.x_index + dd[j][0]][now.y_index + dd[j][1]] = now.size + 1;
                    que.offer(new Index(now.x_index + dd[j][0], now.y_index + dd[j][1], now.size + 1));
                    start = Math.max(start, now.size + 1);
                }
            }
        }
        return start;
    }
    public static class Index{
        public int x_index;
        public int y_index;
        public int size;

        Index(int x, int y,int size){
            this.x_index = x;
            this.y_index = y;
            this.size = size;
        }
    }
}