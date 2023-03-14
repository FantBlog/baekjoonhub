import java.io.*;
import java.util.*;

class llist {
    int r;
    int c;
    int dust;
    llist right;

    public void set(int r, int c, int dust) {
        this.c = c;
        this.r = r;
        this.dust = dust;
    }
}

class que {
    int leng = 0;
    llist start;
    llist end;

    public int getLeng() {
        return leng;
    }

    public void append(int r, int c, int dust) {
        if (leng == 0) {
            llist now = new llist();
            now.set(r, c, dust);
            start = now;
            end = now;
        } else {
            llist now = new llist();
            now.set(r, c, dust);
            end.right = now;
            end = now;
        }
        leng++;
    }

    public int[] popleft() {
        int[] result = {-1, -1, -1};

        if (leng == 0) return result;

        result[0] = start.r;
        result[1] = start.c;
        result[2] = start.dust;
        start = start.right;
        leng--;
        return result;
    }
}

public class Main {
    static int R, C, T, cleaner;
    static int[][] arr;
    static int[] dc = {0, -1, 0, 1}, dr = {1, 0, -1, 0};
    static que que;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        cleaner = -1;

        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        arr = new int[R][C];
        que = new que();

        for (int r = 0; r < R; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < C; c++) {
                arr[r][c] = Integer.parseInt(st.nextToken());
                if (cleaner == -1 && arr[r][c] == -1) {
                    cleaner = r;
                }
            }
        }

        for (int t = 0;t<T;t++) {
            find();

            bfs();

            air();
        }

        bw.write(sum() + "");
        bw.flush();
        br.close();
        bw.close();
    }

    public static void find() {
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (arr[r][c] > 0) {
                    que.append(r, c, arr[r][c]);
                }
            }
        }
    }
    public static int sum() {
        int result = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (arr[r][c] > 0) {
                    result += arr[r][c];
                }
            }
        }
        return result;
    }
    public static void bfs() {
        int N = que.getLeng();
        int nr, nc;

        for (int i = 0; i < N; i++) {
            int[] temp = que.popleft();
            int r = temp[0];
            int c = temp[1];
            for (int j = 0; j < 4; j++) {
                nr = r + dr[j];
                nc = c + dc[j];
                if (nr < 0 || nc < 0 || nr >= R || nc >= C) continue;
                if (arr[nr][nc] == -1) continue;

                arr[nr][nc] = arr[nr][nc] + temp[2] / 5;
                arr[r][c] = arr[r][c] - temp[2] / 5;
            }
        }
    }

    public static void air() {
        int temp;
        int temp2 = 0;
        for (int c = 1; c < C; c++) {
            temp = arr[cleaner][c];
            arr[cleaner][c] = temp2;
            temp2 = temp;
        }
        for (int r = cleaner - 1; r >= 0; r--) {
            temp = arr[r][C - 1];
            arr[r][C - 1] = temp2;
            temp2 = temp;
        }
        for (int c = C - 2; c >= 0; c--) {
            temp = arr[0][c];
            arr[0][c] = temp2;
            temp2 = temp;
        }
        for (int r = 1; r < cleaner; r++) {
            temp = arr[r][0];
            arr[r][0] = temp2;
            temp2 = temp;
        }

        temp2 = 0;
        for (int c = 1; c < C; c++) {
            temp = arr[cleaner + 1][c];
            arr[cleaner + 1][c] = temp2;
            temp2 = temp;
        }
        for (int r = cleaner + 2; r < R; r++) {
            temp = arr[r][C - 1];
            arr[r][C - 1] = temp2;
            temp2 = temp;
        }
        for (int c = C - 2; c >= 0; c--) {
            temp = arr[R-1][c];
            arr[R-1][c] = temp2;
            temp2 = temp;
        }
        for (int r = R - 2; r > cleaner + 1; r--) {
            temp = arr[r][0];
            arr[r][0] = temp2;
            temp2 = temp;
        }
    }
}