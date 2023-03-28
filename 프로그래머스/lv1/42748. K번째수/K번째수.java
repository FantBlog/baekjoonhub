class Solution {
	static int[] arr, soarr;
	
	public static void sort(int start, int end) {
		if (start == end) return;
		
		int center = (start + end) >> 1;
		
		sort(start, center);
		sort(center + 1, end);
		merge(start, end);
	}
	
	public static void merge(int start, int end) {
		int center = (start + end) >> 1, lp = start, rp = center + 1, p = 0;
		
		while (lp <= center && rp <= end) {
			if (arr[lp] <= arr[rp]) soarr[p++] = arr[lp++];
			else soarr[p++] = arr[rp++];
		}
		while (lp <= center) soarr[p++] = arr[lp++];
		while (rp <= end) soarr[p++] = arr[rp++];
		
		for (int i = start; i <= end; i++) arr[i] = soarr[i-start];
	}
	
	public int find(int[] array, int start, int end, int target) {
		arr = new int[end - start + 1];
		soarr = new int[end - start + 1];
		
		for (int i = start; i <= end; i++) {
			arr[i - start] = array[i];
		}
		
		sort(0, end - start);
		
		return arr[target];
	}
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++){
            answer[i] = find(array, commands[i][0] - 1, commands[i][1] - 1, commands[i][2] - 1);
        }
        return answer;
    }
}