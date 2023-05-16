import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> hs = new HashSet<>();
        for(int i = 0; i < numbers.length; i++){
            for (int j = i + 1; j < numbers.length; j++){
                hs.add(numbers[i] + numbers[j]);
            }
        }
		Iterator iter = hs.iterator();
        int[] answer = new int[hs.size()];
        int i = 0;
		while(iter.hasNext()) {
            answer[i++] = Integer.parseInt(iter.next() + "");
			// System.out.print(iter.next() + " ");
		}
        Arrays.sort(answer);
        return answer;
    }
}