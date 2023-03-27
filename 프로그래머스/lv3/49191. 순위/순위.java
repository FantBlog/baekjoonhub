import java.io.*;
import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = n;
        int[][] arr = new int[n][n];
                
        for (int i = 0; i < n; i++) {
            arr[i][i] = 2;
        }
        
        for (int i = 0; i < edge.length; i++){
            arr[edge[i][0]-1][edge[i][1]-1] = 1; // r이 c에게 이김
            arr[edge[i][1]-1][edge[i][0]-1] = -1; // r이 c에게 짐
        }
        
        for (int r = 0; r < n; r++){
            for (int c = 0; c < n; c++){
                if (arr[r][c] == 1){
                    for (int k = 0; k < n; k++){
                        if (arr[c][k] == 1) {
                            arr[r][k] = 1;
                            arr[k][r] = -1;
                        }
                    }
                }
                if (arr[r][c] == -1){
                    for (int k = 0; k < n; k++){
                        if (arr[c][k] == -1) {
                            arr[r][k] = -1;
                            arr[k][r] = 1;
                        }
                    }
                }
            }
        }
        for (int r = 0; r < n; r++){
            for (int c = 0; c < n; c++){
                if (arr[r][c] == 0) {
                    answer--;
                    break;
                }
            }
        }
        return answer;
    }
}