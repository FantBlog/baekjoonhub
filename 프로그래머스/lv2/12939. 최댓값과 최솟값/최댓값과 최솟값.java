class Solution {
    public String solution(String s) {
        String answer = "";
        int max = 0, min = 0;
        String[] test = s.split(" ");
        for (int i = 0; i < test.length; i++){
            if (i == 0){
                max = Integer.parseInt(test[i]);
                min = Integer.parseInt(test[i]);
            }
            else {
                int now = Integer.parseInt(test[i]);
                if (now > max) max = now;
                if (now < min) min = now;
            }
        }
        answer = Integer.toString(min) + " " + Integer.toString(max);
        return answer;
    }
}