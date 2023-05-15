class Solution {
    public int[] solution(int n, long left, long right) {
        int[] answer = new int[(int)(right - left + 1)];
        
        for(long i = left; i <= right; i++){
            int a = (int) (i / n);
            int b = (int) (i % n);
            answer[(int)(i - left)] = Math.max(a,b) + 1;
        }
        
        return answer;
    }
}