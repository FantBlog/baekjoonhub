import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int top = 0, cnt = 1;

        for (int i = 1; i < arr.length; i++){
            if (arr[i] != arr[top]) {
                arr[++top] = arr[i];
                cnt++;
            }
        }
        int[] answer = new int[cnt];

        for (int i = 0; i < cnt; i++){
            answer[i] = arr[i];
        }

        return answer;
    }
}