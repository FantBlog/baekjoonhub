import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        for (int i = 0; i < scoville.length; i++) pq.offer(scoville[i]);
        
        while (pq.peek() < K){
            if (pq.size() <= 1){
                answer = -1;
                break;
            }
            int temp = pq.poll();
            temp += pq.poll() * 2;
            pq.offer(temp);
            answer++;
        }
        
        return answer;
    }
}