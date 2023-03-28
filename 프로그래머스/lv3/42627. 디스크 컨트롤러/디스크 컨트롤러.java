import java.util.*;
import java.io.*;

class Element implements Comparable<Element>{
	public int num; // 정렬의 기준이 될 값
	public int qurry; // 요청받은시간
	
	public Element(int num, int qurry){
		this.num = num;
		this.qurry = qurry;
	}
	
	public int[] get(){
        int[] result = {num, qurry};
		return result;
	}

	public int getqurry(){
		return qurry;
	}
	
	public int getnum(){
		return num;
	}

	@Override
	public int compareTo(Element o) {
		return qurry <= o.qurry ? -1 : 1;
	}
}
class Two extends Element{
	
	public Two(int num, int qurry) {
		super(num, qurry);
	}

	@Override
	public int compareTo(Element o) {
		return num <= o.num ? -1 : 1;
	}
}

class Solution {
    public static int solution(int[][] jobs) {
        int answer = 0;
        
        PriorityQueue<Element> q = new PriorityQueue<Element>();
        PriorityQueue<Two> stack = new PriorityQueue<Two>();
        
        for (int i = 0; i < jobs.length; i++){
            q.offer(new Element(jobs[i][1], jobs[i][0]));
        }
        
        int time = 0, sum = 0;
        
        while (q.size() > 0) {
        	if (q.peek().getqurry() >= time) {
        		if (stack.size() > 0) { // 작업이 밀려 있을때
                    Two now = stack.poll();
                    time += now.getnum();
                    sum += time - now.getqurry();
        		}
        		else { // 작업이없을때
        			Element now = q.poll();
            		time = now.getnum() + now.getqurry();
            		sum += time - now.getqurry();
            	}
        	}
        	else { // 작업중일때
        		Element temp = q.poll();
        		Two next = new Two(temp.getnum(), temp.getqurry());
        		stack.offer(next);
        	}
        	System.out.println(time + " " + sum);
        }

		if (stack.size() > 0) { // 작업이 밀려 있을때
			for (int i = 0; i < stack.size();) {
    			Two now = stack.poll();
        		time += now.getnum();
        		sum += time - now.getqurry();
            	System.out.println(time + " " + sum);
			}
		}
        answer = sum / jobs.length;
        return answer;
    }
}