class Solution {
    public int solution(int n) {
        if (n % 2 == 1) return 0;
        
        long DIV = 1000000007;
        int answer = 0;
        long[] dp = new long[n + 1];
        // 홀수 일때 0
        dp[0] = 1;
        dp[2] = 3;
        for (int i = 4; i <= n; i+=2){
            dp[i] = (DIV + (dp[i - 2] * 4 % DIV) - dp[i - 4] % DIV) % DIV;
        }
        answer = (int) dp[n];
        return answer;
    }
}