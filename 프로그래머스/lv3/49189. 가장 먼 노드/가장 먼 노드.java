import java.io.*;
import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0, cnt = 0;
        LinkedList<Integer>[] arr = new LinkedList[n];
        for(int i=0; i<n; i++) {
            arr[i] = new LinkedList<>();
        }
        
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
                
        for (int i = 0; i < edge.length; i++){
            arr[edge[i][0] - 1].add(edge[i][1] - 1);
            arr[edge[i][1] - 1].add(edge[i][0] - 1);
        }
        queue.add(0);
        visited[0] = true;
        
        while (queue.size() > 0){
            cnt = 0;
            int size = queue.size();
            System.out.println(queue.toString());
            for (int i = 0; i < size; i++){
                int now = queue.poll(); // 지금 출발
                
                for (Integer j : arr[now]){ // 이어진 도착점들
                    if (!visited[j]){ // 안간곳이면
                        visited[j] = true;
                        queue.add(j);
                        cnt++;
                    }
                }
            }
            if (queue.size() == 0) break;
            answer = cnt;
        }
        return answer;
    }
}