class Solution {
    int MOD = 20170805;
    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        int[][][] arr = new int[m][n][2];
        arr[0][0][0] = 1;
        
        for (int r = 0; r < m; r++){
            for (int c = 0; c < n; c++){
                if (r == m - 1 && c == n - 1) continue;
                if (cityMap[r][c] == 0){
                    if (r < m - 1){
                        arr[r + 1][c][0] = (arr[r + 1][c][0] + arr[r][c][0]) % MOD;
                        arr[r + 1][c][0] = (arr[r + 1][c][0] + arr[r][c][1]) % MOD;
                    }
                    if (c < n - 1){
                        arr[r][c + 1][1] = (arr[r][c + 1][1] + arr[r][c][0]) % MOD;
                        arr[r][c + 1][1] = (arr[r][c + 1][1] + arr[r][c][1]) % MOD;
                    }
                }
                if (cityMap[r][c] == 2){
                    if (r < m - 1){
                        arr[r + 1][c][0] = (arr[r + 1][c][0] + arr[r][c][0]) % MOD;
                    }
                    if (c < n - 1){
                        arr[r][c + 1][1] = (arr[r][c + 1][1] + arr[r][c][1]) % MOD;
                    }
                }
            }
        }
        
        
        answer = arr[m-1][n-1][0] % MOD;
        answer = (answer + arr[m-1][n-1][1]) % MOD;
        return answer;
    }
}