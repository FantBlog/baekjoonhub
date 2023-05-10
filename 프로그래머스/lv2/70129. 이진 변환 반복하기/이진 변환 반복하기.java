class Solution {
    public int[] solution(String s) {
        int cnt = 0, zeros = 0, ones = 0;
        while (true){
            ones = 0;
            // 0, 1 개수 새기
            for(int i = 0; i < s.length(); i++){
                if (s.charAt(i) == '0'){
                    zeros += 1;
                } else {
                    ones += 1;
                }
            }
            cnt += 1;
            if(ones == 1){
                break;
            }
            s = Integer.toBinaryString(ones);
        }
        int[] answer = {cnt, zeros};
        return answer;
    }
}