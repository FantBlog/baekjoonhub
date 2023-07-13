import java.io.*;
import java.util.*;

public class Main {
    static int W, H, max_cnt;
    static int[][] visited, count;
    static char[][] world;
    static int[][] dirt = {{0,1},{1,0},{0,-1},{-1,0}};
    static Queue<Que> queue = new LinkedList<>();

    public static void BFS(Que que){
        int x = que.x;
        int y = que.y;
        int curve_cnt = que.curve_cnt;
        int dd = que.dd;

        if (world[y][x] == 'C' && dd != 5) {
            max_cnt = Math.min(max_cnt, curve_cnt);
            return;
        }

        if( curve_cnt >= max_cnt ) return;

        for ( int nd = 0; nd < 4; nd++) {
            int nx = x + dirt[nd][0];
            int ny = y + dirt[nd][1];

            if (nx < 0 || W <= nx || ny < 0 || H <= ny) continue;
            if (world[ny][nx] == '*') continue;

            int next_cnt;
            if (dd == 5 || dd == nd) next_cnt = curve_cnt;
            else next_cnt = curve_cnt + 1;

            // 가로로 오면 1 세로로 오면 2
            // 홀수면 가로
            // 가로 세로 비교 이후 횟수 비교
            if (nd % 2 == 1 && (visited[ny][nx] == 1 || visited[ny][nx] == 0)){
                queue.add(new Que(nx, ny, next_cnt, nd));
                visited[ny][nx] += 2;
                count[ny][nx] = next_cnt;
            }
            else if (nd % 2 == 0 && (visited[ny][nx] == 2 || visited[ny][nx] == 0)){
                queue.add(new Que(nx, ny, next_cnt, nd));
                visited[ny][nx] += 1;
                count[ny][nx] = next_cnt;
            } else if (count[ny][nx] > next_cnt){
                queue.add(new Que(nx, ny, next_cnt, nd));
                count[ny][nx] = next_cnt;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        /*
		String st = new String(br.readLine());
		long N = Long.parseLong(br.readLine());
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
		st.nextToken();
        */

        max_cnt = 10000000; // 대충 큰숫자

        StringTokenizer st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        world = new char[H][W];
        visited = new int[H][W];
        count = new int[H][W];

        int start_x = 0, start_y = 0;

        for(int y = 0; y < H; y++){
            String str = br.readLine();
            for(int x = 0; x < W; x++){
                world[y][x] = str.charAt(x);
                count[y][x] = 10000000;
                if (str.charAt(x) == 'C' && queue.isEmpty()){
                    queue.add(new Que(x, y, 0, 5));
                    visited[y][x] = 3;
                    count[y][x] = 0;
                }
            }
        }

        while (!queue.isEmpty()){
            BFS(queue.poll());
        }

        bw.write(max_cnt + "");
        bw.flush();
    }

}
class Que{
    int x;
    int y;
    int curve_cnt;
    int dd;
    public Que(int x, int y, int c, int d){
        this.x = x;
        this.y = y;
        this.curve_cnt = c;
        this.dd = d;
    }
}