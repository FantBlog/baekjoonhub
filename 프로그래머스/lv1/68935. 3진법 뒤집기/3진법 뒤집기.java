class Solution {
    public int solution(int n) {
        int answer = 0;
        String temp = "";
        
        while (n >= 3){
            temp += (n % 3) + "";
            n /= 3;
        }
        temp += (n % 3) + "";
        
        System.out.println(temp);
        
        for (int j = 0; j < temp.length() ; j++){
            answer += Integer.parseInt(temp.charAt(j) + "") * Math.pow(3,temp.length() - 1 - j);
        }
        
        return answer;
    }
}