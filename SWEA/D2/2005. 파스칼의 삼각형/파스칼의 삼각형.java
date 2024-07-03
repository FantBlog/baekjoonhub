import java.util.Scanner;
import java.io.FileInputStream;
class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T,  n;
		T=sc.nextInt();
        int[][] solu = new int[10][10];
        String a;
        
        for(int i = 0; i < 10; i ++){
            for(int j = 0; j <= i; j++){
                if(j == 0){
                    solu[i][j] = 1;
                }
                else{
                    solu[i][j] = solu[i-1][j-1] + solu[i-1][j];
                }
            }
        }
        
		for(int test_case = 1; test_case <= T; test_case++)
		{
			n=sc.nextInt();
            System.out.println(String.format("#%d", test_case));
            for(int i = 0; i < n; i++){
                a = "";
                for(int j = 0; j <= i; j++){
                    a = a + solu[i][j];
                    a = a + " ";
                }
				System.out.println(a);
            }
		}
	}
}